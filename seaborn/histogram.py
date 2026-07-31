code:
  import seaborn as sns
  import matplotlib.pyplot as plt
  import pandas as pd
  m = [45,50,52,55,60,61,65,68,70,72,75,80,85,90]
  sns.histplot(x=m,bins=10,kde=True,color="black",edgecolor="black")
  plt.show()
