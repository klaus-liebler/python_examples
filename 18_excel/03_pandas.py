## pip install pandas
## pip install openpyxl
import pandas as pd
age = pd.Series([78, 43, 8])
is_female = pd.Series([False,False,True])
name=pd.Series(["Opa", "Papa", "Tochter"])
ort=pd.Series(["Lienen", "Greven", "Greven"])
df = pd.DataFrame({"Name":name, "Weiblich":is_female, "Alter":age, "Ort":ort})
df.to_excel("familie.xlsx", index=False)
papa_index=pd.Index(name).get_loc("Papa")
print("Papa ist", age[papa_index], "Jahre alt und wohnt in", ort[papa_index])


print(df["Alter"].max())