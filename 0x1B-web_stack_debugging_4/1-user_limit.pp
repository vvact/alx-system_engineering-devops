# increase user limit;

exec { 'sed hardlimit':
    command => 'sed -i "s/5/3000/" /etc/security/limits.conf',
    path    => 'usr/local/bin/:/bin/'
}

exec { 'sed softlimit':
    command => 'sed -i "s/4/1000/" /etc/security/limits.conf',
    path    => 'usr/local/bin/:/bin/'
}
