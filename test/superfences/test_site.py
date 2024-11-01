"""
Testing the project

Superfences, the behavior changes

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
    project.self_check()



    # ----------------
    # First page
    # ----------------
    page = project.get_page('index')



    # find the diagrams; they are divs
    diagrams = page.find_all('pre', class_='mermaid')
    assert len(diagrams) == 2
    assert diagrams[0].code.string.startswith('graph TD')
    print("Second diagram's code:\n", diagrams[1].code)
    assert diagrams[1].code.decode_contents().startswith('graph LR')

    # use the fixture:
    version = page.js_version
    print("Version:", version)
    assert version
    assert version > page.LIB_VERSION_CHANGE

    # Find the piece of color-highlighted Python code
    # now that the HTML is highlighted, it is almost unrecognizable
    # it contains a <code> tag that contains <span> tags.
    my_code = page.find('div', class_='highlight')
    assert my_code, "Couldn't find the expected highlighted code block."
    code_text = my_code.get_text() # that strips the tags
    assert 'page.read()' in code_text
    assert 'foo' not in code_text # negative control
    code = my_code.find('code')
    assert code, "Couldn't find code element!"
    spans = my_code.find_all('span')
    assert len(spans) > 5
    

    # ----------------
    # Second page
    # ----------------
    page = project.get_page('second')

    # find the diagrams; they are divs:
    diagrams = page.find_all('pre', class_='mermaid')
    assert len(diagrams) == 3
    wrong_diagram = diagrams[0].code.string # this one is wrong
    assert wrong_diagram.startswith('graph FG') 
    assert "A[Client]" in wrong_diagram
    # the other two are correct:
    assert diagrams[1].code.string.startswith('graph TD')
    assert diagrams[2].code.decode_contents().startswith('graph TD')

    # check that the second page has same version as first
    assert page.js_version == version
    




    