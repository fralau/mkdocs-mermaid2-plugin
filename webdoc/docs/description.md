## Steps for the preparation of an HTML page

There are three steps in the preparation of the page:

1. Setting up the HTML code that wraps the diagram.
2. Inserting the javascript library (Mermaid.js) into the HTML page
3. Inserting the call to the library

## Conversion to HTML

When converting the markdown into HTML, mkdocs normally inserts the
Mermaid code (text) describing the diagram 
into segments:

    <pre class="mermaid">
    <code>
    ...
    </code>
    </pre>


To make the HTML/css page more robust for most mkdocs themes,
the mermaid plugin systematically converts
those segments directly into `<div>` elements:

    <div class="mermaid">
    ...
    </div>

!!! Note "Superfences extension"
    The principle remains the same 
    when using the [Superfences](superfences) extension, except
    when using the Material theme.

    That extension is **not** mandatory.

## Insertion of the Javascript Library
The plugin then inserts a call to the
[javascript library](https://github.com/mermaid-js/mermaid).

By default, the plugin will use one of the latest versions of Mermaid.js.

As already mentioned, you can specify, in the config file, the version
of Mermaid.js required:

```yaml
- mermaid2:
    version: '10.1.0'
```


!!! Note
    The behavior of the plugin depends of the version of Mermaid.js, because
    version 10.0.0 represents a significant change ([see changelog](https://github.com/mermaid-js/mermaid/blob/develop/CHANGELOG.md#1000)). 

=== "Mermaid.js > 10.0.0"

    > *From version 1.0 of mkdocs-mermaid2*

    [For versions from 10.0.0 of the Mermaid javascript library, the plugin uses the ESM format](https://github.com/mermaid-js/mermaid/releases/tag/v10.0.0), since
    it is the only one available. This requires a specific call from the HTML
    page e.g.:

    ``` html
    <script src="https://unpkg.com/mermaid@10.0.2/dist/mermaid.esm.min.mjs" type="module">
    </script>
    ```


    The plugin automatically inserts this call.

=== "Earlier versions"

    For an earlier version of the Mermaid.js (<10),
    the plugin uses the traditional call
    from HTML:

    ``` html
    <script src="https://unpkg.com/mermaid@8.8.2/dist/mermaid.min.js">
    </script>
    ```

    The plugin automatically inserts this call.


## Call to the Library

### Default sequence
To start displaying of the diagrams, the plugin then automatically inserts 
a separate call to initialize the Mermaid library:

    <script>
    mermaid.initialize()
    </script>


The user's browser will then read this code and render it on the fly.

> No svg/png images are produced during the rendering of that graph.

### Additional arguments to the Mermaid engine

Sometimes, however, you may want to add some
additional initialization commands (see [full list](https://github.com/knsv/mermaid/blob/master/docs/mermaidAPI.md#mermaidapi-configuration-defaults)).

For example, you could change the theme of the diagram, 
using 'dark' instead of the default one. 
Simply add those arguments in the config file, e.g.

```yaml
plugins:
    - search
    - mermaid2:
        arguments:
          theme: 'dark'
```

