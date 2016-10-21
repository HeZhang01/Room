<?php
//$http = new swoole_http_server("127.0.0.1",9501);
//$http->on('request',function($request,$response) {
//	var_dump($request->get, $request->post);
//	$response->header("Content-Type","text/html; charset=utf-8");
//	$response->end("<h1>Hello,world!</h1>");
//});

//$http->start();

//创建websocket服务器对象，监听0.0.0.0:9502端口
$ws = new swoole_websocket_server("0.0.0.0", 9502);

//监听WebSocket连接打开事件
$ws->on('open', function ($ws, $request) {
	echo "Open websocket :" . $request->fd . "\n";
});

//监听WebSocket消息事件
$ws->on('message', function ($ws, $frame) {
    $msg =  'Received message from '. $frame->fd . ' Contnet: ' .":{$frame->data}\n";
    
	foreach($ws->connections as $fd)
	{
    	$ws->push($fd, $msg);
	}
});

//监听WebSocket连接关闭事件
$ws->on('close', function ($ws, $fd) {
    echo "client-{$fd} is closed\n";
});

$ws->start();
