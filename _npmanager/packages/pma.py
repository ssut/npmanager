from _npmanager.classes import Package

class PmaPackage(Package):
    COMMAND = ('apt-get install curl unzip -y > /dev/null;'
               'releases=`curl -s -L https://github.com/phpmyadmin/phpmyadmin/releases/latest`;'
               'echo "$releases" | egrep -o "/phpmyadmin/phpmyadmin/archive/RELEASE_(.+)\.zip" | '
               'wget --base="http://github.com" -i - -O /var/www/html/pma.zip;'
               'unzip -q -o /var/www/html/pma.zip -d /var/www/html/;'
               'mv /var/www/html/php* /var/www/html/phpmyadmin;'
               'chmod -R 755 /var/www/html/phpmyadmin;'
               'rm /var/www/html/pma.zip;'
               'mv /var/www/html/phpmyadmin/config.sample.inc.php /var/www/html/phpmyadmin/config.inc.php;'
               "sed -i \"s/AllowNoPassword\'] \= false/AllowNoPassowrd\'] \= true/g\" /var/www/html/phpmyadmin/config.inc.php")
    SELECT = None

    def line_receiver(self, line):
        pass

    def execute(self):
        super(PmaPackage, self).execute()
        