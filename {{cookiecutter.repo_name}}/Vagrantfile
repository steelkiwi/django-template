# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
	config.vm.define "develop" do |develop|
		develop.vm.box = "develop"
		develop.vm.box_url = "http://vagrant.steel.kiwi/vagrant/develop/"

	####Network
		develop.vm.network :forwarded_port, guest: 8000, host: 8000
		develop.vm.network :private_network, ip: '192.168.80.50'
		develop.vm.synced_folder ".", "/vagrant", type: "nfs", mount_options: ['nolock,vers=3,udp,noatime,actimeo=1']
		#develop.vm.synced_folder ".", "/vagrant", type: :virtualbox

	####ansible_provision
		develop.vm.provision "ansible_local" do |ansible|
		ansible.verbose = "v"
		ansible.playbook = "ansible/vagrant.yml"
		end

	####system resources
		develop.vm.hostname = "develop"
		  develop.vm.provider "virtualbox" do |v|
		  v.memory = 1024
		  v.cpus = 1
		  end
	end
end
