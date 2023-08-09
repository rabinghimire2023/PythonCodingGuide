"""Create a function search_log that takes a log file and a search keyword as input.
The function should find and display all lines containing the search keyword."""
def search_log(log_file, search_keyword):
    try:
        with open(log_file, 'r') as file:
            for line_number, line in enumerate(file, 1):
                if search_keyword in line:
                    print(f"Line {line_number}: {line.strip()}")

        print("Search complete.")
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
    except Exception as e:
        print(f"Error: {e}")

log_file = "logfile.txt"
search_keyword = "Error"

search_log(log_file, search_keyword) #ouput:Search complete.
