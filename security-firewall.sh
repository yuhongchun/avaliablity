#!/bin/bash
# Setup Linux System Security

#此脚本为简单的web主机防护脚本，只开放了80和22端口，另外也注意将limit值配置高一些，免得将正常流量也挡住了。122.70.x.x为白名单IP。

iptables -F
iptables -F -t nat
iptables -X
iptables -P INPUT DROP
iptables -P OUTPUT ACCEPT
iptables -P FORWARD ACCEPT
#load connection-tracking modules
modprobe iptable_nat
modprobe ip_conntrack_ftp
modprobe ip_nat_ftp
iptables -A INPUT -f -m limit --limit 100/sec --limit-burst 100 -j ACCEPT
iptables -A INPUT -p icmp --icmp-type echo-request -m limit --limit 1/s --limit-burst 10 -j ACCEPT
iptables -A INPUT -p tcp -m tcp --tcp-flags SYN,RST,ACK SYN -m limit --limit 20/sec --limit-burst 200 -j ACCEPT
iptables -A INPUT -s 122.70.x.x -j ACCEPT
iptables -A INPUT -s 122.70.x.x -j ACCEPT
iptables -A INPUT -i lo -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT
iptables -A INPUT -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -A INPUT -p tcp -m multiport --dport 80,22 -j ACCEPT
