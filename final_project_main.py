# -*- coding: utf-8 -*-
"""
Created on Wed Apr  4 20:34:02 2018

@author: John LaVanne
"""

# -final_project_main.py *- coding: utf-8 -*-
"""
This program maintains a is used to evaluate recipes

Version FINAL:
"""
import os
import numpy as np

def read_data():
    #read data from .txt files
    read_ingredients = []
    file = open("ingredients_output_data.txt", "r") 
    for index, line in enumerate(file): 
            read_ingredients.append(line.strip("\n"))
    
    read_instructions = []
    file = open("instruction_output_data.txt", "r") 
    for index, line in enumerate(file): 
            read_instructions.append(line.strip("\n"))
    
            
    read_total_times = []
    file = open("total_time_output_data.txt", "r") 
    for index, line in enumerate(file): 
            read_total_times.append(line.strip("\n"))
    
            
    read_titles = []
    file = open("title_output_data.txt", "r") 
    for index, line in enumerate(file): 
            read_titles.append(line.strip("\n"))
    
            
    read_urls = []
    file = open("url_data.txt", "r") 
    for index, line in enumerate(file): 
            read_urls.append(line.strip("\n"))
    
    #convert to pandas df     
    import pandas as pd
    data = {"url": read_urls,
            "title": read_titles,
            "total_time": read_total_times,
            "ingredients": read_ingredients,
            "instructions": read_instructions}
    recipe_df = pd.DataFrame.from_dict(data)
    
    #remove null values
    for col in recipe_df.columns:
        recipe_df = recipe_df[recipe_df[col] != "NULL"]
        
    #set index to url values
    recipe_df["index1"] = recipe_df.index
    recipe_df= recipe_df.set_index("url")
    
    return recipe_df

def get_preferences(df):
    
    #check if preferences.txt exists
    #create prefereces.txt with NULL Values
    if not os.path.isfile(os.getcwd().replace("\\","/") + "/preferences.txt"):
        with open("preferences.txt", "w") as output:
            for row in range(df.shape[0]):
                output.write("NULL"+"\n")
                
    #read preference.txt
    read_preferences = []
    file = open("preferences.txt", "r") 
    for index, line in enumerate(file): 
            read_preferences.append(line.strip("\n"))
            
    return read_preferences



def merge_data_and_pref(df, pref):
    df["preference"] = pref
    return df




def update_preferences(df):
    print("\nYou have chosen to update preferences...\n")
    print("To add a preference for a recipe (good, bad), follow the instructions...")
    
    #get url
    input_url = input("Please enter the url of the recipe (starting with 'https://www.'): ")
    
    #validate url exists in database
    while input_url.lower() not in df.index:
        print("\n" + input_url +"?")
        print("Invalid option")
        input_url = input("Please enter the url of the recipe (starting with 'https://www.'): ")
    
    #get preference
    input_pref = input("Please enter you preference for this recipe (good, bad):")
    
    #validate preference
    while input_pref.lower() not in ["good", "bad"]:
        print("\n" + input_pref +"?")
        print("Invalid option")
        input_pref = input("Please enter you preference for this recipe (good, bad):")
        
        
    #update df preference
    df.loc[input_url, "preference"] = input_pref
    
    #update preferences.txt
    with open("preferences.txt", "w") as output:
            for value in df.preference:
                output.write(value +"\n")
                
    #verify completion
    print("Preferences have been updated :)")
    
    return df
    
    

def evaluate_recipe(df):
    print("\nYou have chosen to evaluate a recipe...")
    
    #get url
    input_url = input("Please enter the url of the recipe (starting with 'https://www.'): ")
    
    #validate url exists in database
    while input_url.lower() not in df.index:
        print("\n" + input_url +"?")
        print("Invalid option")
        input_url = input("Please enter the url of the recipe (starting with 'https://www.'): ")
        
    #get classifier
    clf = get_classifier(df)
    
    #make prediction
    X_test = [df.loc[input_url].ingredients]
    predicted = clf.predict(X_test)
    prob = clf.predict_proba(X_test)  
    
    #Print results
    print("Predicted:", predicted)
    print("Classes:", clf.classes_)
    print("Probability:", prob)
        
  
    
    return None


def get_classifier(df):
    #create classifier pipeline and return classifier pipline 
    from sklearn.feature_extraction.text import TfidfVectorizer
    from sklearn.pipeline import Pipeline
    from sklearn.naive_bayes import MultinomialNB
    
    #create test train set
    df = df[df.preference != "NULL"]
    X_train = df['ingredients']
    y_train = df.preference 
    
    #create pipeline
    tools = [('tf', TfidfVectorizer()), ('nb', MultinomialNB())]
    clf = Pipeline(tools)
    clf.set_params(tf__stop_words = 'english')
    
    #fit pipeline
    clf = clf.fit(X_train, y_train)
    
    return clf
    
    
def recipe_rec(df):
    print("\nYou have chosen to get a recipe reccomendation...\n")
    

    from sklearn.feature_extraction.text import TfidfVectorizer
    
    #create tfidf matrix
    tfidf = TfidfVectorizer(stop_words = 'english').fit_transform(df.ingredients)
    
    #reset index
    df = df.reset_index()
    
    #filter data
    good_recipes_index = list(df[df.preference == "good"].index)
    
    #comparison index
    comparison_index = list(df[df.preference == "NULL"].index)
    
    #compute coside similarity
    #https://stackoverflow.com/questions/12118720/python-tf-idf-cosine-to-find-document-similarity
    from sklearn.metrics.pairwise import linear_kernel
    mean_cosine_similarities = np.mean(linear_kernel(tfidf[comparison_index], tfidf[good_recipes_index]), axis = 1)
    
    #find top 5 most closely related recipes
#    sorted_recipe_indices = mean_cosine_similarities.argsort()[:-5:-1]
    best_recipe_indices = mean_cosine_similarities.argsort()[-1]
    
    #pull urls of top 5 best index values
    best_title = df.iloc[best_recipe_indices].title
    best_url = df.iloc[best_recipe_indices].url
    
    #print results
    print("The best recipe for you is...")
    print("Title:", best_title)
    print("URL:", best_url)
    
    return None
    

    
def menu_choice():
    """ Find out what the user wants to do next. """
    print("\n********************************************")
    print("Choose one of the following options?")
    print("   1) Update preferences")
    print("   2) Evaluate a recipe")
    print("   3) Get a recipe reccomendation")
    print("   q) Quit")
    print("********************************************")
    choice = input("Choice: ") 
    if choice.lower() in ['1','2', '3', 'q']:
        return choice.lower()
    else:
        print(choice +"?")
        print("Invalid option")
        return None


def main_loop():
    
    # load data
    print("Reading Data...")
    df = read_data()
    

    #get preferences
    pref = get_preferences(df)


    #combine data and preferences
    df = merge_data_and_pref(df, pref)
    print("Your database has", df.shape[0], "recipes.")
#    print("This is a preview of the data....")
#    print(df.head())
#    print()
    
    while True:
        choice = menu_choice()
        if choice == None:
            continue
        if choice == 'q':
            print( "Exiting...")
            break     # jump out of while loop
        elif choice == '1':
            df = update_preferences(df)
        elif choice == '2':
            evaluate_recipe(df)
        elif choice == '3':
            recipe_rec(df)
        else:
            print("Invalid choice.")
            
    

# The following makes this program start running at main_loop() 
# when executed as a stand-alone program.    
if __name__ == '__main__':
    main_loop()