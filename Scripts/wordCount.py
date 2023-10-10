from datetime import date
import csv

today = date.today()
d1 = today.strftime("%d/%m/%Y")
number_of_words = 0

with open(r'analysis/main.txt','r',encoding="utf-8") as file:
 
    # Reading the content of the file
    # using the read() function and storing
    # them in a new variable
    data = file.read()
 
    # Splitting the data into separate lines
    # using the split() function
    
    lines = data.split()
    for i in reversed(range(len(lines))):
        if lines[i] == '.':
            lines.pop(i)
            
    number_of_words += len(lines)
    
out = [d1,number_of_words]

with open("analysis/wordcount.csv",'a',newline='') as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(out)