"""
Main plugin module for mermaid2
"""

import os
# import pprint
# pp = pprint.PrettyPrinter(indent=4)

from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type as PluginType
from bs4 import BeautifulSoup


from . import pyjs
from .util import info, libname, url_exists



# ------------------------
# Constants and utilities
# ------------------------
# the default (recommended) mermaid lib
MERMAID_LIB_VERSION = '8.6.4'
MERMAID_LIB = "https://unpkg.com/mermaid@%s/dist/mermaid.min.js"


# ------------------------
# Plugin
# ------------------------
class MarkdownMermaidPlugin(BasePlugin):
    """
    Plugin for interpreting Mermaid code
    """
    config_scheme = (

        ('version', PluginType(str, default=MERMAID_LIB_VERSION)),
        ('arguments', PluginType(dict, default={}))
    )


    # ------------------------
    # Properties
    # ------------------------
    @property
    def full_config(self):
        """
        The full plugin's configuration object,
        which also includes the contents of the yaml config file.
        Note: do not call before on_config was run.
        """
        return self._full_config  
    
    @property
    def mermaid_args(self):
        """
        The arguments for mermaid
        Note: do not call before on_config was run.
        """
        return self._mermaid_args

    @property
    def extra_mermaid_lib(self):
        """
        Provides the mermaid library defined in mkdocs.yml
        Note: do not call before on_config was run.
        """
        extra_javascript = self.full_config.get('extra_javascript', [])
        for lib in extra_javascript:
            # get the actual library name
            if  libname(lib) == 'mermaid':
                return lib
        return ''


    @property
    def mermaid_lib(self):
        """
        Provides the actual mermaid library used
        """
        mermaid_version = self.config['version']
        lib = self.extra_mermaid_lib or MERMAID_LIB % mermaid_version 
        if not url_exists(lib):
            raise FileNotFoundError("Cannot find Mermaid library: %s" %
                                    lib)
        return lib

    # ------------------------
    # Event handlers
    # ------------------------
    def on_config(self, config):
        """
        The initial configuration
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
            info("Using default javascript library (%s):\n  "% 
                  self.config['version'],
                  self.mermaid_lib)
            
    def on_post_page(self, output_content, config, **kwargs):
        "Generate the HTML code for all code items marked as 'mermaid'"
        # print("--RAW--\n", output_content, "\n------")
        soup = BeautifulSoup(output_content, 'html.parser')
        mermaids = soup.find_all("div", class_="mermaid")
        has_mermaid = bool(len(mermaids))
        # print("PROCESSING MERMAID (%s)" % len(mermaids))

        if has_mermaid:
            if not self.extra_mermaid_lib:
                # if no extra library mentioned specify it
                new_tag = soup.new_tag("script", src=self.mermaid_lib)
                soup.body.append(new_tag)
            new_tag = soup.new_tag("script")
            # initialization command
            js_args =  pyjs.dumps(self.mermaid_args) 
            # print("Javascript args:", js_args)
            new_tag.string="mermaid.initialize(%s);" % js_args
            soup.body.append(new_tag)
            
        return str(soup)