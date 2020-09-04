"""
Utilities for mermaid2 module
"""
import os
import requests
from termcolor import colored

MERMAID_LABEL = colored("[MERMAID]", 'green') # plugin's signature label
def info(*args, **kwargs) -> str:
    "Write information on the console, preceded by the signature label"
    print(MERMAID_LABEL, *args, **kwargs)


def libname(lib:str) -> str:
    "Get the library name from a path"
    basename = os.path.basename(lib)
    # remove extension three times, e.g. mermaid.min.js => mermaid
    t = basename
    for _ in range(3):
        t = os.path.splitext(t)[0]
    return t

def url_exists(url:str) -> bool:
    "Checks that a url exists"
    if url.startswith('http'):
        request = requests.get(url)
        return request.status_code == 200
    else:
        os.path.exists(url)
