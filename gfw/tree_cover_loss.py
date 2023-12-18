import requests
import json
from typing import List, Dict, Any

def create_geojson_polygon(coordinates: List[List[float]]) -> Dict[str, Any]:
    """
    Create a GeoJSON object for a polygon given a list of coordinates.
    
    :param coordinates: A list of coordinates defining the polygon.
    :return: A GeoJSON formatted polygon object.
    """
    return {
        "type": "Polygon",
        "coordinates": [coordinates]
    }

def construct_sql_query(year: int) -> str:
    """
    Construct the SQL query for the given year.

    :param year: The year for which tree cover loss data is required.
    :return: A SQL query string.
    """
    return f"SELECT SUM(area__ha) FROM results WHERE umd_tree_cover_loss__year={year}"

def send_post_request(geometry: Dict[str, Any], sql: str, api_key: str) -> requests.Response:
    """
    Send a POST request to the GFW Data API.

    :param geometry: The GeoJSON formatted geometry.
    :param sql: The SQL query string.
    :param api_key: The API key for authorization.
    :return: The response from the API.
    """
    url = "https://data-api.globalforestwatch.org/dataset/umd_tree_cover_loss/latest/query"
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = json.dumps({"geometry": geometry, "sql": sql})
    response = requests.post(url, headers=headers, data=data)
    print('Response: ', response)
    return response

def get_tree_cover_loss_data(coordinates: List[List[float]], api_key: str):
    """
    Get tree cover loss data for a range of years and display it in a readable format.

    :param coordinates: The coordinates defining the area of interest.
    :param api_key: The API key for authorization.
    """
    geojson_polygon = create_geojson_polygon(coordinates)
    
    for year in range(2010, 2024):
        sql_query = construct_sql_query(year)
        response = send_post_request(geojson_polygon, sql_query, api_key)

        if response.status_code == 200:
            data = response.json()
            area_loss = data['data'][0]['area__ha'] if data['data'] else 0
            print(f"En el año {year}, la pérdida de cobertura arbórea fue de aproximadamente {area_loss:.2f} hectáreas.")
        else:
            print(f"Error en el año {year}: Estado {response.status_code}")

# Example usage
coordinates = [[-64.73218287192913, -30.729190990496853], [-64.73218287192913, -31.521817034834548],
               [-64.11153624615092, -31.521817034834548], [-64.11153624615092, -30.729190990496853],
               [-64.73218287192913, -30.729190990496853]]

api_key = "79079ed4-9a8b-4e8a-98e6-3f9370d2f66a"
get_tree_cover_loss_data(coordinates, api_key)