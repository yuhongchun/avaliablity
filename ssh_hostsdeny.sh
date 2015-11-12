#!/bin/bash
#hostdeny.sh version 2.0 
#written by yuhongchun
awk '{for(i=1;i<=NF;i++){if($i ~ /rhost/)print substr($i,7)}}' /var/log/secure | sort | uniq    -c > /root/black.txt
DEFINE="100"
cat     /root/black.txt |    while read LINE
do
               NUM=`echo $LINE |awk '{print $1}'`
               host=`echo $LINE    |awk '{print $2}'`
               if [ $NUM -gt $DEFINE ];
               then
                grep $host    /etc/hosts.deny > /dev/null
                   if [ $? -gt 0 ];
                   then
                   echo "sshd:$host"     >> /etc/hosts.deny
                   echo "vsftpd:$host" >> /etc/hosts.deny
                   fi
               fi
done