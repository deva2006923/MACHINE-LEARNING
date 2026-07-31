code:
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
sns.set_theme(style="dark",palette="colorblind")
df = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
    "Sales": [100, 120, 150, 130, 170]
})
sns.lineplot(data=df,x="Month",y="Sales")
