# Add a custom HTTP  header with puppet
# custom HTTP  header must be X-Served-By

exec { 'apt-update':
        command => '/usr/bin/apt-get -y update',
        path    => ['/usr/bin', '/bin'],
}

package { 'nginx':
        ensure  => installed,
}

file {'/var/www/html/index.html':
        content => 'Hello World!',
}

file_line { 'add custom header':
  ensure => present,
  path   => '/etc/nginx/sites-available/default',
  line   => "\tadd_header X-Served-By ${hostname};",
  after  => 'server_name _;',
}

service { 'nginx':
  ensure => running,
}
