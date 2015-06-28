# pylint: disable=C0103,R0903,W0232,C1001,C0111
"""
messages for npmanager
"""

class FATAL:
    NOT_ROOT = 'Important: this script must be run as root.'
    ALREADY_INSTALLED = ('Important: it seems there is already npmanager installed, '
                         'if not, delete /etc/npmanager.conf and try again.')

class WARN:
    FOR_DEBIAN = 'Warning: this script was made for use on debian-based linux.'

class INFO:
    INSTALL_PYAPT = ('Info: the command "add-apt-repository" does not exist on your server.\n'
                     '      this installation will install it on your system.')
