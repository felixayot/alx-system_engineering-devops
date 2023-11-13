# Increases the number of HTTP requests(traffic) an Nginx server can handle.

# Step 1: Raise the ULIMIT of the worker processes file to 10000
exec { 'fix--for-nginx':
  command => 'sed -i "s/15/10000/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

# Step 2: Restart Nginx
exec { 'restart-nginx':
  command => 'nginx restart',
  path    => '/etc/init.d/'
}
