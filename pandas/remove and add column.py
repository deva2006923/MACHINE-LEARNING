code:
  import pandas as pd
  c = pd.read_csv("/content/sample_data/california_housing_train.csv")
  ho=c.pop("households")
  print(ho)
  c["households"]=ho
  print(c["households"])


output:
0        472.0
1        463.0
2        117.0
3        226.0
4        262.0
         ...  
16995    369.0
16996    465.0
16997    456.0
16998    478.0
16999    270.0
Name: households, Length: 17000, dtype: float64



0        472.0
1        463.0
2        117.0
3        226.0
4        262.0
         ...  
16995    369.0
16996    465.0
16997    456.0
16998    478.0
16999    270.0
Name: households, Length: 17000, dtype: float64



