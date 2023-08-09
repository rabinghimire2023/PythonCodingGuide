"""Create a function search_log that takes a log file
and a search keyword as input.
The function should find and display
all lines containing the search keyword."""


def search_log(log_file, search_keyword):
    """Search Log

    Args:
        log_file (str): Log File
        search_keyword (str): Search Keyboard
    """
    try:
        with open(log_file, 'r', encoding="utf-8") as file:
            for line_number, line in enumerate(file, 1):
                if search_keyword in line:
                    print(f"Line {line_number}: {line.strip()}")

        print("Search complete.")
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")


LOGFILE = "logfile.txt"
SEARCHKEYWORD = "Error"

search_log(LOGFILE, SEARCHKEYWORD)  # ouput:Search complete.
