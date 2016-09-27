
/* 容器 */

var Container = function(x) {
	this.__value = x;
};

// 容器构造器(constructor)
Container.of = function(x) {
	return new Container(x);
};

console.log( Container.of(3) );  //=> Container(3)

console.log( Container.of("hello, world") );  // =>Container("hello, world")


console.log( Container.of( Container.of({name: 'he'}) ) );  //=> Container(Container({name: 'he'}))


