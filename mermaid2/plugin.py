"""
Main plugin module for mermaid2
"""

import os

from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type as PluginType
from bs4 import BeautifulSoup

from . import pyjs
from .util import info, libname, url_exists


# ------------------------
# Constants and utilities
# ------------------------
# the default (recommended) mermaid lib
MERMAID_LIB_VERSION = '8.8.0'
MERMAID_LIB = "https://unpkg.com/mermaid@%s/dist/mermaid.min.js"
# Two conditions for activating custom fences:
SUPERFENCES_EXTENSION = 'pymdownx.superfences'
CUSTOM_FENCE_FN = 'fence_mermaid_custom' 

# ------------------------
# Plugin
# ------------------------
class MarkdownMermaidPlugin(BasePlugin):
    """
    Plugin for interpreting Mermaid code
    """
    config_scheme = (

        ('version', PluginType(str, default=MERMAID_LIB_VERSION)),
        ('arguments', PluginType(dict, default={})),
        # ('custom_loader', PluginType(bool, default=False))
    )


    # ------------------------
    # Properties
    # Do not call them before on_config was run!
    # ------------------------
    @property
    def full_config(self):
        """
        The full plugin's configuration object,
        which also includes the contents of the yaml config file.
        """
        return self._full_config  
    
    @property
    def mermaid_args(self):
        """
        The arguments for mermaid.
        """
        return self._mermaid_args

    @property
    def extra_mermaid_lib(self) -> str:
        """
        Provides the mermaid library defined in mkdocs.yml (if any)
        """
        extra_javascript = self.full_config.get('extra_javascript', [])
        for lib in extra_javascript:
            # get the actual library name
            if  libname(lib) == 'mermaid':
                return lib
        return ''


    @property
    def mermaid_lib(self) -> str:
        """
        Provides the actual mermaid library used
        """
        mermaid_version = self.config['version']
        lib = self.extra_mermaid_lib or MERMAID_LIB % mermaid_version 
        if not url_exists(lib):
            raise FileNotFoundError("Cannot find Mermaid library: %s" %
                                    lib)
        return lib


    @property
    def activate_custom_loader(self) -> bool:
        """
        Predicate: activate the custom loader for superfences?
        The rule is to activate:
            1. superfences extension is activated
            2. it specifies 'fence_mermaid_custom' as
               as format function (instead of fence_mermaid)
        """
        try:
            return self._activate_custom_loader
        except AttributeError:
            # first call:
            # superfences_installed = ('pymdownx.superfences' in 
            #             self.full_config['markdown_extensions'])
            # custom_loader = self.config['custom_loader']
            # self._activate_custom_loader = (superfences_installed and 
            #                                 custom_loader)
            # return self._activate_custom_loader
            self._activate_custom_loader = False
            superfences_installed = (SUPERFENCES_EXTENSION in 
                         self.full_config['markdown_extensions'])
            if superfences_installed:
                # get the config extension configs
                mdx_configs = self.full_config['mdx_configs']
                # get the superfences config, if exists:
                superfence_config = mdx_configs.get(SUPERFENCES_EXTENSION)
                if superfence_config:
                    info("Found superfences config: %s" % superfence_config)
                    custom_fences = superfence_config.get('custom_fences', [])
                    for fence in custom_fences:
                        format_fn = fence.get('format')
                        if format_fn.__name__ == CUSTOM_FENCE_FN:
                            self._activate_custom_loader = True
                            info("Found '%s' function: " 
                                 "activate custom loader for superfences" 
                                 % CUSTOM_FENCE_FN)
                            break
                    
            return self._activate_custom_loader

    # ------------------------
    # Event handlers
    # ------------------------
    def on_config(self, config):
        """
        The initial configuration
        store the configuration in properties
        """
        # the full config info for the plugin is there
        # we copy it into our own variable, to keep it accessible
        self._full_config = config
        # here we use the standard self.config property:
        # (this can get confusing...)
        self._mermaid_args = self.config['arguments']
        assert isinstance(self.mermaid_args, dict)
        info("Initialization arguments:", self.mermaid_args)
        # info on the javascript library:
        if self.extra_mermaid_lib:
            info("Explicit mermaid javascript library:\n  ", 
                 self.extra_mermaid_lib)
        else:
            info("Using javascript library (%s):\n  "% 
                  self.config['version'],
                  self.mermaid_lib)
            
    def on_post_page(self, output_content, config, page, **kwargs):
        """
        Actions for each page:
        generate the HTML code for all code items marked as 'mermaid'
        """
        soup = BeautifulSoup(output_content, 'html.parser')
        page_name = page.title
        # first, determine if the page has diagrams:
        if self.activate_custom_loader:
            # the custom loader has its specific marking
            # <pre class = 'mermaid'><code> ... </code></pre>
            info("Custom loader activated")
            mermaids = len(soup.select("pre.mermaid code"))
        else:
            # standard mermaid can accept two types of marking:
            # <pre><code class = 'mermaid'> ... </code></pre>
            # but since we want only <div> for best compatibility,
            # it needs to be replaced
            # NOTE: new versions of WHAT? use `language-mermaid`...
            pre_code_tags = (soup.select("pre code.mermaid") or 
                            soup.select("pre code.language-mermaid"))
            no_found = len(pre_code_tags)
            print("FOUND:", no_found)
            if no_found:
                info("Page '%s': found %s diagrams "
                     "(with <pre><code='mermaid'>), converting to <div>..." % 
                        (page_name, len(pre_code_tags)))
                for tag in pre_code_tags:
                    content = tag.text
                    new_tag = soup.new_tag("div", attrs={"class": "mermaid"})
                    new_tag.append(content)
                    # replace the parent:
                    tag.parent.replaceWith(new_tag)
            # Count the diagrams <div class = 'mermaid'> ... </div>
            mermaids = len(soup.select("div.mermaid"))
        # if yes, add the javascript snippets:
        if mermaids:
            info("Page '%s': found %s diagrams, adding scripts" % 
                    (page_name, mermaids))
            if not self.extra_mermaid_lib:
                # if no extra library mentioned specify it
                new_tag = soup.new_tag("script", src=self.mermaid_lib)
                soup.body.append(new_tag)
                # info(new_tag)
            new_tag = soup.new_tag("script")
            # initialization command
            if self.activate_custom_loader:
                # if the superfences extension is present, use the specific loader
                self.mermaid_args['startOnLoad'] = False
                js_args =  pyjs.dumps(self.mermaid_args) 
                #new_tag.string = "window.mermaidConfig = {\n    default: %s\n}" % js_args
                new_tag.string = "window.mermaidConfig = {default: %s}" % js_args
            else:
                js_args =  pyjs.dumps(self.mermaid_args) 
                new_tag.string="mermaid.initialize(%s);" % js_args
            soup.body.append(new_tag)
        return str(soup)