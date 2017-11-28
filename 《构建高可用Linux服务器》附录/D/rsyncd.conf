#!/bin/bash
src=/data/html/www/images/
des_ip1=10.0.0.16
des_ip2=10.0.0.17

/usr/bin/inotifywait -mrq --timefmt '%d/%m/%y %H:%M' --format  '%T %w%f' -e modify,delete,create,attrib $src | while read  file
do
    rsync -vzrtopg --delete --progress $src www@$des_ip1::web1_sync --password-file=/etc/rsyncd.password 
    rsync -vzrtopg --delete --progress $src www@$des_ip2::web2_sync --password-file=/etc/rsyncd.password 
    echo "File Synchronization is Complete!"
done
