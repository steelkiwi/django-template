
VAGRANTFILE_API_VERSION = "2"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

    config.vm.box = "ubuntu/trusty64"

    config.vm.network :forwarded_port, guest: 8000, host: 8000

    # Required for NFS to work, pick any local IP
     config.vm.network :private_network, ip: '192.168.80.50'
    # Use NFS for shared folders for better performance
     config.vm.synced_folder '.', '/vagrant', nfs: true

    # config.vm.provision :shell, :path => "provision.sh"
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "ansible/vagrant.yml"
        ansible.verbose = "v"
    end

    config.vm.provider "virtualbox" do |v|
      host = RbConfig::CONFIG['host_os']

      # Give VM 1/4 system memory & access to all cpu cores on the host
      if host =~ /darwin/
        cpus = `sysctl -n hw.ncpu`.to_i
        # sysctl returns Bytes and we need to convert to MB
        mem = `sysctl -n hw.memsize`.to_i / 1024 / 1024 / 4
      elsif host =~ /linux/
        cpus = `nproc`.to_i
        # meminfo shows KB and we need to convert to MB
        mem = `grep 'MemTotal' /proc/meminfo | sed -e 's/MemTotal://' -e 's/ kB//'`.to_i / 1024 / 4
      else # sorry Windows folks, I can't help you
        cpus = 2
        mem = 1024
      end

      v.customize ["modifyvm", :id, "--memory", mem]
      v.customize ["modifyvm", :id, "--cpus", cpus]
    end
end
