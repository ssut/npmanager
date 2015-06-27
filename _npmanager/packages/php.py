from _npmanager.classes import Package

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
                         'apt-get install php-apc -y;')

    def line_receiver(self, line):
        if '] :' in line or '] ?' in line:
            self.write('\n')
