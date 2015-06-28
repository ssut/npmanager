import os
import sys
from setuptools import find_packages, setup

def install():
    version = __import__('_npmanager').__version__
    setup(
        name='npmanager',
        version=version,
        url='https://github.com/ssut/npmanager',
        author='SuHun Han (ssut)',
        author_email='ssut@ssut.me',
        description=('The super easy way to install and manage'
                     'NGINX, PHP and MariaDB'),
        license='MIT License',
        packages=find_packages(),
        scripts=['npmanager'],
        classifiers=[
            'Development Status :: 5 - Production/Stable',
            'Intended Audience :: Developers',
            'Intended Audience :: System Administrators',
            'Intended Audience :: Manufacturing',
            'Intended Audience :: Information Technology',
            'License :: OSI Approved :: MIT License',
            'Operating System :: POSIX :: Linux',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.3',
            'Programming Language :: Python :: 3.4',
            'Environment :: Console',
            'Environment :: Console :: Curses',
            'Topic :: System :: System Shells',
            'Topic :: System :: Systems Administration',
        ],
        include_package_data=True
    )

if __name__ == '__main__':
    install()
