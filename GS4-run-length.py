# Run length encoding

def getResults(input):
    op = ''
    cntr = 1
    for i in range(len(input) - 1):
        if input[i+1] == input[i]:
            cntr += 1
        else:
            op += input[i] + str(cntr)
            cntr = 1
    op += input[i+1] + str(cntr)
    return op



input = "AACCCBBBBBAAAAFFFFFFFF"
print(getResults(input))