const names = ["nika", "luka", "nukri"];

const [name1, name2, name3] = names;

console.log(name1); 
console.log(name2);
console.log(name3); 

const points = [10, 30, 5, 2, 99];

points.push(50);

points.pop();


points.shift(); 



const joined = points.join(" - ");
console.log("join:", joined); 
const asString = points.toString();
console.log("toString:", asString); 

const morePoints = [1, 2, 3];
const allPoints = points.concat(morePoints);
console.log("concat:", allPoints);

const fruits = ["apple", "banana", "mango"];
const lastFruit = fruits[fruits.length - 1];

console.log(lastFruit); 

const a = [9, 3, 1];
const b = [4, 6, 5];

const combined = a.concat(b); 
combined.sort((x, y) => x - y);

console.log(combined);

const letters = ["H", "e", "l", "l", "o"];
const word = letters.join("");

console.log(word);


