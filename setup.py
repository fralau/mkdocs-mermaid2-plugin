import os
from setuptools import setup, find_packages


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='mkdocs-mermaid-plugin',
    version='0.0.2',
    description='A MkDocs plugin that support mermaid graph',
    long_description=read('README.md'),
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
