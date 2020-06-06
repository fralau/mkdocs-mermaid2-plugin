"Exports of mermaid2"


def fence_mermaid(source, language, css_class, options, md, 
            classes=None, id_value='', **kwargs):
    """
    For mermaid loose mode:

    This function is needed for correctly displaying the mermaid
    HTML in diagrams when pymdownx.superfences is activated.

    It format sources as <div>...</div>, WITHOUT escaping
    the < and > characters in the HTML.

    It should be called in the mkdocs.yaml file as:

    markdown_extensions:
        - ...
        - ...
        - pymdownx.superfences:
            # make exceptions to highlighting of code:
            custom_fences:
                - name: mermaid
                class: mermaid
                format: !!python/name:mermaid2.fence_div_raw
    """

    if id_value:
        id_value = ' id="{}"'.format(id_value)
    classes = css_class if classes is None else ' '.join(classes + [css_class])

    html = '<code%s class="%s">%s</code>' % (id_value, classes, source)
    # print("--- Mermaid ---\n", html, "\n------")
    return html