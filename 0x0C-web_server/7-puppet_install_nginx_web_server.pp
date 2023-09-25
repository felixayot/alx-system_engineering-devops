# Installs and configures an Nginx server instead of Bash. 
exec { 'get updates':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['update system']
}

file {'/etc/nginx/html/index.html':
  content => 'Hello World!'
}

exec {'redirect_me':
  command  => 'sed -i "24i\	rewrite ^/redirect_me http://google.com/doodles/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell'
}

service {'nginx':
  ensure  => running,
  require => Package['nginx']
}
