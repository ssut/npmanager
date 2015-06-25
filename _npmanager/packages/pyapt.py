# pylint disable=C0112
"""

"""
from _npmanager.classes import Package

class PyAptPackage(Package):
    COMMAND = 'apt-get install software-properties-common python-software-properties'

    def install(self):
        self.call()
