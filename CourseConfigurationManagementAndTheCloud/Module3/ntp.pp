class ntp {
  package { 'ntp':
    ensure => latest,
  } 
  file { '/etc/ntp.conf':
    source => '/home/andro/ntp.conf',
    replace => true,
    require => Package['ntp'],
    notify  => Service['ntp'],
  }
  service { 'ntp':
    enable  => true,
    ensure  => running,
    require => File['/home/andro/ntp.conf'],
  }
}
include ntp
