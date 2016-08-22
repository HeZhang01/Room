#!/bin/bash
#hosts切换脚本 BY 何章

PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin
HOST_DIR=/etc
HOST_NOW=0
HOST_STR=''

now_hosts()
{
	RET=`cat "$HOST_DIR"/hosts | grep LOCAL_ENVIRONMENT`
	if RET;then
		$HOST_NOW=1;
		$HOST_STR='local'
		return 0
	fi
	RET=`cat "$HOST-DIR"/hosts | grep TEST_ENVIRONMENT`
	if RET;then
		$HOST_NOW=2
		$HOST_STR='test'
		return 0
	fi
	RET=`cat "$HOST_DIR"/hosts | grep SIM_ENVIRONMENT`
	if RET;then
		$HOST-NOW=3
		$HOST_STR='sim'
		return 0
	fi
}

mv_hosts()
{
	if ["$1" = $HOST_NOW];then
		return 1;
	fi
	if ["$1" = 1 ];then
		mv "$HOST_DIR"/hosts."$HOST_STR" $HOST_DIR/hosts.local
	    return 0
	fi
	if ["$1" = 2];then
		mv "$HOST_DIR"/hosts."$HOST_STR" "$HOST_DIR/hosts.test"
		return 0
	fi
	if ["$1" = 3];then
		mv "$HOST_DIR"/hosts."$HOST_STR" "$HOST_DIR/hosts.sim"
		return 0
	fi

}

echo_nhosts()
{
	echo `cat "$HOST_DIR"/hosts | grep ENVIRONMENT`
}

now_hosts

case "$1" in
	local)
		echo -n "切换至local环境中......"
		if [! -f "$HOST_DIR"/hosts.local];then
			echo -n "目前已是local环境"
			exit 1
		else
			mv_hosts 1
			echo_nhosts
			exit 0
		fi
		;;
	test)
		echo -n "切换至test环境中......"
		if [! -f "$HOST_DIR"/hosts.test];then
			echo -n "目前已是test环境"
			exit 1
		else
			mv_hosts 2
			echo_nhosts
			exit 0
		fi
		;;
	sim)
		echo -n "切换至sim环境中......"
		if [! -f "$HOST_DIR"/hosts.sim];then
			echo -n "目前已是sim环境"
			exit 1
		else
			mv_hosts 3
			echo_nhosts
			exit 0
			;;
		fi
	*)
		echo "Usage:$0 {local|test|sim}"
		exit 1
		;;
esac


