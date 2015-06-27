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
        self.COMMAND = 'add-apt-repository {} -y'.format(repo)

