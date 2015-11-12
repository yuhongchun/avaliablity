#!/usr/bin/python2.6
from fabric.api import *

env.user = 'ec2-user'
#env.key_filename = '/home/ec2-user/.ssh/id_rsa'
env.key_filename = '/home/ec2-user/.ssh/id_rsa'
env.reject_unknown_hosts = False

#hosts = ['pixel',]
hosts = ['budget', 'adserver', 'bidder1', 'bidder2', 'dns', 'redis1', 'redis2', 'redis3']

def put_ec2_key():
    with settings(warn_only=False):
        put("/home/ec2-user/bilin-master.pub","/home/ec2-user/bilin-master.pub")
        sudo("\cp /home/ec2-user/bilin-master.pub /home/ec2-user/.ssh/authorized_keys")
        sudo("chmod 600 /home/ec2-user/.ssh/authorized_keys")


def put_bilin_key():
    with settings(warn_only=False):
        put("/home/ec2-user/bilin-operation.pub","/home/ec2-user/bilin-operation.pub")
        sudo("\cp /home/ec2-user/bilin-operation.pub /home/bilin/.ssh/authorized_keys")
        sudo("chown bilin:bilin /home/bilin/.ssh/authorized_keys")
        sudo("chmod 600 /home/bilin/.ssh/authorized_keys")


def put_readonly_key():
    with settings(warn_only=False):
        put("/home/ec2-user/bilin-readonly.pub","/home/ec2-user/bilin-readonly.pub")
        sudo("\cp /home/ec2-user/bilin-readonly.pub /home/readonly/.ssh/authorized_keys")
        sudo("chown readonly:readonly /home/readonly/.ssh/authorized_keys")
        sudo("chmod 600 /home/readonly/.ssh/authorized_keys")

for host in hosts:
    env.host_string = host
    put_ec2_key()
    put_bilin_key()
    put_readonly_key()