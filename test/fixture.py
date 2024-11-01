"""
Specific for MkDocs Projects

(C) Laurent Franceschetti 2024
"""

import re
import requests

from super_collections import SuperDict
from mkdocs_test import DocProject, MkDocsPage
from packaging import version


URL_PATTERN  = r'https://[^\s"]+'
VERSION_PATTERN = r"@(\d+\.\d+\.\d+)"

def extract_url(s:str) -> str|None:
    "Extract the first url from a string"
    match = re.search(URL_PATTERN, s)
    if match:
        url = match.group(0)
        return url
    else:
        return None


def get_last_version(mermaid_url:str) -> version.Version:
    "Get the last version from a mermaid url"
    response = requests.get(mermaid_url)
    version_no = response.url.split('@')[1].split('/')[0]
    return version.parse(version_no)



def assert_string_contains(txt:str, items:list) -> bool:
    """
    Find items in a string.
    All items must be present (AND); however, if one item is an
    iterable-non-string, then each subitem will an OR.

    ['foo', 'bar', ('baz', 'barbaz')] -> 'foo' AND 'bar' AND ('baz' OR 'barbaz')
    """
    for item in items:
        if isinstance(item, str):
            assert item in txt, f"'{item}' not found in:\n{txt}!"
        else:
            assert any(subitem in txt for subitem in item), f"None of {item} found in:\n{txt}!"



class Mermaid2Page(MkDocsPage):
    "Specific for Mermaid2"

    LIB_VERSION_CHANGE = version.parse('10')


    @property
    def mermaid_script(self) -> str:
        """
        Get the call to the mermaid javascript library
        (in the two versions, pre- and post- 10.0).

        Performs checks and initializes the js_version property.

        For testing purposes, this function contains INVARIANTS
        (principles that should remain the same in time, and 
        across different configurations).
        """
        try:
            self._mermaid_script
        except AttributeError:
            mermaid_script = self.find('script', type="module")
            if mermaid_script:
                # Version >= 10
                script_txt = mermaid_script.string
                FIND_TEXT = ["import mermaid", "esm.min.mjs", 
                            ('mermaid.initialize', 'mermaidConfig')]
                assert_string_contains(script_txt, FIND_TEXT)
                # Get the version number from the string; if not, from the Mermaid url:
                mermaid_url = extract_url(script_txt)
                assert mermaid_url, "No URL found for mermaid"
                assert 'mermaid' in mermaid_url, f"Error in url: {mermaid_url}"
                self._js_version = get_last_version(mermaid_url)
                return script_txt
            else:
                # Version < 10
                # Find the script calling the library
                mermaid_script = self.find('script', src=lambda x: x and 'mermaid' in x)
                assert mermaid_script, "Couldn't find the < 10 Mermaid library!"
                src = mermaid_script.get('src')
                match = re.search(VERSION_PATTERN, src)
                #  If < 10, it demands that the script version be explicit (x.y.z)
                if match:
                    version_str = match.group(1)
                    version = version.Version(version_str)
                    self._js_version = version
                else:
                    raise ValueError("No version number with < 10 Mermaid library")
                return mermaid_script.string



    @property
    def js_version(self) -> version.Version:
        """
        Get the version of the javascript library, while performing checks.
        """
        try:
            return self._js_version
        except AttributeError:
            # Initialize
            self.mermaid_script
            return self._js_version


class Mermaid2DocProject(DocProject):
    "Specific for MkDocs-Macros"

    @property
    def plugin_version(self) -> version.Version|None:
        "Get the Mermaid2 javascript library version from the plugin"
        plugin = self.get_plugin('mermaid2')
        try:
            return version.Version(plugin.version)
        except AttributeError:
            pass

 
    @property
    def pages(self) -> dict[Mermaid2Page]:
        "List of pages"
        pages = super().pages
        return {key: Mermaid2Page(value) for key, value in pages.items()}
    

 