import numpy as np
import pandas as pd
age = pd.Series([78, 43, 8])
is_female = pd.Series([False,False,True])
name=pd.Series(["Opa", "Papa", "Tochter"])
df = pd.DataFrame({"Name":name, "Weiblich":is_female, "Alter":age})
df.to_excel("familie.xlsx", index=False)

print(df["Name"])
print(df["Alter"].max())