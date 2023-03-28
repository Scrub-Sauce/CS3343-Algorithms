import sys
from Map import Map

# Main Function
if __name__ == "__main__":
    queries_file = 'Queries.csv'
    if len(sys.argv) == 2:
        stores_file = sys.argv[1]
    elif len(sys.argv) == 3:
        stores_file = sys.argv[1]
        queries_file = sys.argv[2]
    else:
        sys.stderr.write("""Improper Usage Error: 'python3 main.py [locations_filename.csv]' or 'python3 main.py [locations_filename.csv] [queries_filename.csv]'""")
        exit(1)

    store_map = Map.get_map_instance()
    store_map.load_locations(stores_file)
    store_map.load_queries(queries_file)
    print(store_map)
    locations = store_map.get_locations()
    print(locations[0])
