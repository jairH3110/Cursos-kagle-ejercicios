##################################################################################
#EJERCICIO 1
# Your code here
dtype = reviews.points.dtype

# Check your answer
q1.check()

#########################################################################################3
#EJERCICIO 2

point_strings = reviews.points.astype(str)

# Check your answer
q2.check()
#######################################################################################
#EJERCICIO 3
missing_price_reviews = reviews[reviews.price.isnull()]
n_missing_prices = len(missing_price_reviews)
# Cute alternative solution: if we sum a boolean series, True is treated as 1 and False as 0
n_missing_prices = reviews.price.isnull().sum()
# or equivalently:
n_missing_prices = pd.isnull(reviews.price).sum()

# Check your answer
q3.check()
##################################################################################################
#EJERCICIO4
reviews_per_region = reviews.region_1.fillna('Unknown').value_counts().sort_values(ascending=False)
######################################################################################################
