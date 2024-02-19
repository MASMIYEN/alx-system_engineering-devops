# update soft limit
exec { 'update_soft_limit':
  command  => "sed -i 's/^holberton soft nofile.*/holberton soft nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}

exec { 'update_hard_limit':
  command  => "sed -i 's/^holberton hard nofile.*/holberton hard nofile 8192/' /etc/security/limits.conf",
  provider => 'shell',
}
