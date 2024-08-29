'''
Create a date.py script that is a date simulator and does the following:

User inputs who is on the date with them
User inputs their budget for the date
Print the restaurant menu (your group created this!) 
User inputs their food/drink item choices from a restaurant menu list (for themselves and their date)
Script tells the user how much money they have left after each order.
At the end of the date user must agree to pay the bill and then their final budget is shown to them.
Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision. 
'''

your_name = input("Please enter your name.\n")
date_name = input("who is on the date with you?\n")
budget = input("Please enter the budget. \n")
second_date = 10

#if the budget is lower than the lowest cost in this resturant then deduct 1 point
if (float(budget) < 75):
    second_date -= 4

#The menu is a dict, we have apptizer, entree and dessert. In each part, we can have the name of the dish and price, and description and whether is vegan
Menu={
        "AppMenu": {
                 "Hush puppies": {"name":"Hush puppies", "price": 8.00, "description": "fried corn meal fritters", "Vegan":True},
                 "Clam Chowder": {"name":"Clam Chowder", "price": 13.00, "description": "New England Style Clam Chowder", "Vegan": False},
                 "Shrimp Cocktail": {"name":"Shrimp Cocktail", "price": 10.00, "description": "Steamed Jumbo Shrimp with cocktail sauce", "Vegan": False},
            },

        "Entree":{
            "Snow Crab Boil": {"name":"Snow Crab Boil", "price": 25.00, "description": "1lb of snow crab with corn and potatoes", "Vegan":False},
            "Lobster Linguine": {"name":"Lobster Linguine", "price": 30.00, "description": "Buttered Lobster in a cream sauce in Linguine with a bed of steamed broccoli", "Vegan":False},
            "Whole Maine Lobster": {"name":"Whole Maine Lobster", "price": 45.00, "description": "1 1/2lb of lobster with baked potato and mixed veggies", "Vegan":False},
        },

        "Dessert": {
            "Canoli": {"name":"Canoli", "price": 5.00, "description": "Marscapone cheese with chocolate chips in a fried pastry shell", "Vegan":False},
            "Apple Pie": {"name":"Apple Pie", "price": 8.00, "description": "Macintosh Apples and Cinnamon in a flakey buttery crust with a scoop of vanilla bean ice cream on top", "Vegan":True},
            "Mochi Ice Cream": {"name":"Mochi Ice Cream", "price": 6.00, "description": "Vanilla with Red bean", "Vegan":False},

        } 
}
print(f"Here is our Menu: \n {Menu}")


#take some user input using input
taste = input("Do you know the taste of your date? (yes/no)\n")
if(taste == "yes"):
    second_date += 1
elif (taste == "no"):
    second_date -= 1

#here is a function for order. Uisng function here is to reuse this part
def get_order(budget):
    #the buget here is string when taking the user input. To compare with float or int, we need to cast
    total = float(budget)

    # app
    print(f"Your can select the appertizer by typing the name: ")
    for key in Menu["AppMenu"]:
        print(key)
    Apptizer = input("What apptizer you would like to order?")
    total -=  Menu["AppMenu"][Apptizer]["price"]
    print(f"You have {total} dollars left")

    #entree
    print(f"Your can select the entree by typing the name:  ")
    for key in Menu["Entree"]:
        print(key)
    Entree = input("What entree you would like to order? \n")
    total -= Menu["Entree"][Entree]["price"]
    print(f"You have {total } dollars left")

    #dessert
    print(f"Your can select the dessert by typing the name: ")
    for key in Menu["Dessert"]:
        print(key)
    Dessert = input("Do you want some dessert? \n")
    total -= Menu["Dessert"][Dessert]["price"]
    print(f"You have {total } dollars left")

    print(f"Your can select the appertizer by typing the name: ")
    for key in Menu["AppMenu"]:
        print(key)
    Apptizer_date = input("What apptizer you would like to order for your date?\n")
    total -= Menu["AppMenu"][Apptizer_date]["price"]
    print(f"You have {total } dollars left")

    print(f"Your can select the entree by typing the name:  ")
    for key in Menu["Entree"]:
        print(key)
    Entree_date = input("What entree you would like to order for your date? \n")
    total -= Menu["Entree"][Entree_date]["price"]
    print(f"You have {total } dollars left")

    print(f"Your can select the dessert by typing the name: ")
    for key in Menu["Dessert"]:
        print(key)    
    Dessert_date = input("Do you want some dessert for your date? \n")
    total -= Menu["Dessert"][Dessert_date]["price"]
    print(f"You have {total } dollars left")

    print(f"You ordered {Menu["AppMenu"][Apptizer]["name"]}, {Menu["Entree"][Entree]["name"]}, and {Menu["Dessert"][Dessert]["name"]}.")
    print(f"You ordered {Menu["AppMenu"][Apptizer_date]["name"]}, {Menu["Entree"][Entree_date]["name"]}, and {Menu["Dessert"][Dessert_date]["name"]} for your date.")
    
    
    total_cost_you = Menu["AppMenu"][Apptizer]["price"] + Menu["Entree"][Entree]["price"] + Menu["Dessert"][Dessert]["price"]
    total_cost_date = Menu["AppMenu"][Apptizer_date]["price"] + Menu["Entree"][Entree_date]["price"] + Menu["Dessert"][Dessert_date]["price"]
    total_cost = total_cost_date + total_cost_you


#for the final cost, show it to the user here. 
    print(f"The total cost is {total_cost}.")
    left = float(budget) - float(total_cost)
    if(left >= 0):
        print(f"You have {left} dollors left. ")
    else:
        print(f"You have to pay {-left} dollars more.")
    
    return total_cost

total_cost = get_order(budget)
#once the user budget is low, we will ask the user, whether or not like to increase the budget or re-order
if(total_cost > float(budget)):
    change_budget = input("The total price is over your budget, would you like to order again or increase your budget?\n Please Enter 'yes' or 'no'\n")
    if (change_budget == 'yes'):
            budget = input("Please enter your new budget. \n")
            if(total_cost > float(budget)):
                second_date -= 1
            
            change_order = input("Would you like to re-order? Please enter 'yes' or 'no'. \n")
            if(change_order == 'yes'):
                total_cost = get_order(budget)
                if(total_cost < float(budget)):
                    second_date += 1
            elif (change_order == 'no'):
                print(f"Your bedget incresed to {budget} dollars, and there are {float(budget) - float(total_cost)} dollars left now.")
    elif(change_budget == 'no'):
        #here the else if statement is to let the user know because they have lower budget and not going to reorder, so we can not process the order
            print("Sorry, we can not process futher for your date.")
            exit()
#ensure that the user will pay and show the total cost
pay = input("If you agree to pay, please enter 'yes'or 'no' ")
match pay:
    case "yes":
        print(f"Thank you! Your total cost will be {total_cost} dollars.")
        print(f"Enjoy the night with {date_name}, {your_name}!")
    case "no":
        print(f"Sorry, we can not process futher for your date.")      
        exit()

#ask for the satisfaction of the date, if it is high, more chance to get the second date
satisfaction = input("Does your date like the meal tonight? (scale 1 - 10)\n")
if(int(satisfaction) > 7):
    second_date += 1
elif (int(satisfaction) > 8):
    second_date += 2
elif(int(satisfaction) < 7):
    second_date -= 2

#make a decision based on previous inputs. tell the user 
if(second_date > 7):
    print(f"{your_name}, you are likely to get the second date.")
else:
    print(f"Sorry, {your_name}, you probably not going to get the second date with {date_name}")
                      
            
            
            
            
            

    
