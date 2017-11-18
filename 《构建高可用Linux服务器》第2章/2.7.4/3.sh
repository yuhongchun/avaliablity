#如果hosts文件不存在，就调用touch命令建立；另外，这里要增加一个逻辑判断，即如果已经有人在发布平台了，第二个运维人员发布的时候，一定要强制退出。
if [ ! -f "$hosts" ]
then
touch "$hosts"
else
    echo "此平台已经有运维小伙伴在发布，请耐心等待！"
exit
fi
#如果出现中止进程的情况，捕捉异常信号，清理临时文件。
trap "echo '程序被中止，开始清理临时文件';rm -rf $hosts;exit" 1 2 3
#进入public_conf目录，通过git pull获取gitlab上最新的相关文件配置
cd /data/conf /public_conf/
git pull origin master:master
#配置文件这里也是通过内部的gitlab管理，这里没简化操作，例如git pull origin master或git pull的时候，是防止此时可能会存在着多分支的情况会导致运行报错
if [ $? == 0 ];then
    echo "当前配置文件为最新版本，可以发布！"
else
    echo "当前配置文件不是最新的，请检查后再发布"
exit
fi
#此为发布单平台多IP的逻辑，$#判断参数个数，这里的逻辑判断为参数大于或等于3时就是单平台多IP发布。
if [ $# >=3 ];then
shift 1
这里通过shift命令往左偏移一个位置参数，从而获取全部的IP。
  echo "此次需要更新的机器IP为：$@"
for flat in $@
do
  echo "此次需要更新的机器IP为：$flat"
platform=`awk '/\[/{a=$0}/'"$flat"'/{print a}' $hosts | head -n1`
	#通过这段awk命令组和来获取当前的机器ip属于哪条线路，比如是移动还是网通或者电信，后续有相应的措施。
if  [[ $platform =~ "yd" ]];then
    /usr/local/bin/ansible -i $hosts $flat -m shell -a "/home/fastcache_conf/publish_fastcache.sh ${public_conf}_yd"
elif  [[ $platform =~ "wt" ]];then
    /usr/local/bin/ansible -i $hosts $flat -m shell -a "/home/fastcache_conf/publish_fastcache.sh ${public_conf}_wt"
else
    /usr/local/bin/ansible -i $hosts $flat -m shell -a "/home/fastcache_conf/publish_fastcache.sh ${public_conf}_dx"
fi
done
fi
#程序正常运行后，也要清理此临时文件，方便下次任务发布。
rm -rf $hosts
trap "rm -rf $hosts" exit