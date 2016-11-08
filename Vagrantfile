Vagrant.configure("2") do |config|
  config.vm.define  "server" do |vb|
    config.vm.provider "virtualbox" do |v|
      v.memory = 512
      v.cpus = 4
    end
    vb.vm.host_name = "server"
    vb.vm.network :private_network, ip: "10.0.2.16"
    vb.vm.box = "centos63"
  end


  config.vm.define  "vagrant1" do |vb|
    config.vm.provider "virtualbox" do |v|
      v.memory = 512
      v.cpus = 4
    end
    vb.vm.host_name = "vagrant1"
    vb.vm.network :private_network, ip: "10.0.2.17"
    vb.vm.box = "centos63"
  end

  config.vm.define  "vagrant2" do |vb|
    config.vm.provider "virtualbox" do |v|
      v.memory = 512
      v.cpus = 4
    end
    vb.vm.host_name = "vagrant2"
    vb.vm.network :private_network, ip: "10.0.2.18"
    vb.vm.box = "centos63"
  end
end
