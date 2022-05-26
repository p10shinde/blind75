# Given an array of integers, return a new array for which every index carries
# the value of the product of the remaining elements



def getResults(input):
    op = []
    
    # Time -> O(n2)
    # for i in range(len(input)):
    #     currProd = 1
    #     for j in range(len(input)):#input[0:i] + input[i+1:]:
    #         if j != i:
    #             currProd *= input[j] # j
    #     op.append(currProd)
    # return op 

    # # Time -> O(n)
    # totalProd = 1
    # for val in input:  
    #     totalProd *= val
    # for val in input:
    #     op.append(int(totalProd/val))
    # return op

    # calculate left product array and right product array
    # multiply elements of these array left[i-1] * right[i+1]

    left_prod = [1] * (len(input) +2)
    right_prod = [1] * (len(input) + 2)
    c_left_prod, c_right_prod = 1, 1

    for i in range(len(input)):
        left_prod[i] = input[i] * left_prod[i-1]

    for j in range(len(input)-1, -1, -1):
        right_prod[j] = input[j] * right_prod[j+1]

    for i in range(0, len(right_prod)):
        op.append(left_prod[i-1] * right_prod[i+1])

    # print(left_prod)
    # print(right_prod)
    return op




input = [1,2,3,4,5]
# input = [4,10,3]
print(getResults(input))
