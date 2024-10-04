import pandas as pd

# Cargar el archivo Excel
df_anidol = pd.read_excel(r'C:\Users\farme\Desktop\ANIdol.xlsx')

# Cargar el archivo CSV
#df_bdidol = pd.read_csv(r'C:\Users\farme\Desktop\BDIdol.csv')
df_bdidol = pd.read_excel(r'C:\Users\farme\Desktop\BDIdol.xlsx')

# Quedarse solo con las columnas eRP y RP en df_bdidol
df_bdidol = df_bdidol[['RP', 'eRP']]

# Quedarse solo con las columnas eRP y RP en df_anidol (si estas columnas existen)
df_anidol = df_anidol[['RP', 'eRP']]  # Asegúrate de que estas columnas existan en df_anidol


# Convertir la columna eRP a tipo string y eliminar espacios en df_bdidol
df_bdidol['eRP'] = df_bdidol['eRP'].astype(str).str.replace(' ', '', regex=False)


# Realizar un merge para agregar la columna eRP_DOS
df_anidol_mod = df_anidol.merge(df_bdidol[['RP', 'eRP']], on='RP', how='left', suffixes=('', '_DOS'))

# Renombrar la nueva columna a eRP_DOS
df_anidol_mod.rename(columns={'eRP_DOS': 'eRP_DOS'}, inplace=True)

# Reordenar las columnas en df_anidol
df_anidol_mod = df_anidol_mod[['RP', 'eRP', 'eRP_DOS']]

#print(df_bdidol)
#print(df_anidol)
print(df_anidol_mod)

df_anidol_mod.to_excel(r'C:\Users\farme\Desktop\df_anidol_mod.xlsx', index=False)
