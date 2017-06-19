#!/usr/bin/env python3

# Word Count Tool using RegEx
# Max Messenger Bouricius
# June 2017
# Counts the words each individual character speaks in a given play's script using RegEx commands to discern
# between characters, spoken lines, and initial scene setup.
# Tools: Python 3.

import re, argparse, csv

def addWordToCharDict(charDict, line):
# given pre-processed line and character's own dictionary (word | freq),
# parses line into separate strings, iterates through, and assigns each word to appropriate dict freqs
    wordList = line.split()
    for word in wordList:
        if (word not in charDict):
            charDict[word] = 1
        else:
            charDict[word] += 1

def printContents(charFullDict):
# puts contents of charFullDict into a neat and tidy console output
    totalCount = 0              # total words spoken by any character at all
    for character in sorted(charFullDict):
        print("Words spoken by", character + ":")
        totalCharWords = 0      # total words spoken by current character
        for word in sorted(charFullDict[character]):
            maxLengthWord = max(charFullDict[character])
            lineToPrint = '{:<18} {:<3}'.format("    " + word, charFullDict[character][word]) 
            print(lineToPrint)
            totalCharWords += charFullDict[character][word]
            totalCount += charFullDict[character][word]
        print("    Total words spoken by", character + ":", totalCharWords, "\n")
    print("Global total words spoken:", totalCount, "\n")

def writeToCSV(charFullDict, fname):
# writes contents of charFullDict to an external CSV file of name fname without using CSV mode
    with open(fname, 'w') as outFile:
        for character in sorted(charFullDict):
            for word in sorted(charFullDict[character]):
                lineToWrite = character + "," + word + "," + str(charFullDict[character][word]) + "\n"
                outFile.write(lineToWrite)
    print("CSV successfully written.")
    outFile.close()

def numExceptions(regex):
    # returns number of exceptions in given regex statement
    return re.compile(regex).groups

def main():
    # ***INITIALIZE ARGUMENTS***
    parser = argparse.ArgumentParser(description='Wordcount tool for theatrical scripts.')
    parser.add_argument(dest='filename', metavar='FILENAME', type=str, help='input name of file to parse.')
    args = parser.parse_args()

    # ***INITIALIZE LISTS AND VARIABLES***
    # charFullDict = dictionary for individual unique characters
        # each key's value is another dictionary of format dict[word][frequency of said word for said character]
    # currentChar = which character is currently speaking
        # initialized as null so program doesn't erroneously scan text before the first character speaks
    charFullDict = {}
    currentChar = ""

    # ***INITIALIZE REGEX STATEMENTS***
    punct = re.compile("[.,?!:;\"]|\[|\]")
    punct2 = re.compile("'(\w+)'")
    dash = re.compile("--")
    spoken = re.compile("^\s+(.+)")

    # open file, scan line by line
    with open(args.filename, 'r') as file1:
        for i, line  in enumerate(file1):
            # clean up line being read in
            modifiedLine = re.sub(punct, "", line)                  # remove punctuation
            modifiedLine = re.sub(dash, " ", modifiedLine)          # remove -- dash, replace with space
            quoteException = re.search(punct2, modifiedLine)
            if (quoteException):
                # while still exception groups to go
                modifiedLine = re.sub(punct2, quoteException.group(1), modifiedLine)
            characterLine = re.search("^(\w+)$\n", modifiedLine)
            modifiedLine = re.sub("\n", "", modifiedLine)           # remove endline
            spokenLine = re.search(spoken, modifiedLine)
            # if not character name, make lowercase and add to relevant dictionary
            if (spokenLine) and (currentChar):
                spokenLine = spokenLine.group(1)
                spokenLine = spokenLine.lower()
                addWordToCharDict(charFullDict[currentChar], spokenLine)
            # else (if character name), only make lowercase
            elif (characterLine):
                characterLine = characterLine.group(1)
                characterLine = characterLine.lower()
                currentChar = characterLine
                # if character doesn't already exist in charFullDict, then initialize dict for said character
                if (currentChar not in charFullDict):
                    charFullDict[currentChar] = {}
    printContents(charFullDict)
    # write contents to wordcount.csv, then close file
    writeToCSV(charFullDict, 'wordcount.csv')
    file1.close()

if __name__ == "__main__":
    main()
