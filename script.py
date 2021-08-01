#!/usr/bin/python3

# 2020
# The SAAS Toolkit was programmed and developed by Us3rn4m3.
# The SAAS Toolkit is published under the MIT Licence.
# The SAAS Toolkit is based on the CLIF-Framework.
# The CLIF-Framework is programmed and developed by Us3rn4m3.
# The CLIF-Framework is published under the MIT Licence.

# This script is a shortcut for everyone who does not want to install Raven-Storm to the bin path.

from importlib import import_module
from sys import path

path.insert(1, "./Raven-Storm/")
main = import_module("Raven-Storm.main")

main.run()
