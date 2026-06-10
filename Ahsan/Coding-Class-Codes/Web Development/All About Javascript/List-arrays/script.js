// let marks = [22,33,12,17]

// // console.log(marks)
// //accessing an element
// console.log(marks[1])

// // change value
// marks[2] = 20
// console.log(marks)

// // Add value
// marks.push(99)
// console.log(marks)

// // removing value from end
// marks.pop()
// console.log(marks)

// // Loop over the list

// for (const i of marks){
//     console.log(i)
// }

// for (let i = 0;i<marks.length;i=i+4){
//     console.log(marks[i])
// }

/*
create a list of 5 number
console log the total number of elements in it
console log the third element 
change the 4th value to something else
Insert a new value at end
remove a value from the end
Loop over the entire list
Loop over the entire list by skip count 2

filter()
includes()


*/


// let lst = [1,2,3,4,5,6,7,8,9,10]

// let filter_lst = lst.filter(x => x != 5) // => arrow operator
// console.log(lst)
// console.log(filter_lst)

let lst = [
    {
        "id":1,
        "name":"Ahsan",
        "grade":7
    },
    {
        "id":2,
        "name":"abubakar",
        "grade":9
    }
]

let filter_list = lst.filter(x => x.name == "abubakar")
console.log(filter_list)