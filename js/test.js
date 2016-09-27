
var add = function (x) {return x++};
var fun = function (g) {return g(g)};

console.log(typeof fun);
console.log(typeof fun(add));

