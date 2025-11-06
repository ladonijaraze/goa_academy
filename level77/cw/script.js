
let myArray = ["a", "b", "c", "d", "e"];


let spliced = myArray.splice(1, 3);
console.log("Spliced:", spliced); ['b', 'c', 'd']
console.log("Original after splice:", myArray);

let sliced = spliced.slice(1, 3); 
console.log("Sliced:", sliced);

sliced.splice(1, 0, "x", "y"); 
console.log("Sliced after splice:", sliced); 
