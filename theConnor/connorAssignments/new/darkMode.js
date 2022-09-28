
const myVar = prompt();

//switch 
// switch (myVar) {
//     case 'hello':
//         alert('hello back');
//         break;
//     case 'whats up':
//         alert('whats up back');
//         break;
//     default:
//         alert("yo");
// }

// Make the equivalent in if else ! 
// DO IT!!!

if(myVar === 'Hello') {
    alert('Hello There');
} else if (myVar === 'What\'s up') {
    alert('What\'s up back');
} else {
    alert('Any other case');
}

const myArray = ['the zeroth element', 'the one element', 'the two element'];

console.log(myArray[0]);
console.log(myArray[1]);
console.log(myArray[2]);

myArray.push('yo');

console.log(myArray[3]);

const myObj = {
    pairOf : 'sleep pants',
    iNeedTo : 'go home',
    name: "austin",
    age: "old",
}

console.log(myObj.age);
console.log(myObj.name);
console.log(myObj.iNeedTo);

// okay here's the cool thing about arrays.... you can sort through them with a loop... 
// but first let's get the size of an array. 

