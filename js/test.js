console.log("Hello world")
let student_name = "Harshitha"
console.log("Student name is: " + student_name)
let student_age = 21
let course_name = "Python Full Stack"
console.log("Student age is: " + student_age, "Course name is: " + course_name)
let fee = 10000
let discount = 10
let discounted_fee = fee - (fee * discount / 100)
console.log("Discounted fee is: " +  discounted_fee) 

let age=18
if(age>=18){
    console.log("Eligible for adminssion")
}
else{
    console.log("Not eligible for adminssion")
}
for(let i=1; i<=5; i++){
    console.log("Iteration number: " + i)
}
const pi = 3.14
console.log("Value of pi is: " + pi)
let student = {
    name: " Harshitha" ,
    age: 21,
    course: "Python Full Stack",
    fee: 10000
}
console.log("Student details: ", student)
function greetStudent(name){
    console.log("Hello " + name + ", welcome to NRRIT Learning Mangement System")
}
greetStudent(student_name)

// write a function to square a number
// write a function to odd or even number
function squareNumber(num) {
    return num * num;
}                    
x=squareNumber(5);
console.log("Square of 5 is: ",x)
 // write a function to odd or even number
function checkOddEven(num) {
    if (num % 2 === 0) {
        return "Even";
    } else {
        return "odd";
    }
}
console.log("check if 7 is odd or even: ", checkOddEven(7));


