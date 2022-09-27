//==============================================================
//==============================================================
//Notes on videos from WEBDEV SIMPLIFIED
//https://www.youtube.com/watch?v=DHvZLI7Db8E
//promises are resolved or rejected (complete of failed) 
//vanilla...
//==============================================================
//==============================================================
// let p = new Promise((resolve, reject) => {
//     //what the promise is.... 
//     let a = 1 + 2;
//     if(a == 2){
//         //what tells it to run on .then
//         resolve('RESOLVED...');
//     }else{
//         //what tells it to run on .catch
//         reject('REJECTED....');
//     }
// })
// //how to interact. the .then only runs on resolve....
// p.then((message) =>{
//     //runs if the promise resolved. 
//     console.log('this is in the then. ' + message);
// }).catch((message)=>{
//     //runs if the promise rejected or fails
//     console.log('fromt the catch block. ' + message);
// }) 

//A lovely example of some callback vs promise which we will come back to.
// const userLeft = false;
// const userWatchingCatMeme = false;

// //I guess this is a callback function....
// function watchTutorialCallback(callback, errorCallback){
//     if(userLeft){
//         //we give this function to this parent function. The params for this is message. see below. 
//         errorCallback({
//             name: 'userLeft',
//             message: 'sucks'
//         })
//     }else if(userWatchingCatMeme){
//         errorCallback({
//             name:'User Watching Cat Meme',
//             message:'WebDev < cat'
//         })
//     }else{
//         callback(' went well');
//     }
// }

// //calling it will explain some things... We'll need to give it some stuff. 
// watchTutorialCallback((message) => {
//     console.log('success' + message)
// }, (error) => {console.log((error.name) + ' ' + error.message)
// })


//MUCH CLEANER!!!!! 
// const userLeft = false;
// const userWatchingCatMeme = false;

// //
// function watchTutorialPromise(){
//     return new Promise((resolve, reject) =>{
//         if(userLeft){
//             //we give this function to this parent function. The params for this is message. see below. 
//             reject({
//                 name: 'userLeft',
//                 message: 'sucks'
//             })
//         }else if(userWatchingCatMeme){
//             reject({
//                 name:'User Watching Cat Meme',
//                 message:'WebDev < cat'
//             })
//         }else{
//             resolve(' went well');
//         }

//     })
// }
// //calling it will explain some things... We'll need to give it some stuff. 
// watchTutorialPromise().then((message) => {
//     console.log('success' + message)
// }).catch((error) => {console.log((error.name) + ' ' + error.message)
// });

// const recordVideoOne = new Promise((resolve, reject)=>{
//     resolve('vid one recorded');
// });

// const recordVideoTwo = new Promise((resolve, reject)=>{
//     resolve('vid Two recorded');
// });

// const recordVideoThree = new Promise((resolve, reject)=>{
//     resolve('vid Three recorded');
// });

// //lets me run all these promises in parallel. It seems promises can take some time?. .then runs after completion... upon success... takes array of promises to run. 
// Promise.all([
//     recordVideoOne,
//     recordVideoTwo,
//     recordVideoThree
// ]).then((messages) => {
//     console.log(messages);
// });

// //will run .then as soon as the first one finishes. 
// Promise.race([
//     recordVideoOne,
//     recordVideoTwo,
//     recordVideoThree
// ]).then((message) => {
//     console.log(message);
// });

//==============================================================
//==============================================================
//Notes on videos from WEBDEV SIMPLIFIED
//https://www.youtube.com/watch?v=V_Kr9OSfDeU
//==============================================================
//==============================================================
// function makeRequest(location){
//     return new Promise((resolve, reject)=>{
//         console.log(`making request to ${location}`)
//         if(location === 'Google'){
//             resolve('Google says hi')
//         }else{
//             reject('We can only talk to google')
//         }
//     })
// }
// function processRequest(response){
//     return new Promise((resolve, reject) => {
//         console.log('processing response')
//         resolve(`Extra info + ${response}`)
//     })
// }
// //THIS 
// // makeRequest('face').then((response => {
// //     console.log('response recieved')
// //     return processRequest(response)
// // })).then(processedResponse => {
// //     console.log(processedResponse)
// // }).catch(err => {
// //     console.log(err)
// // })
// //verses this.
// async function doWork(){
//     const response = await makeRequest('Google');
//     console.log('Response Recieved');
//     const processedResponse = await processRequest(response)
//     console.log(processedResponse) 
// }
// doWork();
// console.log('hello');
// for(var i = 0; i<7; i++){
//     console.log(`${i} ) hello`);
// }
// function taskOne() {
//     console.log('task 1');
// }
// function taskTwo() {
//     console.log('task 2');
// }
// taskOne();

// //has to run AFTER task one. no matter how long one takes. n
// taskTwo();

//Declare a variable to use in the loop. 
// var userInput = '';
// //continue prompting the user for input until the user enters a 0.
// while(userInput!==0){
//     //the user input is the integer conversion of the prompt...
//     userInput=parseInt(prompt('PLEASE enter a number...'));
//     if(isNaN(userInput)){
//        alert('you did not follow instructions stupid user')
//     }else{
//         //log it just for funsies
//     document.write(userInput);
//     }
//     //do a demo on a condition....
//     if(userInput===2){
//         document.write('yo you entered a 2');
//     }
// }
// for(i = 10; i>0; i--){
//     console.log(i);
// }

//make a menu...
//get some data from the user...

// alert("=================\n" + " MENU\n" + "=================\n" + "A) for greeting \nB) for a joke");

// let userChoice = '';

// while(userChoice!='q'){

//     userChoice = prompt("enter a valid menu choice");
//     console.log(userChoice);

//     switch(userChoice){
//         case 'A':
//             console.log("Hello to you, user.");
//             break;
//         case 'B':
//             console.log("This is supposed to be a joke.");
//             break;
//         case 'q':
//             console.log('Later');
//             break;
//         default:
//             console.log("i am a default");
//     }
// }

