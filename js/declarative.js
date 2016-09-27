
/* 声明式编程 */


/* Hindley-Milner类型签名 */

// capitalize :: String -> String
var capitalize = function(s) {
	return toUpperCase(head(s)) + toLowerCase(tail(s));
};

capitalize("hello");  // => "Hello"
console.log(capitalize("hello"));

