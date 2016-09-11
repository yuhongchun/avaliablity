#/bin/bash
#此脚本仅是CentOS 5.x版本(64位)的最小优化脚本，如果需要CentOS6.x系统优化脚本的同学可移步至automation项目
#增加epel源
cd /usr/local/src
wget http://mirrors.ustc.edu.cn/fedora/epel/5/x86_64/epel-release-5-4.noarch.rpm
rpm -ivh epel-release-5-4.noarch.rpm
#清除yum缓存
yum clean all

#安装简单的gcc编译基础工具以及sysstat软件
yum -y install gcc gcc-c++ vim-enhanced unzip unrar sysstat

#配置ntp自动对时
yum -y install ntp
echo "01 01 * * * /usr/sbin/ntpdate ntp.api.bz  >> /dev/null 2>&1" >> /etc/crontab
ntpdate ntp.api.bz
service crond restart

#配置CentOS 5.x的文件最大打开数，注意与CentOS 6.x的区别
ulimit -SHn 65535
echo "ulimit -SHn 65535" >> /etc/rc.local
cat >> /etc/security/limits.conf << EOF
*           soft   nofile       60000
*           hard   nofile       65535
EOF

#系统内核的基础调优，注意如果是高并发环境则需要调整的地方还有很多
cat >> /etc/sysctl.conf << EOF
net.ipv4.tcp_syncookies = 1
net.ipv4.tcp_syn_retries = 1
net.ipv4.tcp_tw_recycle = 1
net.ipv4.tcp_tw_reuse = 1
net.ipv4.tcp_fin_timeout = 1
net.ipv4.tcp_keepalive_time = 1200
net.ipv4.ip_local_port_range = 1024 65535
EOF
/sbin/sysctl -p

#禁用control-alt-delete组合键
sed -i 's@ca::ctrlaltdel:/sbin/shutdown -t3 -r now@#ca::ctrlaltdel:/sbin/shutdown -t3 -r now@' /etc/inittab

#关闭SElinux
sed -i 's@SELINUX=enforcing@SELINUX=disabled@' /etc/selinux/config

#SSH的简单优化
sed -i -e '74 s/^/#/' -i -e '76 s/^/#/' /etc/ssh/sshd_config
sed -i 's@#UseDNS yes@UseDNS no@' /etc/ssh/sshd_config
service sshd restart

#禁止ipv6和ip6tables防火墙
echo "alias net-pf-10 off" >> /etc/modprobe.conf
echo "alias ipv6 off" >> /etc/modprobe.conf
echo "install ipv6 /bin/true" >> /etc/modprobe.conf
echo "IPV6INIT=no" >> /etc/sysconfig/network
sed -i 's@NETWORKING_IPV6=yes@NETWORKING_IPV6=no@'  /etc/sysconfig/network
chkconfig ip6tables off

#vim简单优化
echo "syntax on" >> /root/.vimrc
echo "set nohlsearch" >> /root/.vimrc

#关闭基础的服务，以节约系统资源
chkconfig bluetooth off
chkconfig sendmail off
chkconfig kudzu off
chkconfig nfslock off
chkconfig portmap off
chkconfig iptables off
chkconfig autofs off
chkconfig yum-updatesd off

#重启系统以使上面配置生效，生产环境下注意
reboot
