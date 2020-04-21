# mkdocs-mermaid2-plugin

An [MkDocs](https://www.mkdocs.org/) plugin that renders textual graph
descriptions into [Mermaid](https://mermaid-js.github.io/mermaid) graphs
(flow charts, sequence diagrams, pie charts, etc.).



> This is a fork from
> [Pugong Liu's excellent project](https://github.com/pugong/mkdocs-mermaid-plugin), 
> which is no longer maintained. It offers expanded documentation as
> well as new functions.



<!-- To update, run the following command:
markdown-toc -i README.md 
-->

<!-- toc -->

- [Note for users of version < 1.0.5](#note-for-users-of-version--105)
- [How it works](#how-it-works)
- [Installation](#installation)
  * [Automatic](#automatic)
  * [Manual](#manual)
- [Configuration](#configuration)
- [Usage](#usage)
  * [General Principle](#general-principle)
  * [How to write Mermaid diagrams](#how-to-write-mermaid-diagrams)
  * [Adding arguments to the Mermaid engine](#adding-arguments-to-the-mermaid-engine)
  * [Tip: Adding Hyperlinks to a Diagram](#tip-adding-hyperlinks-to-a-diagram)

<!-- tocstop -->

## Note for users of version < 1.0.5
For users of versions before 0.1.5, 
note that the names were harmonized/simplified. 
The name of the installed
application has changed (now _mkdocs-mermaid2-plugin_ instead of 
_mkdocs-mermaid-plugin2_). Also, the reference within the configuration 
file of mkdocs is now _mermaid2_ instead of _markdownmermaid2_.

Before reinstalling, uninstall the previous version:

    pip uninstall mkdocs-mermaid-plugin2

Also change the reference in the `mkdocs.yml` file of your mkdocs project: 

    plugins:
      ...
      - mermaid2:



## How it works
This plugin transfers the Mermaid code (text) describing the graph 
into the final HTML page:

    <div class="mermaid">
    ...
    <\div>

It also inserts a call to the 
[javascript library](https://github.com/mermaid-js/mermaid) :

    <script>
    mermaid.initialize(...)
    </script>

The user's browser will then read this code and render it on the fly.

> No svg/png images are harmed during the rendering of that graph.


## Installation

### Automatic
Clone this repository and install the package with pip:

```bash
pip install mkdocs-mermaid2-plugin
```

### Manual
Clone this repository into a local directory and:

```bash
python setup.py install
```

## Configuration

To enable this plugin, you need to declare it in your config file
(`mkdocs.yml`).

In order to work, the plugin also requires the
[mermaid](https://www.npmjs.com/package/mermaid) javascript
library (in the exemple below, it fetched from the last version
from the [unpkg](https://unpkg.com/) repository; change the version
no as needed).

```yaml
plugins:
    - search
    - mermaid2

extra_javascript:
    - https://unpkg.com/mermaid@8.5.0/dist/mermaid.min.js
```

> **Note:** Don't forget to include the mermaid.min.js (local or remotely) in your `mkdocs.yml`

> **Note:**  If you declare plugins you need to declare _all_ of them, 
> including `search` (which would otherwise have been installed by default.)


## Usage

### General Principle
In order to insert a Mermaid diagram in a markdown page, simply 
type it using the mermaid syntax,
and surround it with the code fence for Mermaid:


    ```mermaid
    graph TD
    A[Client] --> B[Load Balancer]
    B --> C[Server01]
    B --> D[Server02]
    ```

### How to write Mermaid diagrams
* For instructions on how to make a diagram, see 
  [the official website](https://mermaid-js.github.io/mermaid/#/).
* If you are not familiar, see the [n00bs' introduction to mermaid](https://mermaid-js.github.io/mermaid/#/n00b-overview).
* In case of doubt, you will want to test your diagrams in the
  [Mermaid Live Editor](https://mermaid-js.github.io/mermaid-live-editor).


### Adding arguments to the Mermaid engine

By default, the plugin automatically inserts 
the a Javascript command `mermaid.initialize();`
in the HTML pages, which starts the interpretation.
Sometimes, however, you may want to add some
initialization commands (see [full list](https://github.com/knsv/mermaid/blob/master/docs/mermaidAPI.md#mermaidapi-configuration-defaults)).

For example, you could change the theme of the diagram, 
using 'dark' instead of the default one. 
Simply add those arguments in the config file, e.g.

```yaml
plugins:
    - search
    - markdownmermaid2:
        arguments:
          theme: 'dark'


extra_javascript:
    - https://unpkg.com/mermaid@8.5.0/dist/mermaid.min.js
```

### Tip: Adding Hyperlinks to a Diagram

It is possible to add hyperlinks to a  diagram, e.g.:

```
box1[An <b>important</b> <a href="http://google.com">link</a>] 
```

> By default, however, this is not going to work.

To enable this function, you need to relax mermaid's security level,
([since version 8.2](https://mermaid-js.github.io/mermaid/#/?id=special-note-regarding-version-82)).

> This requires, of course, your application taking responsibility 
> for the security of the diagram source.

If that is OK with you, you can set the argument in the configuration of the
plugin:

```yaml
    - markdownmermaid2:
        arguments:
          securityLevel: 'loose'
```