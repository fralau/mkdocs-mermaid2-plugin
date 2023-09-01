# Specifying the Mermaid Library

> _From version 1.1.0 of Mkdocs-Mermaid2_

## Introduction
By default, MkDocs-Mermaid2 automatically inserts the proper calls to
[the Mermaid.js library, according to the correct version](../description/#insertion-of-the-javascript-library) (all-in one file, or ESM),
so that the diagrams are correctly interpreted.

You may, however, specify your own version, using to the
`javascript` parameter of Mermaid2, 
in the [config file of MkDocs](https://mkdocs.readthedocs.io/en/859/user-guide/configuration/).

```yaml
plugins:
  - search
  - mermaid2:
      javascript: https://unpkg.com/mermaid@10.4.0/dist/mermaid.esm.min.mjs 
```

The files can be found on [unpkg](https://unpkg.com/browse/mermaid@10.4.0/) or [jsdelivr.com](https://www.jsdelivr.com/package/npm/mermaid).

Mkdocs-Mermaid2 will still insert the appropriate call to the library
into the HTML page, according to the type of library (as all-in-one
javascript function, or [ESM module](../description/#automatic-insertion-of-the-javascript-library)), as well as the [initialization
sequence](../description/#initialization-sequence).

To determine which version, it will use the extension:

File extension | Type | HTML Code
--- | -- |
`.js` | All-in-one javascript file (function) | `<script src="URL>"</script>`
`.mjs` | ESM Module | `<script type="module">import mermaid from "URL"</script>`


!!! Warning
    In that case, the `version` parameter is ignored.

## Deploying Mermaid.js with the MkDocs website

In case you wish to use local version of the Mermaid.js library,
you can do so.

```yaml
plugins:
  - search
  - mermaid2:
      javascript: js/mermaid.min.js  
```

The path is relative to the docs directory of Mkdocs. In the above example:

    mkdocs.yaml
    ├─ docs/
    │  ├─ index.md
    │  ├─ ...
    │  ├─ js/
    │  │  ├─ mermaid.min.js


The typical way to download the library from unpkg or cdn.jsdelivr.net,
changing the version number to determine the version you want
(here: **10.2.0**):

```
https://cdn.jsdelivr.net/npm/mermaid@10.2.0/dist/mermaid.min.js
```

!!! Note
    No explicit call to `mermaid.initialize()` is required, since it is
    automatically inserted by the plugin.

!!! Warning "Use the .js file"
    The recommended way to do this, is to work with the file that contains
    the traditional, all-in-one package that ends with `.js`.

    It **may** be possible to use the full ESM module (with a reference to
    the script that ends with `.mjs`). That would require, however, 
    downloading the whole directory structure. Using the `.mjs` file
    on its ownlwill definitely **not** work, since there will be broken
    links.


## Using `extra_javascript`

!!! Warning "DEPRECATED"

    As of version 1.1.0 of Mkdocs-Mermaid2, 
    using `extra_javascript` in the config file
    to explictly call the javascript library is DEPRECATED.
  


Mkdocs provides a standard mechanism for inserting a library into the
HTML pages, which relies on the
[parameter `extra_javascript` in the config file](https://mkdocs.readthedocs.io/en/859/user-guide/configuration/#extra_javascript).


```yaml
extra_javascript:
    - https://unpkg.com/mermaid@8.8.2/dist/mermaid.min.js
```

It still works for versions > 10:

```yaml
extra_javascript:
    - https://unpkg.com/mermaid@10.4.0/dist/mermaid.min.js
```

or (if using a local version):

```yaml
extra_javascript:
    - js/mermaid.min.js
```

(where the path is relative to the docs directory.)

**If Mkdocs-Mermaid2 detects a name of library that contains the
word `mermaid`, it will deactivate its own automatic/manual 
insertion mecanism and fall back on the standard mechanism of MkDocs.**




!!! Warning "Workaround for versions of MkDocs < 1.5"

    > _Versions of MkDocs < 1.5.0 were unable to call the ESM library._

    The best solution is to call the `.js` file:

    ```yaml
    extra_javascript:
        - https://unpkg.com/mermaid@10.2.0/dist/mermaid.min.js
    ```

   

    If you **really** want to use the ESM module,
    you could declare a local script file:

    ```yaml
    extra_javascript:
        - js/mermaidloader.js
    ```

    (where `js` is a subdirectory of the docs directory.)

    `mermaidloader.js` must contains the code for the import statement:

    ```javascript
    import mermaid from "https://unpkg.com/mermaid@10.0.2/dist/mermaid.esm.min.mjs"
    ```










