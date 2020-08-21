"""
Special fence for PyMdown Extensions Superfences
See: https://facelessuser.github.io/pymdown-extensions/extensions/superfences/#formatters
"""

def fence_mermaid(source, language, css_class, options, md, 
            classes=None, id_value='', **kwargs):
    """
    For mermaid loose mode:

    This function is needed for correctly displaying the mermaid
    HTML in diagrams when pymdownx.superfences is activated.

    Contrary to the standard fence_div_format used in
    https://github.com/facelessuser/pymdown-extensions/blob/9489bd8d94eebf4a109b7dada613bc2db378e31f/pymdownx/superfences.py#L149,
    this function it format sources as <div>...</div> but
    WITHOUT escaping the < and > characters in the HTML.

    It should be called in the mkdocs.yaml file as:

    markdown_extensions:
        - ...
        - ...
        - pymdownx.superfences:
            # make exceptions to highlighting of code:
            custom_fences:
                - name: mermaid
                class: mermaid
                format: !!python/name:mermaid2.fence_mermaid
    """

    if id_value:
        id_value = ' id="{}"'.format(id_value)
    classes = css_class if classes is None else ' '.join(classes + [css_class])

    html = '<div %s class="%s">%s\n</div>' % (id_value, classes, source)
    # print("--- Mermaid ---\n", html, "\n------")
    return html

    