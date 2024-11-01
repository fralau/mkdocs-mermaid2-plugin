"""
Testing the project

(C) Laurent Franceschetti 2024
"""


import pytest

from mkdocs_test import DocProject


from test.fixture import Mermaid2DocProject




def test_pages():
    "Test this project"

    FIND_TEXT = ["import mermaid", "mermaid.initialize", "esm.min.mjs"]

    # ----------------
    # First page
    # ----------------
    project = Mermaid2DocProject(".")
    build_result = project.build(strict=False)
    # did not fail
    return_code = project.build_result.returncode
    assert not return_code, f"Build returned with {return_code} {build_result.args})" 

    # ----------------
    # First page
    # ----------------
    page = project.get_page('index')

    # find the diagrams; they are divs
    diagrams = page.find_all('div', class_='mermaid')
    assert len(diagrams) == 2

    # find the mermaid script
    mermaid_script = page.find('script', type="module")
    for text in FIND_TEXT:
        assert text in mermaid_script.string, f"'{text}' not found!"

    # use the fixture:
    version = page.js_version
    print("Version:", version)
    assert version
    assert version > page.LIB_VERSION_CHANGE

    

    # ----------------
    # Second page
    # ----------------
    # there is intentionally an error (`foo` does not exist)
    page = project.get_page('second')
    diagrams = page.find_all('div', class_='mermaid')
    assert len(diagrams) == 3

    # with open('output_file.html', 'w') as f:
    #     f.write(page.html)
    




    