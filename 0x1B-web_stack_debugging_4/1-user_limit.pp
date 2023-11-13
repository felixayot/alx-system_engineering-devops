# Changes the OS configuration so that it is possible to login with the holberton user and open a file without any error message.

# Step 1: Raise hard file limit for holberton user.
exec { 'change-os-configuration-for-holberton-user-hard-nofile':
  command => 'sed -i "/holberton hard/s/5/500000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}

# Step 2: Raise soft file limit for holberton user.
exec { 'change-os-configuration-for-holberton-user-soft-nofile':
  command => 'sed -i "/holberton soft/s/4/500000/" /etc/security/limits.conf',
  path    => '/usr/local/bin/:/bin/'
}
