"""
Package is simply a directory that contains Python modules.

In older version of python you need to create __init__.py under the directory in order to mark it as a package.

In newer versions, any directory that contains Python scripts is able to be considered as a Package.

__init__.py will run some code to initialize the package the first time the package is imported. (Package setup operations)
"""

# from package import math(module), string(module)
from utils import math, string

print(string.capitalize("hi"))