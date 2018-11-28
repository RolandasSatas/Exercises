#pip install pandas
#pip install xlrd

import pandas as pd

#Basisdata_0000_Norge_25833_Postnummeromrader_SOSI_Postnummerområde_FLATE.dbf was converted to file.xslx for expediency, maybe not best way but a quick workaround
filename = r'file.xlsx'
df = pd.read_excel(filename)

#print(df)
#print(df) can be used preview file if needed

#on excel file I can filter 3273 unique postal codes, same seen with below simple commands

answer = df.nunique()
print(answer)

#for GeoPandas related work I keep having issue with pip installer bug, unfortunatedly cannot resolve this quickly now

