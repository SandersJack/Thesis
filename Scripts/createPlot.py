import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('analysis/wordcount.csv')

plt.rcParams['figure.constrained_layout.use'] = True

ax = df.plot(x="Date", y="WC")
ax.set_title("Word Count vs Date")
plt.savefig("analysis/WordcountVsDate.pdf", format="pdf", bbox_inches="tight")