##################################################################################
#EJERCICIOS 0
a = ""
length = 0
#q0.a.check()
#######################
b = "it's ok"
length = 7
#q0.b.check()
#############################
c = 'it\'s ok'
length = 7
#q0.c.check()
#######################
d = """hey"""
length = 3
#q0.d.check()
#####################################
e = '\n'
length = 1
#q0.e.check()
#################################
#EJERCICIO1 
def is_valid_zip(zip_code):
    """Returns whether the input string is a valid (5 digit) zip code
    """
    #help(str)
    a = str(zip_code)
    b= len(a)
    print(a)
    
    if b==5:
        
        c =str.isnumeric(a)
        return c 
     
    return False
    
    

# Check your answer
#q1.check()

#########################################################################################3
#EJERCICIO2
def word_search(doc_list, keyword):
    """
    Takes a list of documents (each document is a string) and a keyword. 
    Returns list of the index values into the original list for all documents 
    containing the keyword.

    Example:
    doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
    >>> word_search(doc_list, 'casino')
    >>> [0]
    """
   
    resultado = []
    palabra = keyword.lower()
    
    for i, doc in enumerate(doc_list):
        doc = doc.lower().replace(".", "").replace(",", "")
        words = doc.split()
         
        if palabra in words:
                resultado.append(i)
            
    return resultado

# Check your answer
#q2.check()
###########################################################################################
#EJERCICIO3
def multi_word_search(doc_list, keywords):
    """
    Takes list of documents (each document is a string) and a list of keywords.  
    Returns a dictionary where each key is a keyword, and the value is a list of indices
    (from doc_list) of the documents containing that keyword

    >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
    >>> keywords = ['casino', 'they']
    >>> multi_word_search(doc_list, keywords)
    {'casino': [0, 1], 'they': [1]}
    """
    resultado_bus = {}
    for keyword in keywords:
        ref = word_search(doc_list,keyword)
        resultado_bus[keyword]=ref
            
    return resultado_bus        
    pass

# Check your answer
#q3.check()

#######################################################################################

##################################################################################################

######################################################################################################
