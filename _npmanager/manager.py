"""
npmanager manager module
"""
from __future__ import print_function
import importlib
import inspect
import os
import sys
import time

from _npmanager.utils import commandutils as cmdutils
from _npmanager import messages

class Manager:
    def __init__(self, conf='/etc/npmanager.conf'):
        self.conf = conf
        self.check_env()
        self.packages = {}
        self._load_packages()

    def _exit(self, stat):
        sys.exit(stat)

    def _load_packages(self):
        root = '_npmanager.packages'
        packages = importlib.import_module(root)
        packages = inspect.getmembers(packages, inspect.ismodule)
        for name, package in packages:
            _, cls = inspect.getmembers(package, \
                lambda member: ('__module__' in dir(member) and root in member.__module__))[0]
            self.packages[name] = cls()

    def check_env(self):
        # check for root user
        euid = os.geteuid()
        # check for package manager (apt)
        aptitude = cmdutils.which('/usr/bin/apt-get') and \
                   cmdutils.which('/usr/bin/aptitude')
        if euid != 0:
            print(messages.FATAL.NOT_ROOT)
            self._exit(1)
        if not aptitude:
            print(messages.WARN.FOR_DEBIAN)

    def install(self):
        if os.path.exists('/etc/npmanager.conf'):
            print(messages.FATAL.ALREADY_INSTALLED)
            sys.exit(0)

        self.packages['nginx'].select()
        self.packages['php'].select()
        self.packages['mariadb'].select()

        time.sleep(1)
        pyapt = cmdutils.which('/usr/bin/add-apt-repository')
        if not pyapt:
            print(messages.INFO.INSTALL_PYAPT)
            self.packages.get('pyapt').execute()

        self.packages.get('nginx').execute()
        self.packages.get('php').execute()
        self.packages.get('mariadb').execute()
        self.packages.get('pma').execute()

        with open('/etc/npmanager.conf', 'w') as fd:
            fd.write('\n')

    def start(self, daemon):
        self.packages.get(daemon).start()

    def stop(self, daemon):
        self.packages.get(daemon).stop()

    def reload(self, daemon):
        self.packages.get(daemon).reload()

    def restart(self, daemon):
        self.packages.get(daemon).restart()

    def status(self, daemon):
        self.packages.get(daemon).status()
