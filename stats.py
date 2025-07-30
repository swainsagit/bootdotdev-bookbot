# function is counting all the words 
def count_number_of_words(text_words):
    count = text_words.split()
    sum = 0
    for i in count:
        sum += 1
    return sum

# counts all the individual characters
# returns a dictionary of String, Integer 
def character_count(text_words):
    character_lower = text_words.lower()
    character_dict = {}
    for i in character_lower:
        if i in character_dict:
            character_dict[i] +=1
        else:
            character_dict[i] = 1
    return (character_dict)

# this will access each dictionary value 
# (list of dictionaries)
def sort_on(mylist):
    return mylist["num"] 


# this function is taking in a dictionary of characters
# and the counts, iterates through the dictionary adding each 
# to a new list which becomes a list of dictionaries for 
# each character, its checking if the characters are alphanumeric
# and then sorting from the highest sum of totals occurances 
def report_func(total):
    mylist = []
    for letter,sum in total.items():
        if letter.isalpha():
            mydict = {"char":letter, "num":sum }
            mylist.append(mydict)
    mylist.sort(reverse=True, key=sort_on)
    return (mylist)




    