import os
import shutil

from _npmanager.classes import Package
from _npmanager.constants import PY3

class PHPPackage(Package):
    COMMAND = ''
    SELECT = {
        'title': 'Choose the version of PHP',
        'subtitle': 'WARNING: Some PHP applications may not be supported by the latest version of PHP.',
        'options': [
            {'title': 'PHP 5.6 (by ondrej)', 'repo': 'ppa:ondrej/php5-5.6'},
            {'title': 'PHP 5.5 (by ondrej)', 'repo': 'ppa:ondrej/php5'}
        ]
    }

    def __init__(self):
        super(PHPPackage, self).__init__()
        self.basepath = os.path.dirname(os.path.abspath(__file__))

    def select(self):
        val = super(PHPPackage, self).select()
        repo = self.SELECT.get('options')[val].get('repo')
        self.COMMAND = 'add-apt-repository {} -y;'.format(repo)
        self.COMMAND += ('apt-get update > /dev/null;'
                         'apt-get install build-essential gcc g++ -y;'
                         'apt-get install libcurl3-openssl-dev -y;'
                         'apt-get install libpcre3 libpcre3-dev -y;'
                         'apt-get install sqlite sqlite3 -y;'
                         'apt-get install php5-common php5-cgi php5-cli php5-fpm php5-gd -y;'
                         'apt-get install php5-mcrypt php5-tidy php5-curl php5-xdebug php5-sqlite -y;'
                         'apt-get install php5-intl php5-dev -y;'
                         'apt-get install php-pear -y;'
                         'apt-get purge apache2 libapache2-mod-php5 -y;'
                         'apt-get install php5-apcu -y;'
                         'apt-get install php-apc -y;'
                         'rm -rf /etc/nginx/sites-available/;'
                         'rm -rf /etc/nginx/sites-enabled/;'
                         'mkdir /etc/nginx/conf.d')

    def line_receiver(self, line):
        if '] :' in line or '] ?' in line:
            self.write('\n')

    def execute(self):
        super(PHPPackage, self).execute()
        nginx = '/etc/nginx/nginx.conf'
        nginx_php = '/etc/nginx/php'
        nginx_local = '/etc/nginx/conf.d/localhost'
        shutil.copy(os.path.join(self.basepath, 'confs', 'nginx.conf'), nginx)
        shutil.copy(os.path.join(self.basepath, 'confs', 'php.conf'), nginx_php)
        shutil.copy(os.path.join(self.basepath, 'confs', 'localhost.conf'), nginx_local)
        try:
            if PY3:
                os.chmod(nginx, 0o644)
                os.chmod(nginx_php, 0o644)
                os.chmod(nginx_local, 0o644)
            else:
                os.chmod(nginx, 436)  # 436 means 644
                os.chmod(nginx_php, 436)
                os.chmod(nginx_local, 436)
        except:
            pass
