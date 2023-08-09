"""File .py"""
# Implement a program that
# reads a CSV file named "data.csv,"
# containing columns
# "Name" and "Age."
# Create a new CSV file called
# "adults.csv" with only the rows of
# individuals who are 18 years or older"""

import csv


def filter_adults(inputfile, outputfile):
    """File Adults

    Args:
        inputfile (str): Input file
        outputfile (str): ouptut file
    """
    with open(inputfile, 'r', encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        adults = [row for row in reader if int(row['Age']) >= 18]
    if adults:
        with open(outputfile, 'w', encoding="utf-8", newline='') as output_csv:
            fieldnames = ['Name', 'Age']
            writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(adults)
        print(f"Data for adults has been saved to {outputfile}.")
    else:
        print("No data found for adults")


INPUT_FILE = "data.csv"
OUTPUT_FILE = "adults.csv"
filter_adults(INPUT_FILE, OUTPUT_FILE)
