# Sets up your client SSH configuration file so that you can connect
# to a server without typing a password.
file { 'ssh_config':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/school',
}
file { '/etc/ssh/ssh_config':
  line     => 'PasswordAuthentication no',
  multiple => true,
}
