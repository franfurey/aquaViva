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

def construct_sql_query(start_date: str, end_date: str) -> str:
    """
    Construct the SQL query for the given date range.

    :param start_date: Start date of the range (YYYY-MM-DD).
    :param end_date: End date of the range (YYYY-MM-DD).
    :return: A SQL query string.
    """
    return f"SELECT longitude, latitude, wur_radd_alerts__date, wur_radd_alerts__confidence FROM results WHERE wur_radd_alerts__date >= '{start_date}' AND wur_radd_alerts__date <= '{end_date}'"

def send_post_request(geometry: Dict[str, Any], sql: str, api_key: str) -> requests.Response:
    """
    Send a POST request to the GFW Data API.

    :param geometry: The GeoJSON formatted geometry.
    :param sql: The SQL query string.
    :param api_key: The API key for authorization.
    :return: The response from the API.
    """
    url = "https://data-api.globalforestwatch.org/dataset/wur_radd_alerts/latest/query"
    headers = {
        'x-api-key': api_key,
        'Content-Type': 'application/json'
    }
    data = json.dumps({"geometry": geometry, "sql": sql})
    response = requests.post(url, headers=headers, data=data)
    return response

# Example usage
coordinates = [[-60.590457916259766, -15.095079526355857], [-60.60298919677734, -15.090936030923759],
               [-60.60161590576172, -15.104774989795663], [-60.590457916259766, -15.095079526355857]]

geojson_polygon = create_geojson_polygon(coordinates)
sql_query = construct_sql_query('2023-05-01', '2023-12-17')
api_key = "79079ed4-9a8b-4e8a-98e6-3f9370d2f66a"

response = send_post_request(geojson_polygon, sql_query, api_key)
if response.status_code == 200:
    print("Respuesta de la API:", response.json())
else:
    print("Error:", response.status_code)
