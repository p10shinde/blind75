# Given a string, find its first non-repeating character

def getResult(input):
    input_len = len(input)
    for index, chr in enumerate(input):
        if chr not in input[index+1:input_len]:
            return chr

print(getResult('geeksforgeeks'))
# inp = 'geeksforgeeks'
# print(inp.index('e'))
# print(inp[1:2] )

