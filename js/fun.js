/* 函数可以保存为变量 */
var fun = function() {
	return 'Hello,world!';
};
console.log(fun());

/* 函数可以保存对象字段 */
var person = {
	name: 'Tom',
	smile: function() {
		return 'Smile';
	}
};

console.log(typeof person); // person为Object类型

console.log(person);
console.log(typeof person.smile);
console.log(person.smile());
