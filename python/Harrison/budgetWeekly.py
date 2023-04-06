
usersWeeklyBudget = int(input("Please Enter your weekly budget: "))
usersCurrentWeekExpenses = 0 
for day in range(1,8):
    tempExpense = int(input("How much did you spend today?: "))
    # rest the users currentWeekExpenses to be what I have already spent plus what I just did spend.
    usersCurrentWeekExpenses = usersCurrentWeekExpenses + tempExpense

print(usersWeeklyBudget)
print(usersCurrentWeekExpenses)
differenceFromBudget = usersCurrentWeekExpenses - usersWeeklyBudget

if(differenceFromBudget > 0):
    print(f"Over Budget by {differenceFromBudget}")
elif(differenceFromBudget < 0):
    print(f"Under Budget by {differenceFromBudget * -1}")
