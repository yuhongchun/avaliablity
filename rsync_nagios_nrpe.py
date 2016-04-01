#!/usr/bin/python2.6
#Fabric template File
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import *

user = 'ec2-user'
hosts = ['bidder1','bidder2','bidder3','bidder4','bidder5']
# hosts = ['bidder1',]

@task
def put_task():
    print yellow("Put Local File to remote")
    with settings(warn_only=True):
        put("/home/ec2-user/check_cpu_utili.sh","/home/ec2-user/check_cpu_utili.sh")
        sudo("cp /home/ec2-user/check_cpu_utili.sh /usr/local/nagios/libexec")
        sudo("chown nagios:nagios /usr/local/nagios/libexec/check_cpu_utili.sh")
        sudo("chmod +x /usr/local/nagios/libexec/check_cpu_utili")
        sudo("kill `ps aux | grep nrpe | head -n1 | awk '{print $2}' `")
        sudo("/usr/local/nagios/bin/nrpe -c /usr/local/nagios/etc/nrpe.cfg -d")
        print green("Put File success and restart nagios nrpe service!")
#@task
#def run_task():
#    with cd("/home/ec2-user/"):
#        run("sh netstat.sh")

for host in hosts:
    env.host_string = host
    put_task()
#put_task()
