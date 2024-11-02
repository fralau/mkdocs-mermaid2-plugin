from setuptools import setup, find_packages


VERSION = '1.2.0'

# required if you want to run tests
# pip install 'mkdocs-mermaid2-plugin[test]'
TEST_REQUIRE = ['mkdocs-material', 'mkdocs-macros-test', 'requests-html',
                'packaging']


def readme():
    """print long description"""
    with open('README.md') as f:
        return f.read()


LONG_DESCRIPTION = (
    "An Mkdocs plugin that renders Mermaid graphs in the markdown file. "
    "To install, please follow instructions in the README file."
)

setup(
    name='mkdocs-mermaid2-plugin',
    version=VERSION,
    description='A MkDocs plugin for including mermaid graphs in markdown sources',
    long_description=LONG_DESCRIPTION,
    keywords='mkdocs python markdown mermaid',
    url='https://github.com/fralau/mkdocs-mermaid2-plugin',
    author='Fralau',
    author_email='fralau@bluewin.ch',
    license='MIT',
    python_requires='>=3.6',
    install_requires=[
        'setuptools>=18.5',
        'beautifulsoup4>=4.6.3',
        'mkdocs>=1.0.4',
        'jsbeautifier',
        'requests',
        'pymdown-extensions >= 8.0'
    ],
    extras_require={
        'test': TEST_REQUIRE,
    },
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
