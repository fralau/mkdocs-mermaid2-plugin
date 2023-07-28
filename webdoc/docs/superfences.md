# Using the mermaid2 with Superfences

## Introduction

[Superfences](https://facelessuser.github.io/pymdown-extensions/extensions/superfences/) is a markdown extension that allows a better management
of code blocks, particularly syntax highlighting for the different languages.

!!! Warning
    Do not use the [codehilite](https://python-markdown.github.io/extensions/code_hilite/) markdown extension, as it is deprecated in this context.

Hence, for a Python code block:

```python
import foo.bar
```

It belongs to the PyMdown extension package (see [installation instructions](https://facelessuser.github.io/pymdown-extensions/installation/)) created
by [facelessuser](https://github.com/facelessuser).


!!! Danger "Caution with Superfences"
    The problem is that if you activate Superfences, you will deactivate
    automatically the display of Mermaid diagrams (they will simply be
    color-highlighted), **unless** you specify an exception for those diagrams,
    called a **custom_fence**.


    Hence the code:

        ```mermaid
        graph LR
            hello --> world
            world --> again
            again --> hello
        ```

    Will be highlighted instead of being displayed!

    See the next paragraph, for how to do that.

!!! Important
    The Superfences extension is **not** mandatory, its main purpose
    is to allow highlighting in code blocks.

    It is, however, [**recommended** for the Material theme](#usage-for-the-material-theme).


## Specifying the Mermaid custom fence 

Hence, to speciy the custom fence in the configuration file:

```yaml
markdown_extensions:
  ...
  - pymdownx.superfences:
        # make exceptions to highlighting of code:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:mermaid2.fence_mermaid
```

Each time a code block of `mermaid` type is found in the markdown,
then the code will **not** be highlighted, but transformed into a diagram.
This is done by the `fence_mermaid` function provided by mermaid2, 
which encloses the Mermaid code
in the following way (in alignment with the plugin's policy):

    <div class="mermaid">
    ...
    </div>

!!! Note "Important"

    1. For better results with the Material theme, use the `fence_mermaid_custom`
        function (see below).
    2. Do not use `fence_mermaid_custom` with themes other than Material, as
        this will prevent the Mermaid diagrams from displaying.
    3. Superfences is slightly more demanding with
       HTML tags inside a mermaid diagram: 
       **take care to always close the HTML tags that require it**
       (e.g. `<small>` must have its corresponding `</small>` tag).
       Otherwise, the extension system will attempt to close those tags 
       and it will break the diagram.


## Usage for the Material theme
The [Material theme](https://squidfunk.github.io/mkdocs-material/), developed by [squidfunk](https://github.com/squidfunk), is designed out of the box 
[so as to exploit the Mermaid.js library](https://squidfunk.github.io/mkdocs-material/reference/diagrams/). 

A beautiful feature is that the color theme will be reflected
on the mermaid diagram, with a much better rendering of the diagrams
according to the palette.

It will also use proper colors for Mermaid diagrams if you use a **dark mode**
in the theme (`scheme: slate`) e.g., in the Config file:

```yaml
theme: 
  # name: readthedocs
  name: material
  language: en
  palette:
    scheme: slate
    primary: red
    accent: pink
```


!!! Important "Recommended usage with Material theme"
    This requires, however,

    1. The use of the Superfences extension.
    2. To use the default `<pre class="mermaid"><code>` representation, and
    not the `<div class="mermaid">` representation used by mkdocs-mermaid2.
    **This is achieved by using the `fence_mermaid_custom` function.**
    

Hence in the configuration file:

```yaml
markdown_extensions:
  ...
  - pymdownx.superfences:
        # make exceptions to highlighting of code:
      custom_fences:
        - name: mermaid
          class: mermaid
          format: !!python/name:mermaid2.fence_mermaid_custom
```

