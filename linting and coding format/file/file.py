"""
Implement a program that reads a CSV file named "data.csv," containing columns
"Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of
individuals who are 18 years or older"""
import csv

def filter_adults(input_file,output_file):
    with open(input_file,'r') as csv_file:
        reader = csv.DictReader(csv_file)
        adults =[row for row in reader if int(row['Age'])>=18]
    if adults:
        with open(output_file,'w',newline='') as output_csv :
            fieldnames=['Name','Age']
            writer=csv.DictWriter(output_csv,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(adults)
        print(f"Data for adults has been saved to {output_file}.")  
    else:
        print("No data found for adults")
    
input_file="data.csv"
output_file="adults.csv"
filter_adults(input_file,output_file)
