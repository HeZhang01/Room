var c = console.log;
/* 柯里化 */

/**
 * 概念：只传递给函数一部分参数来调用它，让他返回一个函数去处理剩下的参数；
 * */ 
/* 每次只传入一个参数分多次调用 */

var add =  function(x) {
	return function(y) {
		return x + y;
	};
};

var increment = add(1);
var addTen    = add(10);

c( increment(2) ); // 3
c( addTen(2) );    // 12


/* 创建curry函数 */
var curry = require('lodash').curry;

var match = curry(function(what, str) {
	return str.match(what);
});

var replace = curry(function(what, replacement, str) {
	return str.replace(what, replacement);
});

var filter = curry(function(f, ary) {
	return ary.filter(f);
});

var map = curry(function(f, ary) {
	return ary.map(f);
});

match(/\s+/g, "hello world");// [ ' ' ]
match(/\s+/g)("hello world");// [ ' ' ]

var hasSpaces = match(/\s+/g);// function(x) { return x.match(/\s+/g) }
hasSpaces("hello world");// [ ' ' ]
hasSpaces("spaceless");// null

filter(hasSpaces, ["tori_spelling", "tori amos"]);// ["tori amos"]

var findSpaces = filter(hasSpaces);// function(xs) { return xs.filter(function(x) { return x.match(/\s+/g) }) }
findSpaces(["tori_spelling", "tori amos"]);// ["tori amos"]
var noVowels = replace(/[aeiou]/ig);// function(replacement, x) { return x.replace(/[aeiou]/ig, replacement) }

var censored = noVowels("*");// function(x) { return x.replace(/[aeiou]/ig, "*") }
censored("Chocolate Rain");// 'Ch*c*l*t* R**n'


// 以上实例表明函数的"预加载"能力，通过传递一到两个参数调用函数，就能得到一个记住了这些参数的新函数









/*==============================================================*/
/* TODO curry的简单实现 */
var curr = function(f){
	return function(){
		return f.apply(f, arguments);
	};
};
var mmatch = curr(function(what, str) {
	return str.match(what);
});

c( mmatch(/\s+/g, "hello world") );
//c( mmatch(/\s+/g)("hello world") );
