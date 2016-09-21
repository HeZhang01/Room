
var c = console.log;
var $ = {
	'getJSON': function(x, y){ return Math.random(x + y); }
};

/* 纯函数 */

// memoize的简单实现(缓存函数)
var memoize = function(f) {
	var cache = {};

	return function() {
		var arg_str = JSON.stringify(arguments);
		cache[arg_str] = cache[arg_str] || f.apply(f, arguments);
		return cache[arg_str];
	};
};


/* 可缓存性(Cacheable) */
var squareNumber = memoize( function(x) { return x * x } );

console.log( squareNumber(4) ); // 16
c( squareNumber(4) ); // 从缓存中读取输入值为4的结果 
c( squareNumber(5) ); // 25
c( squareNumber(5) ); // 从缓存中读取输入值为5的结果 
c( squareNumber(4) ); // 从缓存中读取输入值为4的结果 


	/* 可以通过延迟执行的方式将不纯的函数转换为纯函数 */
	var pureHttpCall = memoize( function(url, params) {
		return function() { return $.getJSON(url, params) };
	}
	);
/* 可移植性/自文档化(Portable) */
// 不纯的
var signUp = function(attrs) {
	var user = saveUser(attrs);
	welcomeUser(user);
};

// 纯的(信息全面的数字签名和延迟执行)
// 强迫的注入依赖
var signUp(Db, email, attrs) {
	return function() {
		var user = saveUser(Db, attrs);
		welcomeUser(email, user);
	};
};

/* 并行执行(没有副作用) */
