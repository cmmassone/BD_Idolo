import pandas as pd

# Cargar el archivo Excel
df_snridol = pd.read_excel(r'C:\Users\Usuario\Desktop\CtrlingIdol_SNR.xlsx') #Animales Seca/NR capturados
df_bdidol = pd.read_excel(r'C:\Users\Usuario\Desktop\BDIdol.xlsx')           #BD asociacion caravana-bolos
df_anidol = pd.read_excel(r'C:\Users\Usuario\Desktop\ANIdol.xlsx')           #BD asociacion caravana-botones
df_anidol_mod = pd.read_excel(r'C:\Users\Usuario\Desktop\df_anidol_mod.xlsx')#Info compartida a German-Meli-Eze


# Quedarse solo con las columnas eRP y RP en df_bdidol
df_bdidol = df_bdidol[['RP', 'eRP']]

# Quedarse solo con las columnas eRP y RP en df_anidol
df_anidol = df_anidol[['RP', 'eRP']]

# Quedarse solo con las columnas eRP y RP en df_snridol (si estas columnas existen)
df_snridol = df_snridol[['RP', 'eRP']]  # Asegúrate de que estas columnas existan en df_snridol

# Convertir la columna eRP a tipo string y eliminar espacios en df_bdidol
df_bdidol['eRP'] = df_bdidol['eRP'].astype(str).str.replace(' ', '', regex=False)

# Reordenar las columnas en df_anidol
df_bdidol = df_bdidol[['RP', 'eRP']]
df_anidol = df_anidol[['RP', 'eRP']]
df_snridol = df_snridol[['RP', 'eRP']]


# Convertir la columna eRP a tipo numérico en df_bdidol
df_bdidol['eRP'] = pd.to_numeric(df_bdidol['eRP'], errors='coerce')

# Convertir la columna eRP a tipo numérico en df_anidol
df_anidol['eRP'] = pd.to_numeric(df_anidol['eRP'], errors='coerce')

# Convertir la columna eRP a tipo numérico en df_snridol
df_snridol['eRP'] = pd.to_numeric(df_snridol['eRP'], errors='coerce')

# Convertir la columna eRP a tipo numérico en df_anidol_mod
df_anidol_mod['eRP'] = pd.to_numeric(df_anidol_mod['eRP'], errors='coerce')
df_anidol_mod['eRP_DOS'] = pd.to_numeric(df_anidol_mod['eRP_DOS'], errors='coerce')




# Creo copia del dataframe df_bdidol y lo nombro df_bdidol_aux
df_bdidol_aux = df_bdidol.copy()



# {{ edit_1 }}: Agregar la columna 'Lectura' y completarla con 'Si' donde se encuentren los valores
df_bdidol_aux['Lectura'] = df_bdidol_aux['eRP'].isin(df_snridol['eRP']).replace({True: 'Si', False: ''})

#df_bdidol_aux.to_excel(r'C:\Users\Usuario\Desktop\df_bdidol_lec.xlsx', index=False)


# {{ edit_2 }}: Agregar la columna 'eRP (Farmerin)' donde coincidan los valores de 'RP'
df_bdidol_aux['eRP (Farmerin)'] = df_bdidol_aux.apply(
    lambda row: df_anidol.loc[df_anidol['RP'] == row['RP'], 'eRP'].values[0] if row['Lectura'] == 'Si' and not df_anidol.loc[df_anidol['RP'] == row['RP'], 'eRP'].empty else '',
    axis=1
)


# {{ edit_3 }}: Agregar la columna 'Similitud' para comparar 'eRP' y 'eRP (Farmerin)'
df_bdidol_aux['Similitud'] = df_bdidol_aux.apply(
    lambda row: 'T' if row['eRP'] == row['eRP (Farmerin)'] else 'F',
    axis=1
)

# {{ edit_4 }}: Filtrar solo las filas donde 'Lectura' es 'Si'
df_bdidol_aux = df_bdidol_aux.loc[df_bdidol_aux['Lectura'] == 'Si']


# {{ edit_5 }}: Agregar la columna 'Enviados' y completarla con 'SI' donde 'RP' esté en df_anidol_mod
df_bdidol_aux['Enviados'] = df_bdidol_aux['RP'].isin(df_anidol_mod['RP']).replace({True: 'OK', False: ''})


# Descargo el .xlxs
df_bdidol_aux.to_excel(r'C:\Users\Usuario\Desktop\df_bdidol_final.xlsx', index=False)

# Muestro por pantalla los diferentes dataframe
#print(df_bdidol)
print(df_bdidol_aux)
#print(df_snridol)
#print(df_anidol_mod)
