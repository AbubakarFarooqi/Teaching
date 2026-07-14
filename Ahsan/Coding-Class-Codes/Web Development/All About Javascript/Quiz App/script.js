const questionSpan = document.getElementById('question')
const option1Span = document.getElementById('op1')
const option2Span = document.getElementById('op2')
const option3Span = document.getElementById('op3')
const option4Span = document.getElementById('op4')


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