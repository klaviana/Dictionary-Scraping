import csv

txt_file = r"dictionary.txt"
csv_file = 'dictionary.csv'

with open(txt_file) as in_txt, open(csv_file, 'w') as out_csv:
    out_csv.write("Word,Disambiguation,Description,Definition,Example\n") # Write the header
    previous = next(in_txt)
    for line in in_txt:
        if len(previous.strip()) == 0 and line.isupper():
            out_csv.write(",".join(line.strip().split('\t')) + "\n")
        #if "Defn:" in line:
            #out_csv.write(",".join(line.strip().split('\t')) + "\n")
        previous = line

'''
Notes:

My first roadblock was identifying the word. The definitions are easy to identify, since they follow "Defn: ".
However the words themselves are just written. I identified some qualities that set them apart: 
Preceded by an empty line, being only letters, and being all uppercase.

It took me a little while to figure out how to identify those preceding empty lines. I ended up creating
a variable to hold the previous line, and if its length was 0 after removing whitespace, I concluded it was empty.

'''