import sys

# Main Function
if __name__ == "__main__":
    queries_file = 'Queries.csv'
    if len(sys.argv) == 2:
        stores_file = sys.argv[1]
    else:
        sys.stderr.write("Improper Usage Error: python3 main.py [filename.csv]")
        exit(1)
