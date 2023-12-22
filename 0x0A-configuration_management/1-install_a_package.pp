# install flask and required packages

#Install python 3.8.10
package { 'python3.8':
  ensure => '3.8.10',
  }

#install pip3
package { 'python3-pip':
  ensure => present,
  }

#install flask
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
  require  => Package['python3-pip']
}

#install Werkzeug 2.1.1
package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip',
  require  => Package['python3-pip'],
  }
