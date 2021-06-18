from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(
    r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\25k\25k.csv", sep=";")

wykryte = data["wykryte"]
nienaprawione = data["nienaprawialne"]
niewykryte = data["niewykryte"]
bledy = data["bledy"]

fig1, ax1 = plt.subplots()

fig1.suptitle("Wykres pudelkowy bledow dla ciagu 25000 bitow")
ax1.boxplot(wykryte, boxprops=dict(color='#000000'), medianprops=dict(
    color='#000000'), patch_artist=True, vert=False)
fig1.set_figheight(3.8)
ax1.axes.yaxis.set_visible(False)

fig1.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\25k\wykryte.png", dpi=300)

fig2, ax2 = plt.subplots()

fig2.suptitle("Wykres pudelkowy bledow nienaprawionych dla ciagu 25000 bitow")
ax2.boxplot(nienaprawione, boxprops=dict(color='#000000'),
            medianprops=dict(color='#000000'), patch_artist=True, vert=False)
ax2.axes.yaxis.set_visible(False)
fig2.set_figheight(3.8)

fig2.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\25k\nienaprawione.png", dpi=300)

fig3, ax3 = plt.subplots()

fig3.suptitle("Wykres pudelkowy bledow niewykrytych dla ciagu 25000 bitow")
ax3.boxplot(niewykryte, boxprops=dict(color='#000000'), medianprops=dict(
    color='#000000'), patch_artist=True, vert=False)
ax3.axes.yaxis.set_visible(False)
fig3.set_figheight(3.8)

fig3.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\25k\niewykryte.png", dpi=300)

fig4, ax4 = plt.subplots()

fig4.suptitle("Wykres pudelkowy bledow dla ciagu 25000 bitow")
ax4.boxplot(bledy, boxprops=dict(color='#000000'), medianprops=dict(
    color='#000000'), patch_artist=True, vert=False)
ax4.axes.yaxis.set_visible(False)
fig4.set_figheight(3.8)

fig4.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\25k\bledy.png", dpi=300)