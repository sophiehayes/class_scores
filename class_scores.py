##
## class_scores.py
# sophie
# 02/03/2023

# lsits
class_a = [44, 33, 28, 47, 12, 28, 32, 31, 11, 39, 40, 26, 36]
class_b = [19, 26, 38, 31, 30, 42, 44, 14, 27, 43, 46, 49, 24, 26, 36]

# combine list
combined_list = class_a + class_b
count = 0
total_score = 0
for classes in combined_list:
    count += 1
    total_score += combined_list
    

# mean
print("the mean is {}".format(total_score/count))
