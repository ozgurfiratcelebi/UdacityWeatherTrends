"""

istanbul verilerini  al
Dünyanın sıcaklık değerlerini al 
csv leri python ile açgrafiği dök
Şehriniz, küresel ortalamaya kıyasla ortalama olarak daha sıcak mı yoksa daha soğuk mu? Fark zaman içinde tutarlı oldu mu?
Şehrinizin sıcaklıklarındaki zaman içindeki değişimler, küresel ortalamadaki değişikliklerle karşılaştırıldığında nasıl?
Genel eğilim neye benziyor? Dünya daha da ısınıyor mu, soğuyor mu? Trend, son birkaç yüz yılda tutarlı oldu mu?

"""


import pandas as pd 
import matplotlib.pyplot as plt

dfIstanbul = pd.read_csv("Istanbul.csv")
dfGlobal = pd.read_csv("Global.csv")

 
 plt.plot(dfIstanbul['year'],dfIstanbul['avg_temp'] ,label="Istanbul Data") 
 plt.plot(dfGlobal['year'],dfGlobal['avg_temp'] ,label="Global Data")  

 

plt.legend()
plt.title('Temperature in Istanbul and Global', fontsize=20)
plt.xlabel('Year', fontsize=16)
plt.ylabel('Temperature [°C]', fontsize=16)

plt.show()

 