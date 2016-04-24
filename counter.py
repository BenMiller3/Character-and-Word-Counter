"""
Counts the number of distinct words
within a text file
By: Benjamin D. Miller
"""
import sys
import os

"""
Takes a file and counts the distict
words and characters within it
returns the concatenated string result
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

"""
Pass filename to be counted as the arguements
Checks it is a valid filename and then counts
"""
def main():
    if len(sys.arg) == 2:   # Argument passed should be filename
        filename = sys.arg[1]
        if not os.path.isfilename(filename):
            print(filename," does not exist on the system")
            exit(0)
        print("Counting words and characters in: ",filename,"\n")
    
    try:
        wordCounter(filename)
    except:
        print("Invalid file name")
        
if __name__ == '__main__':
    main()
    
