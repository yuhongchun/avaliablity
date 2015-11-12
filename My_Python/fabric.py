a#!/usr/bin/python2.6
#Fabric template File
from fabric.api import *
from fabric.colors import *
from fabric.context_managers import * 

user = 'ec2-user'
hosts = ['bidder1','bidder2']

@task
def put_task():
    print yellow("Put Local File to remote")
    with settings(warn_only=True):
        put("/home/ec2-user/nginxlua_log.cfg","/home/ec2-user/nginxlua_log.cfg",mode=644)
        sudo("cp /home/ec2-user/nginxlua_log.cfg /usr/local/nagios/etc/nginxlua_log.cfg")
        print green("Put File success!")
#@task
#def run_task():
#    with cd("/home/ec2-user/"):
#        run("sh netstat.sh")

for host in hosts:
    env.host_string = host
    put_task()
#    run_task()