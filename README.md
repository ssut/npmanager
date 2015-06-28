# npmanager

[![PyPI version](https://badge.fury.io/py/npmanager.svg)](http://badge.fury.io/py/npmanager)

![](http://i.imgur.com/QkllAZ1.png)

**npmanager** is the super easy way to install and manage NGINX, PHP and MariaDB on your debian-based linux server.

## Prerequisite for installation

* You need a debian-based linux distribution – I recommend you to get **Ubuntu LTS** releases.
* This requires up to 1GB of data, and up to 500MB of space for its operation.
* Python is needed – You don't need to install python at all to get started on Ubuntu.

**npmanager does not support the [end-of-life Ubuntu releases](http://www.ubuntu.com/info/release-end-of-life).**

## What's inside?

* NGINX (stable or dev)
    * includes simple performance tweak by configuration
* PHP (5.5 or 5.6)
    * php5-cli
    * php5-fpm
    * php5-gd
    * php5-mcrypt
    * php5-tidy
    * php5-curl
    * php5-xdebug
    * php5-sqlite
    * php5-intl
    * php5-mysql
    * php5-apc (for performance improvements)
* MariaDB (stable only)


## Installation

This installation guide is written as if **Ubuntu 14.04 LTS** was just installed.

### Video guide

[![YouTube Guide to install npmanager](http://img.youtube.com/vi/JgUC9mS2cRk/0.jpg)](http://www.youtube.com/watch?v=JgUC9mS2cRk)

### Text guide

Tip: The dollar sign(`$`) just means you are a normal user. I would recommend login as a normal user to work, and use sudo command instead of login as root(`#`).

```bash
$ sudo apt-get install python-pip -y
$ sudo pip install npmanager
$ sudo npmanager install
If you want to continue press RETURN(Enter) key or CTRL + C to exit:  # press enter
# select nginx, php and mariadb version you want to install and take a coffee break :)
```

### After installation

You have to know a few things, as follows:

#### Go ahead

 Go to the index page then check *"Here are the details you need to know to go ahead with secure"* section.

- As explaned in the index page, you **must** set your MariaDB password FIRST!
- Also, configuration files are located in the following directories:
    - NGINX: `/etc/nginx`
    - NGINX Web: `/etc/nginx/conf.d` (check the default config in the file named `localhost`)
    - PHP: `/etc/php5/fpm`
    - MariaDB: `/etc/mysql`
- The default web directory is `/var/www/html`, and the owner is set to your username as installation default.

#### Start, Stop, Reload, Restart, and see the Status of the daemon

```bash
# Start
$ sudo npmanager start [daemon]
# Stop
$ sudo npmanager stop [daemon]
# Reload 
$ sudo npmanager reload [daemon]
# Restart
$ sudo npmanager restart [daemon]
# Status
$ sudo npmanager status [daemon]
```

## To upgrade when an update becomes available

```bash
$ sudo pip install npmanager --upgrade
```


## Contributing

Fork this project then create a feature branch and send me a pull request.

## Support

Support is available via the [issue tracker](https://github.com/ssut/npmanager/issues) in the Github project page or via Telegram [@ssssut](https://telegram.me/ssssut).


## License

**npmanager** is released under the [MIT License](http //www.opensource.org/licenses/mit-license.php).

```
The MIT License (MIT)

Copyright (c) 2015 SuHun Han

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
