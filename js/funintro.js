
/* 函数式编程简介 */

/* 匿名函数 */

// map函数

function map(a, f) 
{
	var res = [];
	for ( var i = 0, len = a.length; i < len; i++ )
	{
		res.push( f(a[i]) );
	}
	return res;
}

var maped = map( [1, 2, 3, 4, 5, 5], function (x) {
	return x * x;
} );

console.log(maped);

//注意 map 函数的调用，map 的第二个参数为一个函数，这个函数对 map 的第一个参数 ( 数组 ) 中的每一个都有作用，但是对于 map 之外的代码可能没有任何意义，因此，我们无需为其专门定义一个函数，匿名函数已经足够。






/* 柯里化 */

// 柯里化函数接受一些参数返回一个函数，然后让函数来继续处理后面的事
function adder(x)
{
	return function(y)
	{
		return x + y;
	};
}

var add1 = adder(1);
var add2 = adder(2);

console.log( add1(2) );
console.log( add2(2) );



/* 高阶函数 */
// 见上述的map函数



