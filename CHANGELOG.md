# Changelog: Mkdocs-Mermaid2

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/) and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 1.2.1, 2024-11-02

* Added: a test framework with MkDocs-Test and pytest
* Changed: migrated from `setup.py` to `pyproject.toml`

## 1.1.2, 2024-09-05

* Changed: If the `javascript` parameter starts with http(s) and no Internet
access is available, a WARNING is now issued
(mkdocs no longer fails with an exception).

## 1.1.1, 2023-09-26

* Fixed: Bug with local javascript library 

## 1.1.0, 2023-09-01

* Added: Parameter `javascript` in config file for optionally specifying the
    URL or path of the Mermaid javascript library.

* Changed: Parameter `extra_javascript` in config file is DEPRECATED,
    for optionally specifying the URL or path of the Mermaid javascript library

* Changed: Updated documentation.

## 1.0.8, 2023-08-09

* Fixed: Arguments of config file not taken into consideration,
    for mermaid.js version > 10 (#82)

## 1.0.5, 2023-07-29

* Added: A new [doc website is available on Read The Docs](https://mkdocs-mermaid2.readthedocs.io/en/latest/).

## 1.0.1, 2023-07

* Added: Now the plugin works with versions of the library > 10 and lower (#75)
* Added: Added: A new [doc website is available on Read The Docs](https://mkdocs-mermaid2.readthedocs.io/en/latest/).
