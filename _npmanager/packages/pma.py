from _npmanager.classes import Package

class PmaPackage(Package):
    COMMAND = ('apt-get install curl unzip -y > /dev/null;'
               'releases=`curl -s -L https://github.com/phpmyadmin/phpmyadmin/releases/latest`;'
               'echo "$releases" | egrep -o "/phpmyadmin/phpmyadmin/archive/RELEASE_(.+)\.zip" | '
               'wget --base="http://github.com" -i - -O /var/www/html/pma.zip;'
               'unzip -o /var/www/html/pma.zip -d /var/www/html/;'
               'mv /var/www/html/php* /var/www/html/phpmyadmin;'
               'chmod -R 755 /var/www/html/phpmyadmin')
    SELECT = None

    def line_receiver(self, line):
        pass
