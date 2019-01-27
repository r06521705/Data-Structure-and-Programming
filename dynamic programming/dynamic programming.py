############################################
#   107-1 Data Structure and Programming
#   Programming Assignment #2
#   Instructor: Pei-Yuan Wu
############################################

import sys

lookup_table = {}
logic_table = {}
    
for i in range(10):
    lookup_table[str(i)] = 1
    logic_table[str(i)] = 1
    
for i in range(10 , 100):
    lookup_table[str(i)] = 2
    logic_table[str(i)] = 2

lookup_table['100'] = 3
lookup_table[''] = 1
logic_table['100'] = 3
logic_table[''] = 1
#lookup_table
# **********************************
# *  TODO                          *
# **********************************
def solution(input_string):
    total = 0
    if input_string in lookup_table:
        #print(lookup_table[input_string] , input_string , 'base')
        return lookup_table[input_string]
    
    else:
        #temp = 0
        for i in range(1,4):
            head_string = input_string[:i]             #1234 分成 1 搭配 f(234) ==> 在丟到下一個recursive
            cursive_string = input_string[i:]          #          12 搭配 f(34) ==> 在look_up table有 ==> done
            if head_string in logic_table:             #          123 搭配 f(4) 但這一項刪掉，不合理
                total += solution(cursive_string)      # 00 ,05 , 004這種不合理的會被 if 那行擋掉
                #temp += solution(cursive_string)
    lookup_table[input_string] = total
    #print(total , input_string ,'new')
    return total

# **********************************
# *  Do NOT modify the code below  *
# **********************************
if __name__ == '__main__':
    # 1. Check the command-line arguments
    if len(sys.argv) != 3:
        sys.exit("Usage: python3 programming_hw2.py <input> <output>")
    
    # 2. Read the input file
    inFile = open(sys.argv[1], 'r')
    input_list = list(inFile.read().splitlines())
    inFile.close()
    # print(input_list)

    # 3. Solve
    answer_list = [ solution(s) for s in input_list ]
    # print(answer_list)

    # 4. Output answers
    outFile = open(sys.argv[2], 'w')
    for ans in answer_list:
        outFile.write('{}\n'.format(ans))
    outFile.close()
