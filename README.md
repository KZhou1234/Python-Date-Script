# Python Practice
The repository will be continuously updated with scripts written in Python. It will also include some of my own troubleshooting procedures for good measure.

## Exercise One:  Date Simulator
The date simulator does the following:

* User inputs who is on the date with them
* User inputs their budget for the date
  * The budge for dating is a significant role in date. In this script, the budget should cover at least one appetizer, one entree and one dessert per person.
  * If cannot be covered, the second date chance will reduce.
* Print the restaurant menu
  * Our group made a seaFood Restruant menu using nested dictionary. In this way, we can quickly get the name, value, or description according user input.
  * At the beginning, our group used a list to create different sections in the menu dict. Even though we could still retrieve items and display the menu, it makes more sense to retrieve them by key instead of using an index.  
* User inputs their food/drink item choices from a restaurant menu list
  * Before the user order anything, ask the user some questions about date, if they know too few about their date, then reduce the score.
  * The user can preselect the dishes with considering their budget.
* Script tells the user how much money they have left after each order.
  * It's important to let the user know how much money they have left in order to make adjustments to their budget.
  * If the cost is higher than the budget, then ask the user if they want to increase the budget or reorder.
    * If the adjusted budget is still low, then deduct some points from the total.
* At the end of the date user must agree to pay the bill and then their final budget is shown to them.
  * If the user refuse to pay, then exit.
  * Ask for the satisfaction rate from the date's perspective.
* Challenge: Based on all the user inputs, the script should decide whether the user will get a second date or not and tell the user the decision.
  * The threshold for the second date was set to 7, if the final score below 7, then the user probably not going to have the next date; if higher than 7, the user very likely to get the next date.

