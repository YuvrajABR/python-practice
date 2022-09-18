"""
day 1 : 

    Python program to check if List containts consectuvie 3
    has_33([1, 3, 3]) --> True
    has_33([1, 3, 1, 3]) --> False
    has_33([3, 1, 3]) --> False
    has_33([3,3,1]) --> True
    
"""

def has_33(list_input):
    for i in range(0,len(list_input) - 1):
        if list_input[i:i+2] == [3,3]:
            return True
    else:
        return False

#test case 1
#result = has_33([1, 3, 3])

#test case 2
#result = has_33([1, 3, 1, 3])
    
#test case 3
#result = has_33([3, 1, 3])

#test case 4
result = has_33([3,3,1])    

print(result)