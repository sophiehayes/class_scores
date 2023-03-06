##
## class_scores.py
# sophie the lord
# 02/03/2023

# funtion for input

def user_input (user_score):
    '''
    user input to list
    '''
    combined_list.append(user_score)

    return user_score

def user_modify (number, insert):
    '''
    user modifys value in list
    '''
    combined_list.insert(number, insert)

    return number, insert
    
        
    
# lits
class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

# combine list
combined_list = class_a + class_b


# get user to add score and calc inside funtion
user_score = float(input("what score did you get? "))
user_input(user_score)

# print list
print(combined_list)

# get user to modify a value in list
user_choice = input("would you like to change a value in the list (y/n)? ").strip().lower()
if user_choice == "y":
    number = int(input("which number on the list is the value, count from 0: "))
else :
    print("wtf")

# get the insert variable
insert = int(input("what value would you like to add?"))

# call funtion and print new list
user_modify(number, insert)
print(combined_list)





# set variables
count = 0
total_score = 0

# create loop
for classes in combined_list:
    count += 1
    total_score += classes

    
# print mean
print("the mean is {:.2f} for both class lists combined".format(total_score/count))

# print max
print("the max score for both class lists combined is: ", max(combined_list))

# print min
print("the min score for both class lists combined is: ", min(combined_list))



