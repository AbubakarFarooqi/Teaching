const input = document.getElementById("input")
const type = document.getElementById("type")
const description = document.getElementById("description")
const amount = document.getElementById("amount")
const addTransaction = document.getElementById("addTransaction")
const transactionHistory = document.getElementById('transactionHistory') 

const expenses = []

addTransaction.addEventListener("click", (e) => {
    e.preventDefault()
    const transactionType = type.value
    const transactionDesc = description.value
    const transactionAmount = amount.value
    if (transactionType == "" || transactionDescription == "" || transactionAmount == "") {
        alert("Fill out the inputs before adding a transaction")
        return
    }

    expenses.push({
        "type":transactionType,
        "description":transactionDesc,
        "amount":transactionAmount
    })
    console.log(expenses)
    CalculateTotalIncomeAndExpense()
    ShowTransaction(transactionAmount,transactionDesc,"2026-09-15",transactionType)
})

function CalculateTotalIncomeAndExpense () {
    totalIncomeSum = 0
    totalExpenseSum = 0

    for(const transaction of expenses)
    {
        if (transaction["type"] == "income"){
            totalIncomeSum += parseInt(transaction["amount"])
        }
        if (transaction["type"] == "expense"){
            totalExpenseSum += parseInt(transaction["amount"])
        }
    }

    currentBalance = totalIncomeSum - totalExpenseSum

    const curBalSpan = document.getElementById('curBalSpan')
    const incomeSpan = document.getElementById('incomeSpan')
    const expenseSpan = document.getElementById('expenseSpan')

    curBalSpan.innerHTML = "$ " + `${currentBalance}`
    incomeSpan.innerHTML = "$ " + `${totalIncomeSum}`
    expenseSpan.innerHTML = "$ " + `${totalExpenseSum}`
}

function ShowTransaction (amount,description,date,type) {

    if (type == "income")
    {
        incomeTransaction = document.createElement("div")
        incomeTransaction.classList.add ("income-transaction")
        

        incomeTransactionDetails = document.createElement("div")
        incomeTransactionDetails.classList.add ("transaction-details")

        incomeTransactionDescription = document.createElement("span")
        incomeTransactionDescription.classList.add ("transaction-description")
        incomeTransactionDescription.innerHTML = description


        incomeTransactionDate = document.createElement("span")
        incomeTransactionDate.classList.add ("transaction-date")
        
        incomeTransactionDate.innerHTML = date

        incomeAmountAndCancel = document.createElement("div")
        incomeAmountAndCancel.classList.add ("amount-and-cancel")
        

        incomeTransactionAmount = document.createElement("div")
        incomeTransactionAmount.classList.add ("income-transaction-amount")
        

        incomeTransactionAmountSpan = document.createElement("span")
        incomeTransactionAmountSpan.innerHTML = `+ $${amount}`


        incomeCancelTransaction = document.createElement("i")
        incomeCancelTransaction.classList.add ("fa-solid")
        incomeCancelTransaction.classList.add ("fa-x")

        incomeTransactionAmount.AppendChild (incomeTransactionAmountSpan)
        incomeAmountAndCancel.AppendChild (incomeTransactionAmount)
        incomeAmountAndCancel.AppendChild (incomeTransactionAmountSpan)
        incomeTransaction.AppendChild (incomeTransactionDetails)
        incomeTransaction.AppendChild (incomeTransactionDescription)
        incomeTransaction.AppendChild (incomeTransactionDate)
        incomeTransaction.AppendChild (incomeAmountAndCancel)

        transactionHistory.appendChild(incomeTransaction)
    }
    
else{
    expenseTransaction = document.createElement("div")
    expenseTransaction.classList.add ("expense-transaction")
    

    expenseTransactionDetails = document.createElement("div")
    expenseTransactionDetails.classList.add ("transaction-details")

    expenseTransactionDescription = document.createElement("span")
    expenseTransactionDescription.classList.add ("transaction-description")
    
    expenseTransactionDescription.innerHTML = description

    expenseTransactionDate = document.createElement("span")
    expenseTransactionDate.classList.add ("transaction-date")
    
    expenseTransactionDate.innerHTML = date
    
    expenseAmountAndCancel = document.createElement("div")
    expenseAmountAndCancel.classList.add ("amount-and-cancel")
    
    
    expenseTransactionAmount = document.createElement("div")
    expenseTransactionAmount.classList.add ("expense-transaction-amount")
    
    expenseTransactionAmountSpan = document.createElement("span")
    expenseTransactionAmountSpan.innerHTML = `- $${amount}`
    
    expenseCancelTransaction = document.createElement("i")
    expenseCancelTransaction.classList.add ("fa-solid")
    expenseCancelTransaction.classList.add ("fa-x")
    
    expenseTransactionAmount.AppendChild (expenseTransactionAmountSpan)
    expenseAmountAndCancel.AppendChild (expenseTransactionAmount)
    expenseAmountAndCancel.AppendChild (expenseTransactionAmountSpan)
    expenseTransaction.AppendChild (expenseTransactionDetails)
    expenseTransaction.AppendChild (expenseTransactionDescription)
    expenseTransaction.AppendChild (expenseTransactionDate)
    expenseTransaction.AppendChild (expenseAmountAndCancel)
    
    transactionHistory.appendChild(expenseTransaction)
}
  
}