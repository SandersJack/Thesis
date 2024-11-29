import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
import csv

def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    #print(f"Running command: {' '.join(command)}")
    #print(f"Output: {result.stdout}")
    #print(f"Error: {result.stderr}")
    return result.stdout.strip()

log_output = run_git_command(['git', 'log', '--pretty=format:"%ad %h %s"', '--date=short'])

commit_data = log_output.split("\n")

date_wc_dict = {}

workflow_keywords = ["Auto"]

for line in commit_data:
    parts = line.split()
    date_str = parts[0]  # The date part of the commit
    commit_hash = parts[1]  # The commit hash
    commit_message = " ".join(parts[2:])  # The commit message
    
    # Skip non workflow-related commits
    if any(keyword.lower() in commit_message.lower() for keyword in workflow_keywords):
        pass
    else:
        continue
    print(commit_hash)
    run_git_command(['git', 'checkout', commit_hash])

    wc = 0
    try:
        with open('analysis/main.txt', 'r', encoding='utf-8') as f:
            data = f.read()
    
            lines = data.split()
            for i in reversed(range(len(lines))):
                if lines[i] == '.':
                    lines.pop(i)

            for i in reversed(range(len(lines))):
                if lines[i].isdigit():
                    lines.pop(i)

            start_index = None
            for i, line in enumerate(lines):
                if "Chapter" in lines[i] and "1"in lines[i+1]:
                    start_index = i+1
                    break
            lines = lines[start_index:]

            #with open("analysis/words.txt", "w", encoding="utf-8") as output_file:
            #    # Join the filtered words and write to the output file
            #    output_file.write(" ".join(lines))
                    
            wc += len(lines)
    except FileNotFoundError:
        print(f"File 'analysis/main.txt' not found in commit {commit_hash}. Skipping.")
        continue

    formatted_date = datetime.strptime(date_str, "%Y-%m-%d").strftime("%d/%m/%Y")

    if formatted_date not in date_wc_dict:
        date_wc_dict[date_str] = 0
    date_wc_dict[date_str] = max(date_wc_dict[date_str], wc)

    print(date_str, wc)

run_git_command(['git', 'checkout', 'master'])

sorted_dates = sorted(date_wc_dict.keys())
sorted_wc = [date_wc_dict[date] for date in sorted_dates]

output_filename = "git_word_count_filtered.csv"
with open(output_filename, "w", newline='', encoding="utf-8") as csvfile:
    fieldnames = ["Date", "Cumulative WC"]
    writer = csv.writer(csvfile)
    
    writer.writerow(["Date", "Word Count"])

    for date, wc in date_wc_dict.items():
        writer.writerow([date, wc])

print(f"Cumulative word count data saved to {output_filename}")