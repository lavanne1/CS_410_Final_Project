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
This function dispalys the main menu and takes the user's input.

### def recipe_rec(df):
This function provides a recipe recomendation for the users. The recommendation will be a recipe for which the users has not entred a preference. The recommended recipe title and url will be printed. This function takes the merged data and preferences pandas dataframe and returns None.

### def get_classifier(df):
The function is used by the "evaluate_recipe()" function to return a pipeline object. The merged pandas datafram is passes as an input to the fuction. This fuction then creates a pipeline to transform data into a tfidf matrix then classify it according the a multinomial Naive Bayes classifier. This function primarily relies on functionality from the scikitlearn python library.

### def evaluate_recipe(df):
This function evaluates a recipe by predicted that it will be either "good" or "bad" according the the user's preferences. This function takes asks the user to input a url of a recipe (url's must be already scraped and loaded into the database). This function then calls the "get_classifier()" function to get a multinomial Naive Bayes classifier trained on the tfidf transformed preferenes the user had previous defined. Using this classifier, this function will predicted whether the input url would be a good of bad recipe.

### def update_preferences(df):
This function allows the user to update prefrenes about recipes in the database. The user will entere a url and a rating (good or bad). This function then updates the preference values in the database and writes all new preferences to the preferences.txt file.

### def merge_data_and_pref(df, pref):
The function merged the pandas dataframes created in "get_preferences()" and in "read_data()" into one pandas dataframe.

### def get_preferences(df):
This function extracts the user preferences from the preferences.txt file. If this file does not exist, this function will create a new preferences.txt file initialized with "NULL" values for all preferences. Data extratacted from preferences.txt is then converted to a pandas dataframe and returnted by this function.

### def read_data():
This function reads the raw data .txt files containing the scraped recipe data. The .txt data files were created using a web crawler and scraper to extract recipe data. This data was then converted to .txt files. This function extracts all this data and converted it to a pandas dataframe, which this function returns.

## Implementation

### Updating Preferences

### Evaluating a Recipe

### Providing Recipe Reccomendation


## Usage
