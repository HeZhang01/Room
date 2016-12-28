#! /bin/bash

# 必应搜索背景桌面下载脚本 by hezhang
# 2016/08/24
# 此功能依赖于jq
`curl 'http://cn.bing.com/HPImageArchive.aspx?format=js&idx=0&n=1&nc=1472008012548&pid=hp&scope=images:zh-cn&mkt=zh-CN&video=1' -H 'Accept-Encoding: gzip, deflate, sdch' -H 'Accept-Language: zh-CN,zh;q=0.8' -H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/51.0.2704.79 Chrome/51.0.2704.79 Safari/537.36' -H 'Accept: */*' -H 'Referer: http://cn.bing.com/?scope=images:zh-cn&mkt=zh-CN' -H 'Cookie: MUID=2EA4AFBE24E16F02252FA6A620E16C71; SRCHD=AF=NOFORM; SRCHUID=V=2&GUID=434E951B819647BDB38BAED24FD2C823; SRCHUSR=DOB=20160823; MUIDB=2EA4AFBE24E16F02252FA6A620E16C71; HPBingAppQR=CLOSE=1; WLS=TS=63607604799; _EDGE_S=mkt=zh-cn&SID=303AB116E6AC61F22ED1B86DE70D60B4; SRCHHPGUSR=CW=1520&CH=150&DPR=1&UTC=480; _SS=SID=303AB116E6AC61F22ED1B86DE70D60B4&bIm=648662&HV=1472008013' -H 'Connection: keep-alive' --compressed > json.txt`

# 提取url #
url=`cat json.txt | jq ".images[0].url"`
baseUrl='http://s.cn.bing.net'

# 获取图片名称（日期） #
date=`cat json.txt | jq '.images[0].enddate'`
brief=`cat json.txt | jq ".images[0].copyright"`

# 由于jq提取出来的元素带引号（故需通过正则提取） #
dates=`sed 's/^\"\(.*\)\"$/\1/'<<<$date`
urls=`sed 's/^\"\(.*\)\"$/\1/'<<<$url`
urls=${baseUrl}${urls}
imgName=$dates.jpg


# 禁止重复下载 #
if [ -f "$imgName" ];then
	echo "今日图片已下载"
	eog $imgName &
	exit 1
fi

# 下载图片 #
sudo touch $imgName
sudo chmod a+w $imgName
echo "Downloading....................................."
`sudo curl $urls  > $imgName`
echo "OK"

# 打开图片 #
eog $imgName &
