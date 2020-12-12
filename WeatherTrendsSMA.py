import pandas as pd 
import matplotlib.pyplot as plt

dfIstanbul = pd.read_csv("Istanbul.csv")
dfGlobal = pd.read_csv("Global.csv")

 

"Simple moving average at time period "
dfGlobal['SMA_5'] = dfGlobal.avg_temp.rolling(5, min_periods=1).mean() 
dfIstanbul['SMA_5'] = dfIstanbul.avg_temp.rolling(5, min_periods=1).mean()
plt.plot(dfIstanbul['year'],dfIstanbul['SMA_5'] ,label="5-years Istanbul SMA")
plt.plot(dfGlobal['year'],dfGlobal['SMA_5'] ,label="5-years Global SMA") 
 
plt.legend()
plt.title('Temperature in Istanbul and Global', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=16)

plt.show()

 