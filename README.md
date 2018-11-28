# mkdocs-markdownextradata-plugin

A MkDocs plugin that render meraid graph to mermaid style


## Installation


Install the package with pip:

```bash
pip install mkdocs-mermaid-plugin
```

## Usage

Enable this plugin in your `mkdocs.yml`:

```yaml
plugins:
    - search
    - markdownmermaid

extra_javascript:
    - https://unpkg.com/mermaid@7.1.2/dist/mermaid.min.js
```

> **Note:** If you have no `plugins` entry in your config file yet, you'll likely also want to add the `search` plugin. MkDocs enables it by default if there is no `plugins` entry set, but now you have to enable it explicitly.

> **Note:** Don't forget to include the mermaid.min.js (local or remotely) in your `mkdocs.yml`

More information about plugins in the [MkDocs documentation][mkdocs-plugins]



[mkdocs-plugins]: http://www.mkdocs.org/user-guide/plugins/