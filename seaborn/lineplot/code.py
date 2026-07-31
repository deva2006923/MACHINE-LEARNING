code:
  import seaborn as sns
  import matplotlib.pyplot as plt
  import pandas as pd
  sns.set_theme(style="dark",palette="colorblind")  #this used to set theme for all  there are two parameters style=controls the background and grid appearence of graph......,palette=""....colection of colors
  sns.lineplot(x=[1,2,3],y=[2,4,6])
  plt.show()
