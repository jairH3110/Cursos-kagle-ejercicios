##################################################################################
#EJERCICIO 1
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruits.
fruits = pd.DataFrame({'Apples':[30],'Bananas':[21]})

# Check your answer
q1.check()
fruits


#########################################################################################3
#EJERCICIO 2
# Your code goes here. Create a dataframe matching the above diagram and assign it to the variable fruit_sales.
fruit_sales = pd.DataFrame({'Apples':[35,41],'Bananas':[21,34]},index=['2017 Sales','2018 Sales'])

# Check your answer
q2.check()
fruit_sales



#######################################################################################
#EJERCICIO 3
ingredients = pd.Series(['4 cups' ,'1 cup','2 large','1 can'],index=['Flour','Milk','Eggs','Spam'],name='Dinner')

# Check your answer
q3.check()
##################################################################################################
#EJERCICIO 4
reviews = pd.read_csv('../input/wine-reviews/winemag-data_first150k.csv',index_col=0)

# Check your answer
q4.check()
reviews
######################################################################################################
#EJERCICIO5
# Your code goes here
animals.to_csv(cows_and_goats)
# Check your answer
q5.check()