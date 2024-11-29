import subprocess
from datetime import datetime
import matplotlib.pyplot as plt
import csv

def run_git_command(command):
    result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
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
    
    # Skip workflow-related commits
    if any(keyword.lower() in commit_message.lower() for keyword in workflow_keywords):
        continue

    files_changed = run_git_command(['git', 'show', '--name-only', '--pretty=format:', commit_hash]).splitlines()

    wc = 0
    try:
        with open('analysis/main.txt', 'r', encoding='utf-8') as f:
            file_text = f.read()
            words = [word for word in file_text.split() if not word.isdigit()]  # Exclude numbers
            wc = len(words)
    except FileNotFoundError:
        print(f"File 'analysis/main.txt' not found in commit {commit_hash}. Skipping.")

    # Update the dictionary with the cumulative word count for the date
    if date_str not in date_wc_dict:
        date_wc_dict[date_str] = 0
    date_wc_dict[date_str] = max(date_wc_dict[date_str], wc)

    print(date_str, wc)
    break

run_git_command(['git', 'checkout', 'main'])