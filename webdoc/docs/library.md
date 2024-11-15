# Using the JavaScript Mermaid Library

> _From version 1.1.0 of Mkdocs-Mermaid2_

## Introduction
By default, MkDocs-Mermaid2 automatically inserts the proper calls to
[the Mermaid.js library, according to the correct version](description.md/#insertion-of-the-javascript-library) (all-in one file, or ESM),
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

Mkdocs-Mermaid2 will still insert the appropriate call to the JavaScript library
into the HTML page, according to the type of library (as all-in-one
javascript function, or [ESM module](description.md/#automatic-insertion-of-the-javascript-library)),
as well as the [initialization
sequence](description.md/#initialization-sequence).

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

!!! Warning "Behavior in case of incorrect URL/no Internet access"
    1. An incorrect URL will cause an error that aborts MkDocs.
    2. If the address starts with http(s) and no Internet access
       is available at time of compile, MkDocs-Mermaid will continue and issue
       a WARNING. That behavior is for containers that do not
       have necessarily have Internet access at compile time
       (however, if you want to abort
       in that case use the strict mode: `mkdocs build --strict`.

## Using `extra_javascript`

Mkdocs, by default, provides a standard mechanism for inserting a library into the
HTML pages, which relies on the
[parameter `extra_javascript` in the config file](https://mkdocs.readthedocs.io/en/859/user-guide/configuration/#extra_javascript).


!!! Warning "DEPRECATED in default cases"
    As of version 1.1.0 of Mkdocs-Mermaid2, 
    using `extra_javascript` in the config file
    as the default solution to explictly call 
    the Mermaid javascript library is **DEPRECATED**.

    Use instead the standard config of Mkdocs-Mermaid2 parameters.


!!! Important "Failsafe mechanism"
    
    However, `extra_javascript` was not kept only
    as a backward compatibility measure.

    Its purpose is now to be a **failsafe mechanism**.

    **If Mkdocs-Mermaid2 detects a name of library that contains the
    word `mermaid`, it will deactivate its own automatic/manual 
    insertion mecanism and fall back on the standard mechanism of MkDocs.**

    You can (and possibly should) use `extra_javascript` mechanism,
    if the standard defaults
    of MkDocs-Plugin do not match your needs.



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


!!! Note "Going 'full manual'?"

    If you feel that you need the flexibility of the `extra_javascript`
    parameter,
    you might start to weigh the pros and cons of using MkDocs-Mermaid2
    as a plugin. 

    You might want to go "full manual", 
    **and deactivate the Mkdocs-Mermaid2 plugin.** 
    
    Or on the contrary, if you are using the **Material theme**, you might consider
    [using its default config for Mermaid](https://squidfunk.github.io/mkdocs-material/reference/diagrams/)
       (if it works better for you).


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










