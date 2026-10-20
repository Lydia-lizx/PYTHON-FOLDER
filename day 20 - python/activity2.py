#initialize dictionary
test_dict = {'Codingal' : 2, 'is' : 2, 'best' : 2, 'for' : 2, 'Coding' : 1}
#printing original dictionary
print("The original dictionary is : " + str(test_dict))
#initialize value
k = 2
#using loop
#selecting key values in dictionaries
res = 0 
for key in test_dict:
    if test_dict[key] == k:
        res += 1
print("frequency of", k, "in dictionary is : " + str(res))