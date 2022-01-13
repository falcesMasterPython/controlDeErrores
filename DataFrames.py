import pandas as pd
import numpy  as np
from pandas.core.arrays.string_ import StringArray
from pandas.core.frame import DataFrame
from pandas.io.pytables import IndexCol

def cambioDataframe():
    print(' ')
    print('-----------------------------------------------------')
    print('---------------- CAMBIO DE DATAFRAME ----------------')
    print('-----------------------------------------------------')
    print(' ')

def ejemplo(text):
    print(' ')
    print(text, '---------------------')
    print(' ')

f = lambda x : int(x) + 10
g = lambda x : int(x) * 10

cambioDataframe()

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

pd.set_option("display.max_rows", None, "display.max_columns", None)

df = pd.DataFrame(data)
ejemplo('df')
print(df)

ejemplo('df.head(n=2)')
print(df.head(n=2)) # Número de filas empezando por arriba

ejemplo('df.tail(n=2)')
print(df.tail(n=2)) # Número de filas empezando por abajo

row_labels = [101, 102, 103, 104, 105, 106, 107]
df = pd.DataFrame(
    data,               # Datos
    index=row_labels    # Crear índices (debe coincidir con el número de filas)
)
ejemplo('df')
print(df)

# Selecciionar una columna. Es lo mismo que df.city si el nombre de la columna es un identificador válido
cities = df['city']
ejemplo("cities = df['city']")
print(cities)

# Seleccionar un dato concreto de la columna
ejemplo("cities[104]")
print(cities[104])

 # Seleccionar una fila concreta
row = df.loc[103]
ejemplo("row = df.loc[103]")
print(row)

# Seleccionar un dato de la fila. Es lo mismo que row.age si el nombre de la columna es un identificador válido
ejemplo("row['age']")
print(row['age'])

cambioDataframe()
print('Creating a Pandas DataFrame With Dictionaries')

d = {'x': [1, 2, 3], 'y': np.array([2, 4, 8]), 'z': 100}

data = pd.DataFrame(d)
ejemplo("data")
print(data)

data = pd.DataFrame(
    d,                          # dataframe
    index=[100, 200, 300],      # Cambio de índices
    columns=['z', 'y'],         # Selección y orden de las columnas
)
ejemplo("pd.DataFrame con index, columns")
print(data)

print('')
print('Creating a Pandas DataFrame With Lists')

l = [{'x': 1, 'y': 2, 'z': 100},
     {'x': 2, 'y': 4, 'z': 100},
     {'x': 3, 'y': 8, 'z': 100}]

data = pd.DataFrame(l)

ejemplo('data')
print(data)

data = pd.DataFrame(l, columns=['x', 'y', 'z'])
ejemplo('data con columns')
print(data)

print('')
print('Creating a Pandas DataFrame With NumPy Arrays')

arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])

data = pd.DataFrame(arr, columns=['x', 'y', 'z'])
ejemplo('data con columns')
print(data)

# Podemos modificar valores en el array original y se reflejan, ya que no es una copia. Modificar el array original también modifica el DataFrame
ejemplo('arr[0, 0] = 1000')
arr[0, 0] = 1000
print(data)

# Podemos especificar que se haga una copia
ejemplo('Parámetro copy=True')
arr = np.array([[1, 2, 100],
                [2, 4, 100],
                [3, 8, 100]])
data = pd.DataFrame(arr, columns=['x', 'y', 'z'], copy=True)
arr[0, 0] = 1000
print(data)

cambioDataframe()

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai', 'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}

ejemplo('Crear CSV con el dataframe')
df = pd.DataFrame(data)
try:
    df.to_csv('data/data.csv')
except Exception as e:
    print('Error:', e)
else:
    print("Se ha creado el archivo en data/data.csv")

ejemplo('Leer CSV con el dataframe')
df = pd.read_csv('data/data.csv', index_col=0)
print(df)

ejemplo('Extraer índices y campos')

indices = df.index
print(indices)

campos = df.columns
print(campos)

ejemplo('Extraer nombre del campo en la tercera posición')
print(campos[2])

ejemplo('Modificar índices')
# Creamos un array secuencial con Numpy y lo asignamos al índice del DataFrame
df.index = np.arange(10, 17)
print(df.index)
print(df)

# Pandas recomienda el uso de Numpy para extraer arrays para poder usar los parámetros dtype y copy.
ejemplo('De DataFrame a Array')
print(df.to_numpy(dtype=None, copy=False))
# print(df.values)

ejemplo('Ver los tipos de datos')
print(df.dtypes)

ejemplo('Modificar tipo de datos')
df = df.astype(dtype={'age': np.int32, 'py-score': np.float32})
print(df.dtypes)
ejemplo('Tamaño del dataframe')
print('Dimensiones')
print(df.ndim)
print('Filas x Columnas')
print(df.shape)
print('Número total de valores')
print(df.size)
print('Memoria utilizada')
print(df.memory_usage())

ejemplo('Accediendo a los datos')
# Accedemos por el valor del índice
print(df.loc[10])
print()
print(df.loc[[10,12]])
print()
print(df.loc[12, 'city'])
print()
print(df.loc[[10,12], 'city'])
print()
print(df.loc[10:12, 'city'])
print()
print(df.loc[:, 'city'])
print()
print(df.iloc[:, 1])
print()
print(df.loc[11:15, ['name', 'city']])
print()
print(df.iloc[1:6, [0, 1]])
print()
print(df.iloc[1:6:2, 0])
print()
print(df.iloc[slice(1, 6, 2), 0])
print()
print(df.iloc[np.s_[1:6:2], 0])
print()
print(df.iloc[pd.IndexSlice[1:6:2], 0])
print()
print(df.at[12, 'name'])
print()
print(df.iat[2, 0])
print()

ejemplo('Modificando datos')

print(df)
print()
df.loc[:13, 'py-score'] = [40, 50, 60, 70]
df.loc[14:, 'py-score'] = 0
print(df)

print()
df.iloc[:, -1] = np.array([88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0])
print(df)

