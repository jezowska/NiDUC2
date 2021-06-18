from matplotlib.patches import Patch
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv(
    r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\szum09\Dane_szum09.csv", sep=";")

wykryte = data["wykryte"]
nienaprawione = data["nienaprawialne"]
niewykryte = data["niewykryte"]
bledy = data["bledy"]

fig1, ax1 = plt.subplots()

fig1.suptitle("Wykres pudelkowy bledow wykrytych dla ciagu 25000 bitow, z 9% szansą na zaszumienie bitu")
ax1.boxplot(wykryte, boxprops=dict(color='#000000'), medianprops=dict(
    color='#000000'), patch_artist=True, vert=False)
fig1.set_figheight(3.8)
ax1.axes.yaxis.set_visible(False)

fig1.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\szum09\wykryte.png", dpi=300)

fig2, ax2 = plt.subplots()

fig2.suptitle("Wykres pudelkowy bledow nienaprawionych dla ciagu 25000 bitow, z 9% szansą na zaszumienie bitu")
ax2.boxplot(nienaprawione, boxprops=dict(color='#000000'),
            medianprops=dict(color='#000000'), patch_artist=True, vert=False)
ax2.axes.yaxis.set_visible(False)
fig2.set_figheight(3.8)

fig1.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\szum09\nienaprawione.png", dpi=300)

fig3, ax3 = plt.subplots()

fig3.suptitle("Wykres pudelkowy bledow niewykrytych dla ciagu 25000 bitow, z 9% szansą na zaszumienie bitu")
ax3.boxplot(niewykryte, boxprops=dict(color='#000000'), medianprops=dict(
    color='#000000'), patch_artist=True, vert=False)
ax3.axes.yaxis.set_visible(False)
fig3.set_figheight(3.8)

fig1.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\szum09\niewykryte.png", dpi=300)

fig4, ax4 = plt.subplots()

fig4.suptitle("Wykres pudelkowy bledow dla ciagu 25000 bitow, z 9% szansą na zaszumienie bitu")
ax4.boxplot(bledy, boxprops=dict(color='#000000'), medianprops=dict(
    color='#000000'), patch_artist=True, vert=False)
ax4.axes.yaxis.set_visible(False)
fig4.set_figheight(3.8)

fig4.savefig(r"C:\Users\socze\OneDrive\Documents\GitHub\NiDUC2\pudelkowe\szum09\bledy.png", dpi=300)

plt.show()
