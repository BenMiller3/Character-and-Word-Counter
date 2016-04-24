"""
Counts the number of distinct words
within a text file
By: Benjamin D. Miller
"""
def wordCounter(filename):
    wordCount = 0
    charCount = 0
    file = open(filename,'r')
    for line in file.readlines():
        for i in range(len(line)):
            if(line[i]==" "): wordCount+=1
        charCount+=1
    ans = "\tTotal words: " + str(wordCount) + "\n\tTotal characters: " + str(charCount)
    return ans

def main():
    filename = in.next()
    wordCounter(filename)

if __name__ == '__main__':
    main()
    
