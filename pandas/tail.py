code:
    import pandas as pd
    c = pd.read_csv("/content/sample_data/california_housing_train.csv")
    print(c.tail(2))   #tail()-->it gives last record.... tail(n)--->last n records


output:
          longitude  latitude  housing_median_age  total_rooms  total_bedrooms  \
16998    -124.30     41.80                19.0       2672.0           552.0   
16999    -124.35     40.54                52.0       1820.0           300.0   

       population  households  median_income  median_house_value  
16998      1298.0       478.0         1.9797             85800.0  
16999       806.0       270.0         3.0147             94600.0  
