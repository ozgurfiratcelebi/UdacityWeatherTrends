 
import pandas as pd 
import matplotlib.pyplot as plt

dfIstanbul = pd.read_csv("Istanbul.csv")
dfGlobal = pd.read_csv("Global.csv")

dfGlobal['exp'] = dfGlobal.avg_temp.expanding().mean() 
dfIstanbul['exp'] = dfIstanbul.avg_temp.expanding().mean()
plt.plot(dfIstanbul['year'],dfIstanbul['exp'] ,label=" Expanding Istanbul  ")
plt.plot(dfGlobal['year'],dfGlobal['exp'] ,label="Expanding  Global  ") 
 

plt.legend()
plt.title('Temperature in Istanbul and Global', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=16)

plt.show()

 