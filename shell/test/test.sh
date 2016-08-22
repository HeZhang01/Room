#!/bin/bash
ret=`cat hosts | grep loa`
if [ "$?" = '0' ];then
	echo 'OK'
	exit
fi
echo "fail"
