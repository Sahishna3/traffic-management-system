import folium


def display_map(routes):
    map_center = [40.7128, -74.0060]  # Example coordinates (New York City)
    traffic_map = folium.Map(location=map_center, zoom_start=12)
    for route in routes:
        folium.PolyLine(route).add_to(traffic_map)
    return traffic_map
