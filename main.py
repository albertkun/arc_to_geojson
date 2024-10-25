import requests
import geojson
import os
import argparse

def fetch_aserver_data_to_geojson(aserver_url, geojson_file):
    try:
        # Define the query parameters
        params = {
            'where': '1=1',
            'outFields': '*',
            'f': 'geojson'
        }

        # Make the request
        response = requests.get(f"{aserver_url}/query", params=params)
        response.raise_for_status()

        # Parse the response as GeoJSON
        geojson_data = response.json()

        # Write the GeoJSON data to a file
        with open(geojson_file, 'w') as f:
            geojson.dump(geojson_data, f)

        print(f"GeoJSON file saved to {geojson_file}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching data from server: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Fetch data from an server and convert it to GeoJSON.")
    parser.add_argument("aserver_url", help="The URL of the server.")
    parser.add_argument("geojson_file", help="The path to the output GeoJSON file.")
    args = parser.parse_args()

    fetch_aserver_data_to_geojson(args.aserver_url, args.geojson_file)