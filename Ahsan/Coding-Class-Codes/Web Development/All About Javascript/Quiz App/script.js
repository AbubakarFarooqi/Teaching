const questionSpan = document.getElementById('question')
const option1Span = document.getElementById('op1')
const option2Span = document.getElementById('op2')
const option3Span = document.getElementById('op3')
const option4Span = document.getElementById('op4')


let currentQuestion = 0
const questions = [
    {
        question: "Which language runs in a web browser",
        options: ["Java","JavaScript","Python","C++"],
        answer:1
    },
    {
        question: "What does CSS stand for?",
        options: [
          "Central Style Sheets",
          "Cascading Style Sheets",
          "Cascading Simple Sheets",
          "Cars SUVs Sailboats"
        ],
        answer: 1
      },
      {
        question: "What does HTML stand for?",
        options: [
          "Hypertext Markup Language",
          "Hypertext Markdown Language",
          "Hyperloop Machine Language",
          "Helicopters Terminals Motorboats Lamborghinis"
        ],
        answer: 0
      },
      {
        question: "Which method adds an item to the end of an array?",
        options: ["shift()", "pop()", "push()", "unshift()"],
        answer: 2
      },
      {
        question: "Which keyword declares a constant in JavaScript?",
        options: ["var", "let", "const", "static"],
        answer: 2
      }
]

function showQuestion(){
    const questionObject = questions[currentQuestion]

    questionSpan.innerHTML = questionObject.question

    selectedOption = null
    
    op1 = questionObject.options[0]
    op2 = questionObject.options[1]
    op3 = questionObject.options[2]
    op4 = questionObject.options[3]

    option1Span.innerHTML = op1
    option2Span.innerHTML = op2
    option3Span.innerHTML = op3
    option4Span.innerHTML = op4

    option1Span.addEventListener('click',function (){
        selectedOption = 0
        console.log("abc")
        option1Span.classList.add("select-option")
    })

    



}

showQuestion()