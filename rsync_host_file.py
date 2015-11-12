#!/usr/bin/python
from fabric.api import *
from fabric.colors import * 
from fabric.context_managers import * 

user = 'root'
hosts = ['192.168.1.213','192.168.1.214','192.168.1.215']
env.password = 'bilin101'


@task
def put_hosts_files():
   print yellow("rsync local hosts File")
   with settings(warn_only=True):
       put("/etc/hosts","/etc/hosts")
       print green("rsync file sucess!")

for host in hosts:
    env.host_string = host
    put_hosts_files()