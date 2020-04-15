"""
Main plugin module 
"""
import json

from mkdocs.plugins import BasePlugin
from mkdocs.config.config_options import Type as PluginType
from bs4 import BeautifulSoup


try:
    unicode
except NameError:
    # Python 3 doesn't have `unicode` as `str`s are all Unicode.
    unicode = str


class MarkdownMermaidPlugin(BasePlugin):
    """
    Plugin for interpreting Mermaid code
    """
    config_scheme = (

        ('foo', PluginType(str, default='hello')),
        ('arguments', PluginType(dict, default={}))
    )

    def config(self):
        "The plugin's specific configuration (under plugin > markdownmermaid2)"
        return self._config

    def on_config(self, config):
        """
        The initial configuration
        """
        # the plugin config is there
        self._config = config
        mermaid_args = self.config['arguments']
        print("[MERMAID] %s" % mermaid_args)
        

    def on_post_page(self, output_content, config, **kwargs):
        "Generate the HTML code for all code items marked as 'mermaid'"
        soup = BeautifulSoup(output_content, 'html.parser')
        mermaids = soup.find_all("code",class_="mermaid")
        hasMermaid = 0
        for mermaid in mermaids:
            hasMermaid = 1
            # replace code with div
            mermaid.name="div"
            # replace <pre> 
            mermaid.parent.replace_with(mermaid)

        if(hasMermaid==1):
            new_tag = soup.new_tag("script")
            # get the additional configuration:
            mermaid_args = self.config['arguments']
            assert isinstance(mermaid_args, dict)
            # initialization command
            new_tag.string="mermaid.initialize(%s);" % json.dumps(mermaid_args) 
            soup.body.append(new_tag)
            
        return unicode(soup)