Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import matplotlib.pyplot as plt
import pandas as pd

#Dataframe with all columns
df=pd.DataFrame({
	'Apprx. 5000 Venezuelans Interiorized in Brazil' : [503,75,267,21,190,248,75,244,545,268,283,102,918,117,482,877,35],
	'Brazil States' : ['Amazonas','Bahia','Federal District','Goiás','Mato Grosso','Mato Grosso do Sul','Minas Gerais','Paraíba','Paraná','Pernambuco','Rio de Janeiro','large northern river','Rio Grande do Sul','Rondônia','Santa Catarina','Sao Paulo','Sergipe']})

#Sorting for Interiorized people bar chart
df_sorted=df.sort_values(by='Apprx. 5000 Venezuelans Interiorized in Brazil',ascending=False)

#Plot horizontal bar chart
df_sorted.plot(kind='barh',y='Apprx. 5000 Venezuelans Interiorized in Brazil',x='Brazil States')

plt.show()
