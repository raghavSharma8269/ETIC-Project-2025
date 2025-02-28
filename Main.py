import requests

# API url
url = "http://localhost:5081/api/home"



# test url
def testConnection():
    response = requests.get(url+"/test")
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}") # prints status code and error given by api



# GET all expenses
def getExpenses():
    response = requests.get(url+"/expenses") # adds /expense endpoint
    if response.status_code == 200:
        print(response.json())
    else:
        print(f"Error: {response.status_code}, {response.text}")


# POST request to create new expense
def createExpense(new_expense): # expects new expense json parameter
    response = requests.post(url+"/create-expense", json=new_expense) # adds /create-expense endpoint

    if response.status_code == 200:
        print(f"Expense created: {response.json()}")
    else:
        print(f"Error: {response.status_code}, {response.text}")



# PUT request to update expense
def updateExpense(id, updated_expense): # expects id and updated expense json parameters
    response = requests.put(url+"/update-expense/"+id, json=updated_expense) # adds /update-expense/{id} endpoint

    if response.status_code == 200:
        print(f"Expense updated: {response.json()}")
    else:
        print(f"Error: {response.status_code}, {response.text}")


# DELETE request to delete expense
def deleteExpense(id): # expects id parameter
    response = requests.delete(url+"/delete-expense/"+id) # adds /delete-expense/{id} endpoint
    if response.status_code == 200:
        print(f"Expense deleted: {response.json()}")
    else:
        print(f"Error: {response.status_code}, {response.text}")



# allows user to perform CRUD operations with their inputs
def run():

    loop = 0
    while loop == 0:
        user_input = input("1. Get All Expenses\n2. Create New Expense\n3. Update Expense\n4. Delete Expense\n5. Exit\n" ) # command list for user to select CRUD operation

        user_input = int(user_input) # casts user input into int

        if user_input == 1:
            getExpenses()

        elif user_input == 2:

            description = input("Enter Description: ")
            value = input("Enter Value: ")

            new_expense = {

                "Description": description,
                "Value": value
            }

            createExpense(new_expense)

        elif user_input == 3:

            id = input("Enter ID: ")
            updated_description = input("Enter Updated Description: ")
            updated_value = input("Enter Updated Value: ")

            updated_expense = {
                "Description": updated_description,
                "Value": updated_value
            }

            updateExpense(id, updated_expense)

        elif user_input == 4:

            id = input("Enter ID for Deletion: ")

            deleteExpense(id)

        elif user_input == 5:
            break # ends loop




run()