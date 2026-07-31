code:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="dark",palette="colorblind")
df = pd.DataFrame({
    "Age": [25, 30, 35, 40],
    "c": [180, 190, 210, 220],
    "hd": ["No", "No", "No", "Yes"]})
sns.barplot(data=df,x="hd",y="Age",hue="hd",palette="dark")
plt.plot()
