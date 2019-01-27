############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #5
#   Instructor: Pei-Yuan Wu
############################################

import sys

# **********************************
# *  TODO                          *
# **********************************

def quick_sort(list): 
    smaller = []
    bigger = []
    keylist = []

    if len(list) <= 1:
        return list

    else:
        key = list[0] 
        for i in list:
            if i < key: 
                smaller.append(i)
            elif i > key: 
                bigger.append(i)
            else:
                keylist.append(i)

    smaller = quick_sort(smaller)
    bigger = quick_sort(bigger)
    return smaller + keylist + bigger

def solution(k, list_):


    list_sort = quick_sort(list_)
    #print(list_sort)
   
    res = 999999999
  
    n = len(list_sort)

    for i in range((n - k) + 1): 
        difference = list_sort[i + k - 1] - list_sort[i] 
        res = min(res, difference) 
    print(res)  
    return res 
    
# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw5.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()

    # 3. Solve
    input_k = int(input_list[0])
    input_set = input_list[1].split(',')
    input_set = [ int(s) for s in input_set ]
    answer = solution(input_k, input_set) 

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    outFile.write(str(answer))
    outFile.close()