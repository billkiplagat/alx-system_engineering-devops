#configure ssh config
file { '/etc/ssh':
  ensure => directory,
  owner  => 'root',
  group  => 'root',
  mode   => '0755',
}
file { '/etc/ssh/config':
  owner => 'root',
  group => 'root',
  mode  => '0644',
}
file_line { 'Turn off passwd auth':
  path => '/etc/ssh/config',
  line => 'PasswordAuthentication no'
}

file_line { 'Declare identity file':
  path => '/etc/ssh/config',
  line => 'IdentityFile ~/.ssh/school'

}
