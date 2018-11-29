import os
from setuptools import setup, find_packages


def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()

long_description = (
    "This is a mkdocs plugin that could enable the mermaid graph in the markdown file."
    "Please follow the instruction in reame to enable this plugin"
)

setup(
    name='mkdocs-mermaid-plugin',
    version='0.1.1',
    description='A MkDocs plugin that support mermaid graph in markdown file',
    long_description=long_description,
    keywords='mkdocs python markdown mermaid',
    url='https://github.com/pugong/mkdocs-mermaid-plugin',
    author='pugong',
    author_email='pugong.liu@gmail.com',
    license='MIT',
    python_requires='>=2.7',
    install_requires=[
        'mkdocs>=0.17'
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
            'markdownmermaid = markdownmermaid.plugin:MarkdownMermaidPlugin'
        ]
    }
)
