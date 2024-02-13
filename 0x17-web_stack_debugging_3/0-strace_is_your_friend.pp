#Identify issue that causes 500 error
exec { 'fix wordpress':
  command  => 'sudo sed -i "s/.phpp/.php/" /var/www/html/wp-settings.php',
  provider => shell,
}
