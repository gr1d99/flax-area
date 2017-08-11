function add(a, b) {
    var c = Number(a) * Number(b);
    return c;
}
console.log(add(2, 2));
output.innerHTML = add(2, 3);

var myString = 'Hello world this is gideon kim';

function mySearch(someString, searchString) {
    var foundString = null;
    foundString = someString.search(/\b[a-z]{5}\b/);
    return foundString;
}

console.log(mySearch(myString, 'Hello'));

