#!/usr/bin/python2.6
#Fabric template File
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *

user = 'ec2-user'
hosts = ['bidder1','bidder2','bidder3','bidder4','bidder5','bidder6','bidder7','bidder8']


@task
def put_task():
    print yellow("Put Local File to remote")
    with settings(warn_only=True):
        put("/home/ec2-user/check_ip_connects.sh","/home/ec2-user/check_ip_connects.sh")
        sudo("cp /home/ec2-user/check_ip_connects.sh /usr/local/nagios/libexec/check_ip_connects.sh")
        sudo("chown nagios:nagios /usr/local/nagios/libexec/check_ip_connects.sh")
	sudo("chmod +x /usr/local/nagios/libexec/check_ip_connects.sh")
        sudo("sed '/command\[check_ip_connects\]/d' /usr/local/nagios/etc/nrpe.cfg")
        sudo("sed '/command\[check_cpu_utili\]/a\command\[check_ip_connects]=/usr/loca/nagios/libexec/check_ip_connects.sh' /usr/local/ngios/etc/nrpe.cfg")
        sudo("kill -9 `ps aux | grep nrpe | head -n1 | awk '{print $2}' `")
        sudo("/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d")
        print green("Put File success and restart nagios nrpe service!")

for host in hosts:
    env.host_string = host
    put_task()
