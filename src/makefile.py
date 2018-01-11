##     |    MakroBox    |     ##
## Brute-Force List Generator ##
##            |  |            ##
from sys import argv
from os import path
from options import optionsList

def generate(name = False):
    if (name == False): return False
    file = open(name, 'w+')
    chars, length = optionsList['chars'], optionsList['length']
    index = [0 for i in range(length)]
    ##
    generatedNum = 0
    while True: #while we haven't generated all the codes
        generatedNum += 1
        now = "".join([chars[i] for i in index]) #current code
        file.write(now + '\n') #write the current code into the file
        print(now) #print the current code
        if sum(index)/length == len(chars)-1: break #have we checked all the codes?
        index[length-1] += 1 #change the index
        while max(index) >= len(chars):
            mi = index.index(max(index))
            index[mi] = 0
            index[mi-1] += 1
    print('Number of generated codes:', generatedNum)
    file.close()
    return True

if len(argv) >= 2:
    fileName = argv[1]
    success = generate(fileName)
else:
    print('Usage:', path.basename(__file__), '<path to the generated file>')
