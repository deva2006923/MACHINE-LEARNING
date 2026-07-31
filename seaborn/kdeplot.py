code:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="dark",palette="colorblind")
m = [45,50,52,55,60,61,65,68,70,72,75,80,85,90]
sns.kdeplot(x=m,fill=False,color="black",linewidth=10)
plt.show()
