#!/bin/bash
iptables -F
iptables -X
iptables -Z

#FTP需要ip_nat_ftp模块
modprobe ip_conntrack_ftp
modprobe ip_nat_ftp

#这里为了实验效果，OUTPUT默认策略也定义为DROP
iptables -P INPUT DROP
iptables -P OUTPUT DROP
iptables -P FORWARD ACCEPT

#打开回环口，免得不必要的麻烦
iptables -A INPUT -i lo  -j ACCEPT
iptables -A OUTPUT -o lo -j ACCEPT

#22和21端口都打开，确认这二个端口的数据都会被顺利放行,但请大家注意的是，这里并没有开放20端口
iptables -A INPUT -p tcp --dport 22 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 22 -j ACCEPT
iptables -A INPUT -p tcp --dport 21 -j ACCEPT
iptables -A OUTPUT -p tcp --sport 21 -j ACCEPT

#与FTP-DATA有关的RELATED包都会被放行，用状态来约束数据包比用端口智能些
iptables -A INPUT -p tcp  -m state --state ESTABLISHED,RELATED  -j ACCEPT
iptables -A OUTPUT -p tcp -m state --state ESTABLISHED,RELATED  -j ACCEPT
