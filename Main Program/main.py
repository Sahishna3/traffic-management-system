from data_collection.traffic_api import get_traffic_data
from data_processing.traffic_analysis import analyze_traffic_data
from route_planning.dijkstra import dijkstra
from visualization.map_display import display_map
from alerts.email_alerts import send_email_alert


def main():
    # Step 1: Collect Data
    traffic_data = get_traffic_data("your_api_key", "New York")

    # Step 2: Process Data
    average_flow = analyze_traffic_data(traffic_data)
    print(f"Average Traffic Flow: {average_flow}")

    # Step 3:route_planning
    graph = {
        'A': {'B': 1, 'C': 4},
        'B': {'A': 1, 'C': 2, 'D': 5},
        'C': {'A': 4, 'B': 2, 'D': 1},
        'D': {'B': 5, 'C': 1}
    }
    distances, shortest_path = dijkstra(graph, 'A')
    print(f"Shortest Path: {shortest_path}")

    # Step 4: visualization
    routes = [
        [(40.7128, -74.0060), (40.7129, -74.0050)],  # Example route
    ]
    traffic_map = display_map(routes)
    traffic_map.save("traffic_map.html")

    # Step 5: alerts
    send_email_alert("recipient@example.com", "Traffic Alert", "High traffic detected")


if __name__ == "__main__":
    main()
