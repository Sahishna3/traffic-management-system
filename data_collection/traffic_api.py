import requests

# Define your API key and other configurations
api_key = 'your_actual_here_api_key'
def get_traffic_data(api_key, location):
    url = f"https://api.traffic.com/data?location=40.7128,-74.0060;40.7484,-73.9857&key={api_key}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

location = '40.7128,-74.0060;40.7484,-73.9857'  # Example bounding box for New York City
traffic_data = get_traffic_data(location)
print(traffic_data)
