# mkdocs-markdownextradata-plugin

A MkDocs plugin that renders mermaid graph to mermaid style.

> This is a fork from Pugong Liu's excellent project, 
> which is no longer maintained."


## Installation

### Automatic
Install the package with pip:

```bash
pip install mkdocs-mermaid-plugin2
```

### Manual
Clone this repository:

```bash
python setup.py install
```

## Installation

To enable this plugin, you need to declare it in your config file
(`mkdocs.yml`).

In order to work, the plugin also requires the
[mermaid](https://www.npmjs.com/package/mermaid) javascript
library (in the exemple below, it fetched from the last version
from the [unpkg](https://unpkg.com/) repository; change the version
no as needed).

```yaml
plugins:
    - markdownmermaid2

extra_javascript:
    - https://unpkg.com/mermaid@8.5.0/dist/mermaid.min.js
```

> **Note:** Don't forget to include the mermaid.min.js (local or remotely) in your `mkdocs.yml`


## Usage

### General Principle
In order to insert a mermaid diagram, simply insert the diagram,
preceded by the language:


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
