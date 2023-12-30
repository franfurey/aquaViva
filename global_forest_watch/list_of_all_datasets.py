import requests
import pandas as pd
import os

def get_gfw_datasets(api_url: str = "https://data-api.globalforestwatch.org/datasets") -> pd.DataFrame:
    """
    Fetch the list of datasets available in the GFW Data API and return a DataFrame.

    :param api_url: The API endpoint URL for fetching datasets.
    :return: DataFrame with datasets information.
    """
    response = requests.get(api_url)
    if response.status_code == 200:
        datasets = response.json().get('data', [])
        # Convertimos cada diccionario en metadata en sus propias columnas
        for dataset in datasets:
            metadata = dataset.pop('metadata', {})
            for key, value in metadata.items():
                dataset[f"metadata_{key}"] = value
        return pd.DataFrame(datasets)
    else:
        print(f"Error al obtener los conjuntos de datos: Estado {response.status_code}")
        return pd.DataFrame()

def save_to_excel(df: pd.DataFrame, file_name: str, folder: str = 'gfw') -> None:
    """
    Save the DataFrame to an Excel file in the specified folder.

    :param df: DataFrame to be saved.
    :param file_name: Name of the file to save.
    :param folder: Folder where the file will be saved.
    """
    if not os.path.exists(folder):
        os.makedirs(folder)
    file_path = os.path.join(folder, file_name)
    df.to_excel(file_path, index=False)
    print(f"Datos guardados en {file_path}")

# Obtener los datos
df_datasets = get_gfw_datasets()

# Guardar en un archivo Excel dentro de la carpeta gfw
if not df_datasets.empty:
    save_to_excel(df_datasets, "GFW_Datasets.xlsx")
