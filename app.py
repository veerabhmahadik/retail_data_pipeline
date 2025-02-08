import sys
from config import DB_DETAILS
from util import get_tables

def main():
    '''Program takes at least one argument'''
    if len(sys.argv) < 2:  # Check if at least one argument is passed
        print("Error: Please provide an environment (e.g., 'dev', 'prod').")
        sys.exit(1)  # Exit the program with an error status
    
    env = sys.argv[1]  # Get the environment argument
    print(f"Running in {env} environment")

    # Example of fetching DB details and processing tables
    db_details = DB_DETAILS[env]
    tables = get_tables('table_list.txt')
    for table in tables['table_name']:
        print(table)

if __name__ == "__main__":
    main()