"""
Jun Seob Shim
On Liberation Final Project
Word Analysis
"""
#ask for and establish file title from user
title = input("Enter article name to read: ")

article = title + ".txt"

#open file, read data, then close
file = open(article,"r",errors ="ignore")
alldata = file.read()

file.close()

#empty string for breaking down long string
rawtext = ""

#translate string to string of pure lowercase words
for i in alldata:
    if (i.isalnum() == True) or (i == " "):
        rawtext += i.lower()

#split long string into list by spaces
wordslist = rawtext.split(" ")

#empty lists for unique words and frequency
uniquewords = []
frequency = []

#iterate through long list of words
for j in range(len(wordslist)):

    #if the word is new
    if (wordslist[j] in uniquewords) == False:
        #add to unique list, and add counter
        uniquewords.append(wordslist[j])
        frequency.append(1)

    #if the word isn't new
    else:
        #add 1 to frequency
        frequency[uniquewords.index(wordslist[j])] += 1

#create sorted frequency list
sortedfrequency = frequency.copy()
sortedfrequency.sort()
sortedfrequency.reverse()

#create empty list for reordered words
sortedwords = []

#iteratre through frequencies from high to low
for a in sortedfrequency:
    #iterate through unsorted frequencies
    for b in frequency:
        #if the two are equal
        if a == b:
            #add the word in the corresponding position to the list
            position = frequency.index(b)
            sortedwords.append(uniquewords[position])

            #delete the frequency and the word from the lists
            del uniquewords[position]
            del frequency[position]

            #break and move onto next iteration
            break

#establish and create table file
tabletitle = title + "table.csv"
table = open(tabletitle,"w")

#write statistics (unique word and frequency) to file
for k in range(len(sortedwords)):
    table.write(sortedwords[k])
    table.write(",")
    table.write(str(sortedfrequency[k]))
    table.write("\n")

#close file
table.close()
