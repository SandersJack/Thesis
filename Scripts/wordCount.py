from datetime import date
import csv

print("Calculating word count")
today = date.today()
d1 = today.strftime("%d/%m/%Y")
number_of_words = 0

with open(r'analysis/main.txt','r',encoding="utf-8") as file:
 
    data = file.read()
    
    lines = data.split()
    for i in reversed(range(len(lines))):
        if lines[i] == '.':
            lines.pop(i)

    for i in reversed(range(len(lines))):
        if lines[i].isdigit():
            lines.pop(i)

    with open("analysis/words.txt", "w", encoding="utf-8") as output_file:
        # Join the filtered words and write to the output file
        output_file.write(" ".join(lines))
            
    number_of_words += len(lines)
    
out = [d1,number_of_words]
print(d1,number_of_words)
with open("analysis/wordcount.csv",'a',newline='') as f:
    csv_writter = csv.writer(f)
    csv_writter.writerow(out)