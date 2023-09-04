# Add a custom HTTP  header with puppet
# custom HTTP  header must be X-Served-By

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
        ensure  => 'installed',
        require => Exec['update system']
}

file {'/var/www/html/index.html':
        content => 'Hello World!'
}
exec {'redirect_me':
        command  => 'sed -i "24i\        rewrite ^/redirect_me https://youtube/ permanent;" /etc/nginx/sites-available/default',
        provider => 'shell'
}
exec {'HTTP header':
        command  => 'sed -i "25i\           add_header X-Served-by \$hostname;" /etc/nginx/sites-available/default',
        provider => 'shell'
}

service { 'nginx':
        ensure  => running,
        require => Package['nginx']
}
