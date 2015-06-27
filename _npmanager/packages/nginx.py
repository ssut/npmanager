from _npmanager.classes import Package


class NginxPackage(Package):
    COMMAND = ''
    SELECT = {
        'title': 'Choose the version of NGINX',
        'subtitle': 'WARNING: Do not use development releases on production systems!',
        'options': [
            {'title': 'NGINX Stable', 'repo': 'ppa:nginx/stable'},
            {'title': 'NGINX Development', 'repo': 'ppa:nginx/development'}
        ]
    }

    def select(self):
        val = super(NginxPackage, self).select()
        repo = self.SELECT.get('options')[val].get('repo')
        self.COMMAND = 'add-apt-repository {} -y;'.format(repo)
        self.COMMAND += ('apt-get update > /dev/null;'
                         'apt-get install nginx -y;'
                         'mkdir -p /var/www/html;'
                         'chmod 755 /var/www/html')


    def line_receiver(self, line):
        pass

