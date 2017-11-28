#/bin/bash
DB=pharma
USER=root
PASSWD=root@change

/usr/local/mysql/bin/mysql  -u$USER -p$PASSWD $DB -e "select TABLE_NAME from information_schema.TABLES where TABLE_SCHEMA='"$DB"' and ENGINE='"MyISAM"';" | grep -v "TABLE_NAME" > mysql_table.txt
cat  mysql_table.txt | while read LINE
do
    echo "Starting convert table engine..."
    /usr/local/mysql/bin/mysql -u$USER -p$PASSWD $DB -e "alter table $LINE  engine='"InnoDB"'"
    sleep 1
done
