# CS_410_Final_Project

The documentation should consist of the following elements: 
1) An overview of the function of the code (i.e., what it does and what it can be used for). 
2) Documentation of how the software is implemented with sufficient detail so that others can have a basic understanding of your code for future extension or any further improvement. 
3) Documentation of the usage of the software including either documentation of usages of APIs or detailed instructions on how to install and run a software, whichever is applicable.  
4) Brief description of contribution of each team member in case of a multi-person team.  


## Overview of Functions:

### def main_loop():
This function controls the flow of the program. It serves as the "main function". Initially it calls the "read_data()" function to read the raw recipe data scraped from the web. Then "main_loop()" calls "get_preferences()" to extracts the users preferences about the recipes in the database. Then "merge_data_pref()" is called to merge the raw recipe data scraped from the web with the user preferences into on pandas dataframe.

The "main_loop()" then enters into a loop to display the menu choices from the "menu_choise()" function. According the to the user input, the "main_loop()" will then enter to the appropriate function associated with the user's input. The user can choose to do any of the following:
  1) Update user's preferences about recipes in the database as either a "good" or "bad" recipe
  2) Evaluet a recipe for which the user has no known preference and classify it as being a "good" or "bad" recipe
  3) Get a recipe recomendation of a recipe for which the user has no known preference



### def menu_choice():

### def recipe_rec(df):

### def get_classifier(df):

### def evaluate_recipe(df):

### ef update_preferences(df):

### def merge_data_and_pref(df, pref):

### def get_preferences(df):

### def read_data():
