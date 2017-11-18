#!/bin/bash
#每5分钟运行一次脚本

CE_HOME='/data/ContentEngine'
LOG_PATH='/data/logs'

# 控制爬虫数量为8
MAX_SPIDER_COUNT=8

# current count of spider
count=`ps -ef | grep -v grep | grep run.py | wc -l`
# 下面的逻辑是控制run.py进程数量始终为8，充分挖掘机器的性能，并且为了防止形成死循环，这里没有用while语句。
try_time=0
cd $CE_HOME
while [ $count -lt $MAX_SPIDER_COUNT -a $try_time -lt $MAX_SPIDER_COUNT ];do
	let try_time+=1
	python run.py >> ${LOG_PATH}/spider.log 2>&1 &
	count=`ps -ef | grep -v grep | grep run.py | wc -l`
done