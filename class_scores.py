##
## class_scores.py
# sophie the lord
# 02/03/2023

# lits
class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

# combine list
combined_list = class_a + class_b

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

