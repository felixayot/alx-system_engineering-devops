# Installs and configures an Nginx server instead of Bash. 
#  Also creates a custom HTTP header response, `X-Served-By`.

exec { 'get updates':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => 'installed',
  require => Exec['get updates'],
}

file {'/etc/nginx/html/index.html':
  content => 'Hello World!',
}

exec { 'configure_nginx':
  command  => 'echo "server { listen 80; server_name localhost; location / { root /etc/nginx/html; } }"',
  provider => 'shell',
  require  => Package['nginx'],
}

file_line {'create_Header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $HOSTNAME;',
    require => Package['nginx'],
}

exec {'redirect_me':
  command  => 'sed -i "24i	\rewrite ^/redirect_me http://google.com/doodles/ permanent;" /etc/nginx/sites-available/default',
  provider => 'shell',
  require  => [Package['nginx'], Exec['configure_nginx']],
}

service {'nginx':
  ensure  => 'running',
  require => Package['nginx'],
}
