# Replace wrong `phpp` extensions with `php` in the `wp-settings.php` file to fix the WordPress website.

exec { 'subtitute-filext':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
