# Importar la libreria pandas, que es fundamental para el analisis de datos
import pandas as pd

# Define la ruta del archivo csv que contiene los datos.
# Si el archivo esta en el mismo directorio que este script, solo  necesitas el nombre del archivo.
path = 'Online_Retail.csv'

# Lee el archivo csv usando la función read_csv de pandas
# se especifica la codificación latin 1 para manejar caracteres especiales
retail_data = pd.read_csv(path, encoding="latin1")
# Muestra el tipo de la variable retail_data para confirmar que es un DataFrame de pandas.
# un dataframe es una estructura de datos bidimensional similar a una tabla.
print(type(retail_data))
# Imprime todo el contenido del data frame
print(retail_data)