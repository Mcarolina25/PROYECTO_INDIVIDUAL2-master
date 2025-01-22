import pandas as pd


df = pd.DataFrame(data)

# Calcular KPI
df['KPI (%)'] = ((df['Nuevo_acceso'] - df['Acceso_actual']) / df['Acceso_actual']) * 100

print(df)