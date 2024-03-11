
# Buscamos duplicados en la columna
def check_duplicates(df,column_name):
    try:
        duplicates = df[df.duplicated(subset=[column_name], keep=False)]
        if not duplicates.empty:
            print("Valores Duplicados:")
            return duplicates
        else:
            print(f"No hay duplicados en la columna:{column_name}")
            return None
    except KeyError:
        print(f"Columna '{column_name}' no existe en Dataframe.")
        return None
    
# Buscamos valores faltantes
def check_missing_values(df, column_name):
    try:
        missing_values = df[df[column_name].isnull()]
        if not missing_values.empty:
            print(f"Valores faltantes en {column_name}:")
            return missing_values
        else:
            print(f"No hay valores faltantes en la columna {column_name}")
    except KeyError:
        print(f"Columna '{column_name}' no existe en Dataframe.")
        return None



# Estadísticas del dataframe generales                       
def calculate_column_stats(df):
    stats = pd.DataFrame()
    df.replace(r'^\s*$', np.nan, regex=True, inplace=True)
    for col in df.columns:
        unique_values = df[col].nunique()
        missing_values = df[col].isnull().sum()
        missing_percentage = round(((missing_values / len(df)) * 100),2)

        if df[col].dtype in ['int64', 'float64']:
            min_value = df[col].min()
            max_value = df[col].max()
            most_common = df[col].mode().values[0]
        else:
            min_value = None
            max_value = None
            most_common = None

        has_duplicates = df[col].duplicated().any()
        duplicate_percentage = round(((df[col].duplicated().sum() / len(df)) * 100),2)

        stats[col] = [unique_values, missing_values, missing_percentage, 
                      min_value, max_value, most_common, has_duplicates, duplicate_percentage]

    # Transponer el DataFrame
    stats = stats.T

    # Setear el nombre de las columnas
    stats.columns = ['Unique_Values', 'Missing_Values', 'Missing_Percentage', 
                     'Min', 'Max', 'Most_Common', 'Has_Duplicates', 'Duplicate_Percentage']

    # Agregar una nueva columna de  datatype
    stats['Data_Type'] = df.dtypes

    return stats

# Analizamos las características básicas d la columna    
def sumary_column(df,column_name):
    cantidad = df[column_name].value_counts()
    list = df[column_name].nunique()
    print(list)
    print(f'Hay {cantidad} de valores únicos en {column_name}')
    return df[column_name].value_counts()

def convert_to_sentence_case(df, columns):
    # Aplicar una transformacion al string en las columnas definicas 
    for column in columns:
        df[column] = df[column].apply(lambda x: str(x).title())

def create_point(latitude, longitude):
    return f'point({latitude}, {longitude})'

# Función para asignar el rango a las edades 
def assign_age_group(age):
    for group, age_range in rango_edad.items():
        if age in age_range:
            return group
    return '66+' # Handle cases outside specified ranges


# Definir una función para actualizar las columnas de punto, latitud y longitud
def update_coordinates(row):
    row['point'] = 'Point(0, 0)'
    row['latitude'] = 0
    row['longitude'] = 0
    return row