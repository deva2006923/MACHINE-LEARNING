code:
   salary = {
    "Ravi":45000,
    "Priya":55000,
    "Arjun":70000
  }

  s = pd.Series(salary,index=["name","sal"])

  print(s)



output:
   name   NaN
   sal    NaN
   dtype: float64
