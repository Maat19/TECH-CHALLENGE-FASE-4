import pandas as pd
df = pd.read_csv("Obesity.csv")


df_analise = df.copy()

# Flag de obesidade
df_analise['Obeso'] = df_analise['Obesity'].str.contains("Obesity")

# Faixa etária
df_analise['Faixa_Idade'] = pd.cut(
    df_analise['Age'],
    bins=[13,20,30,40,50,100],
    labels=["14-20","21-30","31-40","41-50","51+"]
)

# Sedentarismo
df_analise['Sedentario'] = df_analise['FAF'] == 0

df_analise.to_csv("obesity_analise.csv", index=False)
