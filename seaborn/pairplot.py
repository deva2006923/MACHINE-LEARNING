code:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="dark",palette="colorblind")
df = pd.DataFrame({
    "Age":[20,25,30,35],
    "BP":[120,130,140,150],
    "Cholesterol":[180,190,200,220],
    "Gender":["M","F","M","F"]
})
sns.pairplot(df);
