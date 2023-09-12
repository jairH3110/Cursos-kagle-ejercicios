##################################################################################
#EJERCICIO 1
median_points = reviews['points'].median()

# Check your answer
q1.check()


#########################################################################################3
#EJERCICIO2
countries = reviews['country'].unique()

# Check your answer
q2.check()


#######################################################################################
#EJERCICIO 3
reviews_per_country =reviews['country'].value_counts()

# Check your answer
q3.check()
##################################################################################################
#EJERCICIO 4
centered_price =reviews['price'] - reviews['price'].mean()
# Check your answer
q4.check()
######################################################################################################
#EJERCICIO5
centered_price =reviews['price'] - reviews['price'].mean()
# Check your answer
q4.check()

#######################################################################################################3
#EJERCICIO 6
tropical = reviews.description.map(lambda desc: "tropical" in desc).sum()
fruity = reviews.description.map(lambda desc: "fruity" in desc).sum()
descriptor_counts = pd.Series([tropical, fruity], index=['tropical', 'fruity'])

# Check your answer
q6.check()
#############################################################################################
#EJERCICIO 7
def stars(row):
    if row.country == 'Canada':
        return 3
    elif row.points >= 95:
        return 3
    elif row.points >= 85:
        return 2
    else:
        return 1

star_ratings = reviews.apply(stars, axis='columns')

# Check your answer
q7.check()