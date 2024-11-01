"""
Testing the project

Material theme, otherwise normal

(C) Laurent Franceschetti 2024
"""


import pytest

from mkdocs_test import DocProject

from test.fixture import Mermaid2DocProject




def test_pages():
    "Test this project"



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
    assert diagrams[0].string.startswith('graph TD')
    assert diagrams[1].string.startswith('gitGraph')

    # use the fixture:
    version = page.js_version
    assert version == project.plugin_version
    print("Version:", version)
    assert version
    assert version > page.LIB_VERSION_CHANGE

    # find the piece of Python code
    my_code = page.find('code', class_='language-python')
    assert 'page.read()' in my_code.string
    

    # ----------------
    # Second page
    # ----------------
    page = project.get_page('second')

    # find the diagrams; they are divs:
    diagrams = page.find_all('div', class_='mermaid')
    assert len(diagrams) == 3
    wrong_diagram = diagrams[0].string # this one is wrong
    assert wrong_diagram.startswith('graph FG') 
    assert "A[Client]" in wrong_diagram
    # the other two are correct:
    assert diagrams[1].string.startswith('graph TD')
    assert diagrams[2].string.startswith('graph TD')

    # check that the second page has same version as first
    assert page.js_version == version
    




    