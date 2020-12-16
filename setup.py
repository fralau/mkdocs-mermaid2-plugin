import os
from setuptools import setup, find_packages


VERSION = '0.5.1'

def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()

LONG_DESCRIPTION = (
    "A mkdocs plugin that interprets mermaid graphs in the markdown file."
    "To install, please follow instructions in the readme file."
    "This is a fork of the Pugong Liu's excellent project, "
    "which is no longer maintained."
)

setup(
    name='mkdocs-mermaid2-plugin',
    version=VERSION,
    description='A MkDocs plugin for including mermaid graphs in markdown sources',
    long_description=LONG_DESCRIPTION,
    keywords='mkdocs python markdown mermaid',
    url='https://github.com/fralau/mkdocs-mermaid2-plugin',
    author='pugong, Fralau',
    author_email='pugong.liu@gmail.com, fralau2035@yahoo.com',
    license='MIT',
    python_requires='>=3.5',
    install_requires=[
        'setuptools>=18.5',
        'beautifulsoup4>=4.6.3',
        'mkdocs>=1.0.4',
        'jsbeautifier',
        'pyyaml', # for testing
        'mkdocs-material', # for testing
        'requests',
        'pymdown-extensions >= 8.0'
    ],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Information Technology',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8'
    ],
    packages=find_packages(exclude=['*.tests']),
    entry_points={
        'mkdocs.plugins': [
            'mermaid2 = mermaid2.plugin:MarkdownMermaidPlugin'
        ]
    }
)
