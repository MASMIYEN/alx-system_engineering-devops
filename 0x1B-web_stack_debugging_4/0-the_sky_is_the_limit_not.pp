# the sky has no limit
exec {'update ulimit':
  command  => "sed -i 's/^ULIMIT=.*/ULIMIT=\"-n 15000\"/' /etc/default/nginx",
  provider => 'shell',
}
-> exec {'restart nginx':
  command  => 'service nginx restart',
  provider => 'shell',
}

