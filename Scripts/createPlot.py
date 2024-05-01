import matplotlib.pyplot as plt
import pandas as pd

print("Creating Plot")
df = pd.read_csv('analysis/wordcount.csv')

plt.rcParams['figure.constrained_layout.use'] = True

df = df.drop_duplicates(subset='Date', keep="last")
df['Date'] = pd.to_datetime(df['Date'], format='%d/%m/%Y')
df.set_index('Date', inplace=True)

ax = df.plot(y="WC")
ax.set_title("Word Count vs Date")
plt.savefig("analysis/WordcountVsDate.pdf", format="pdf", bbox_inches="tight")

plt.show()