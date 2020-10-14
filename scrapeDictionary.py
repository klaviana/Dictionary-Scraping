# -*- coding: utf-8 -*-
import csv

txt_file = r"dictionary.txt"
csv_file = 'dictionary.csv'

with open(txt_file) as in_txt, open(csv_file, 'w') as out_csv:
    out_csv.write("Word,Disambiguation,Part of Speech,Definition\n") # Write the header
    csvwriter = csv.writer(out_csv)
    previous = next(in_txt)
    for line in in_txt:
        if len(previous.strip()) == 0 and line.isupper() and line.count('***') < 1: # We have arrived at a new word
            disambiguation = partofspeech = etymology = definition = notes = ''
            nextline = next(in_txt)
            for element in range(0, len(nextline)): # Determine if there is disambiguation
                if nextline[element] == ',':
                    break
                if nextline[element] == ' ': 
                    disambiguation = ''
                    break
                disambiguation += nextline[element]
            if (nextline.count(' n. ') > 0): partofspeech = 'n.' # Determine the part of speech if listed --> kind of hacky with the if statements..
            if (nextline.count(' a. ') > 0): partofspeech = 'a.'
            if (nextline.count(' v. ') > 0): partofspeech = 'v.'
            if (nextline.count(' prep. ') > 0): partofspeech = 'prep.'
            if (nextline.count(' adv. ') > 0): partofspeech = 'adv.'
            while (definition == ''): # Iterate ensuing lines until we come to the definition
                if (nextline.count('Defn: ') > 0):
                    definition = nextline
                    definition = definition[6:] # splice out the "Defn: "
                    break
                nextline = next(in_txt)
            csvwriter.writerow([line, disambiguation, partofspeech, definition]) # Write to csv
        previous = line



'''
Chronological Notes:

My first roadblock was identifying the word. The definitions are easy to identify, since they follow "Defn: ".
However the words themselves are just written. I identified some qualities that set them apart: 
Preceded by an empty line, being only letters, and being all uppercase.

It took me a little while to figure out how to identify those preceding empty lines. I ended up creating
a variable to hold the previous line, and if its length was 0 after removing whitespace, I concluded it was empty.

My next roadblock was identifying whether there is a disambiguation, as some words have them while others do not.
I decided on the case that if a comma comes before a space in the next line, then there is a disambiguation.

My next challenge was determining part of speech. One option was to continue with string manipulation in the
second line like I did for determining disambiguation, but I opted instead to simply check for the specific 
parts of speech since there are so few. 

The next hurdle was scraping for definition. It was easy to throw all the definitions in a csv file by searching
for "Defn: ", however the challenge becomes the fact that the definition occurs in a non-predetermined number of 
lines after the word, while the disambiguation and part of speech both occurred in the line after the word. I chose
to search the ensuing lines until I found "Defn:". 
'''



'''
Final Thoughts:

I didn’t break up the function into smaller functions, mainly because I went over the suggested time limit. 
I would have to think about the best way to do it with the way the program is checking lines sequentially, 
but if I were to continue on this project, that would be one the first things I tackle.

There is room for improvement in regards to efficiency. I do a lot of searching with if statements and for
loops for each type of data I am extracting, and a few of them could probably be combined together seeing 
as the same lines are getting iterated multiple times.

I accounted for edge cases where possible. The first and last words both end up in the csv properly. That said, 
it seems like there are a lot of intricacies within this dictionary, so I assume there are areas where my 
algorithms do not perfectly catch them. My part of speech does not 

'''