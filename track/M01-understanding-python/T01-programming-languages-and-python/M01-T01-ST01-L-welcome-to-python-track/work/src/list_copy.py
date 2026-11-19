# import copy
# original = [[1,2],[3,4]]
# s_copy = copy . copy(original)
# original[1][0] = 100
# print(original)
# print(s_copy)

# deep copy
import copy
original = [[1,2],[3,4]]
new_list = copy . deepcopy(original)
original[0][0] = 100
print(original)
print(new_list)