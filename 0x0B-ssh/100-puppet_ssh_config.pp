#configure ssh config

file_line { 'Turn off passwd auth':
  path => '/etc/ssh/config',
  line => 'PasswordAuthentication no'
}

file_line { 'Declare identity file':
  path => '/etc/ssh/config',
  line => 'IdentityFile ~/.ssh/school'

}
