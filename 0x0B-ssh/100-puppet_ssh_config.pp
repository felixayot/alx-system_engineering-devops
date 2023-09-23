# Sets up your client SSH configuration file so that you can connect
# to a server without typing a password.
file_line { 'ssh_config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/school',
}
file_line { 'ssh_config':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => 'PasswordAuthentication no',
}
