var c = console.log;
/* 代码组合 */

// f和g都是函数，x是它们之间通过"管道"传输的值
var compose = function(f, g) {
	return function(x) {
		return f( g(x) );
	};
};

var upper = function(x) { return x.toUpperCase(); };
var excla = function(x) {return x + '!';};
var shout = compose(excla, upper);

c( shout('send in the clowns') );
