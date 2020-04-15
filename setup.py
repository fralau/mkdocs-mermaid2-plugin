import os
from setuptools import setup, find_packages


VERSION = '0.1.3'

def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()

long_description = (
    "A mkdocs plugin that interprets mermaid graphs in the markdown file."
    "To install, please follow instructions in the readme file."
    "This is a fork of the Pugong Liu's excellent project, "
    "which is no longer maintained."
)

setup(
    name='mkdocs-mermaid-plugin2',
    version=VERSION,
    description='A MkDocs plugin for including mermaid graphs in markdown sources',
    long_description=long_description,
    keywords='mkdocs python markdown mermaid',
    url='https://github.com/pugong/mkdocs-mermaid-plugin',
    author='pugong, Fralau',
    author_email='pugong.liu@gmail.com, fralau2035@yahoo.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'setuptools>=18.5',
        'beautifulsoup4>=4.6.3',
        'mkdocs>=1.0.4',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'markdownmermaid2 = markdownmermaid.plugin:MarkdownMermaidPlugin'
        ]
    }
)
