import pandas as pd  

dfIstanbul = pd.read_csv("Istanbul.csv")
dfGlobal = pd.read_csv("Global.csv") 
 

maxNumber = max(dfIstanbul['avg_temp'])
minNumber = min(dfIstanbul['avg_temp'])

maxNumberGlobal = max(dfGlobal['avg_temp'])
minNumberGlobal = min(dfGlobal['avg_temp'])

 
print("maxNumber: {0}" .format( maxNumber))
print("minNumber:{0}" .format( minNumber))
print("maxNumberGlobal:{0}" .format( maxNumberGlobal))
print("minNumberGlobal:{0}" .format( minNumberGlobal))

 

 

