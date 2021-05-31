import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv("data.csv", sep=";")

wykryte = data["wykryte"]
niewykryte = data["niewykryte"]
nienaprawialne = data["nienaprawialne"]
bledy = data["bledy"]

# print(data.head())

BINS = 21 # int(((max(wykryte) - wykryte.min())/20).round())

fig0, ax0 = plt.subplots()
# C17767
# 2B4162
# 053C5E
# 064A74
# 454B66
# 677DB7
counts, bins, patches = ax0.hist(wykryte, bins=BINS, rwidth=0.90, color="#014f86")

ax0.set_xticks(bins.round())
plt.setp(ax0.xaxis.get_majorticklabels(), rotation =70)

fig0.suptitle("Histogram błędów wykrytych")
ax0.set_xlabel("Wartości błędów wykrytych", labelpad=10)
ax0.set_ylabel("Częstotliwość")

for c, b, p in zip(counts, bins, patches):
    ax0.text(b+4.5, c+4, str(int(c)), rotation=90)

ylims = ax0.get_ylim()
ax0.set_ylim([ylims[0], ylims[1]*1.06])

fig0.tight_layout()

fig0.savefig("wykryte.png", dpi=300)

fig1, ax1 = plt.subplots()
# C17767
# 2B4162
# 053C5E
# 064A74
# 454B66
# 677DB7
counts1, bins1, patches1 = ax1.hist(niewykryte, bins=11, rwidth=0.90, color="#01497c")

ax1.set_xticks(bins1.round())
plt.setp(ax1.xaxis.get_majorticklabels(), rotation =70)

fig1.suptitle("Histogram błędów niewykrytych")
ax1.set_xlabel("Wartości błędów niewykrytych", labelpad=10)
ax1.set_ylabel("Częstotliwość")

for c, b, p in zip(counts1, bins1, patches1):
    ax1.text(b + 0.35, c + 5, str(int(c)), rotation=90)

ylims = ax1.get_ylim()
ax1.set_ylim([ylims[0], ylims[1]*1.06])

fig1.tight_layout()

fig1.savefig("niewykryte.png", dpi=300)

plt.show()

fig2, ax2 = plt.subplots()
counts2, bins2, patches2 = ax2.hist(nienaprawialne, bins=12, rwidth=0.90, color="#013a63")

ax2.set_xticks(bins2.round())
plt.setp(ax2.xaxis.get_majorticklabels(), rotation =70)

fig2.suptitle("Histogram błędów nienaprawalnych")
ax2.set_xlabel("Wartości błędów nienaprawalnych", labelpad=10)
ax2.set_ylabel("Częstotliwość")

for c, b, p in zip(counts2, bins2, patches2):
    ax2.text(b + 2.5, c + 5, str(int(c)), rotation=90)

ylims = ax2.get_ylim()
ax2.set_ylim([ylims[0], ylims[1]*1.06])

fig2.tight_layout()

fig2.savefig("nienaprawialne.png", dpi=300)

plt.show()


fig3, ax3 = plt.subplots()
counts3, bins3, patches3 = ax3.hist(bledy, bins=13, rwidth=0.90, color="#012a4a")

ax3.set_xticks(bins3.round())
plt.setp(ax3.xaxis.get_majorticklabels(), rotation =70)

fig3.suptitle("Histogram błędów")
ax3.set_xlabel("Wartości błędów", labelpad=10)
ax3.set_ylabel("Częstotliwość")

for c, b, p in zip(counts3, bins3, patches3):
    ax3.text(b + 11, c + 5, str(int(c)), rotation=90)

ylims = ax3.get_ylim()
ax3.set_ylim([ylims[0], ylims[1]*1.06])

fig3.tight_layout()

fig3.savefig("bledy.png", dpi=300)

plt.show()