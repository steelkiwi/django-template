 #!/usr/bin/env bash

if [ -e "/etc/vagrant-provisioned" ];
then
    if [ "/vagrant/provision.sh" -ot "/etc/vagrant-provisioned" ];
    then
        echo "Vagrant provisioning already completed. Skipping..."
        exit 0
    else
        echo "Starting Vagrant provisioning process..."
    fi

else
    echo "Starting Vagrant provisioning process..."
fi

# Install core components
/vagrant/sh/core.sh

# Install python
/vagrant/sh/python.sh

# Install postgresql
/vagrant/sh/postgresql.sh

{% if cookiecutter.use_redis == "y" %}
# Install redis
/vagrant/sh/redis.sh
{% endif %}

{% if cookiecutter.use_rabbit == "y" or cookiecutter.use_celery == "y"  %}
# Install rabbit
/vagrant/sh/rabbitMQ.sh
{% endif %}

{% if cookiecutter.use_memcached == "y" %}
# Install memcached
/vagrant/sh/memcached.sh
{% endif %}

# Install bower
/vagrant/sh/bower.sh


touch /etc/vagrant-provisioned

echo "--------------------------------------------------"
echo "Your vagrant instance is running"
