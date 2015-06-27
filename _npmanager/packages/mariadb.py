from operator import itemgetter

from _npmanager.classes import Package
from _npmanager.utils.commandutils import lsb_release
from _npmanager.utils import networkutils as netutils

class MariadbPackage(Package):
    COMMAND = ''
    SELECT = {
        'title': 'Choose the version of MariaDB',
        'subtitle': 'INFO: Currently, the beta releases of MariaDB is not provided by repos.',
        'options': [
            {'title': 'MariaDB 10.x stable', 'repo': '10.0'},
            {'title': 'MariaDB 10.x stable', 'repo': '10.0'}
        ]
    }
    REPOS = {
        '10.0': [
            # KAIST, South Korea
            'http://ftp.kaist.ac.kr/mariadb/repo/{version}/{os}/',
            # Yamagata Univ., Japan
            'http://ftp.yz.yamagata-u.ac.jp/pub/dbms/mariadb/repo/{version}/{os}/',
            # DigitalOcean, Singapore
            'http://sgp1.mirrors.digitalocean.com/mariadb/repo/{version}/{os}/',
            # DigitalOcean, London, UK
            'http://lon1.mirrors.digitalocean.com/mariadb/repo/{version}/{os}/',
            # DigitalOcean, San Francisco, US
            'http://sfo1.mirrors.digitalocean.com/mariadb/repo/{version}/{os}/',
        ]
    }

    def select(self):
        val = super(MariadbPackage, self).select()
        _os, _codename = lsb_release()
        ver = self.SELECT.get('options')[val].get('repo')
        print('INFO: selecting best server based on latency..')
        data = {}
        for repo in self.REPOS[ver]:
            url = repo.format(version=ver, os=_os)
            data[url] = netutils.ping(url)
        server, _ = sorted(data.items(), key=itemgetter(1))[0]
        deb = 'deb {url} {codename} main'.format(url=server, codename=_codename)
        self.COMMAND = ('apt-key adv --recv-keys --keyserver hkp://keyserver.ubuntu.com:80 0xcbcb082a1bb943db;'
                        'add-apt-repository \'{deb}\';'.format(deb=deb))
        self.COMMAND += ('apt-get update > /dev/null;'
                         'DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::="--force-confnew" -q -y install mariadb-server;'
                         'DEBIAN_FRONTEND=noninteractive apt-get -o Dpkg::Options::="--force-confnew" -q -y install mariadb-client;'
                         'apt-get install php5-mysql -y --force-yes')

    def line_receiver(self, line):
        pass

