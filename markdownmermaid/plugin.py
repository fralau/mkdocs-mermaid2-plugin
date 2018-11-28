from mkdocs.plugins import BasePlugin
from bs4 import BeautifulSoup

class MarkdownMermaidPlugin(BasePlugin):
   
    def on_post_page(self, output_content, config, **kwargs):
        soup = BeautifulSoup(output_content, 'html.parser')
        for mermaid in soup.find_all("code",class_="mermaid"):
            # replace code with div
            mermaid.name="div"
            # replace <pre> 
            mermaid.parent.replace_with(mermaid)
            # print mermaid.parent
        return unicode(soup)