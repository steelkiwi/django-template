## Date:
02.06.2016

## box name:
- steelkiwi_django_0.0.1.box

## version:
- 0.0.1

## OsType:
- ubuntu/trusty64

## Soft:
- virtualenv - 1.11.4
- postgresql - 9.4
- postgis    - 2.2.2
- redis      - 2:2.8.4-2
- RabbitMQ   - 3.2.4-1
- nodejs     - 4.4.5 (LTS)
- bower      - 1.7.9
- memcached  - 1.4.14
- Python     - 3.5.1

## Actions:
- create user vagrant (superuser) in postgres

* * * 

## Date:
20.06.2016

## box name:
- steelkiwi_django_0.0.2.box

## version:
- 0.0.2

## OsType:
- ubuntu/trusty64

### Added
- Python 2.7.11
- Pip 8.1.2
- Activate venv via .profile (modify .profile)

* * *

## Date:
 08.07.2016

## box name:
- steelkiwi_django_0.0.3.box

## version:
- 0.0.3

## OsType:
- ubuntu/trusty64

### Update
- nodejs - 4.4.7 (LTS)
- Python2 - 2.7.12
- Python3.4 - 3.4.3
- Python3.5 - 3.5.2

### Added
- pip3 - 8.1.1
- mysql-server - 5.5.49
- nginx - 1.4.6
- apache - 2.4.10
- supervizor - 3.0b2-1

## Actions:
- update-rc.d (remove apache2, nginx, mysql, postgres, redis, supervisor, rabbitmq)
- alias pip=/usr/local/bin/pip
- alias python=/usr/local/bin/python


* * *

