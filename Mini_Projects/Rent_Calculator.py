"""
Input we need from User 
Total Amount of Rent 
Total food and snacks ordered amount spended on it
electricity units spend charge per unit 
Output of Total amount you have to pay is #answer
Adding all the amount will be equally divided between the person lives in the room
"""
# Basics Info about rent and amount spend on Food/Groceries etc
rent = int(input("Enter your rent Hostel/Flat amount: "))
food = int(input("Enter the amount of food ordered: "))

#Electricity Bills and how Much will be charged to each person based on the price on each unit spend
electricity_bill = int(input("Enter the total of Electricity Bill Amount: "))
Charge_per_unit = int(input("Enter The charge per unit:"))
Total_Bill = electricity_bill + Charge_per_unit

#Number of the Person who lives together and the total amount will be divided between them 
persons = int(input("Enter the Number of Persons Living in room/flat:"))

Output = (food+rent+Total_Bill)//persons
print("Each Person Will pay = ", Output)