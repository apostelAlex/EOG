import csv, sys
import pandas as pd

def convert_scientific_to_real(number_str):
    try:
        number = float(number_str)
        # Check if the number is in scientific notation
        if 'e' in number_str.lower():
            return '{:.12f}'.format(number)
        else:
            return number_str  # Return unchanged if not in scientific notation
    except ValueError:
        return number_str  # Return unchanged if not convertible to float

def convert_csv_to_real_numbers(input_csv, output_csv):
    with open(input_csv, 'r') as infile, open(output_csv, 'w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        
        for row in reader:
            converted_row = [convert_scientific_to_real(cell) for cell in row] 
            writer.writerow(converted_row)



def remove_scientific_notation(path:str)-> None:
    df = pd.read_csv(path)
    df.to_csv(path)


if __name__ == "__main__":
    args = sys.argv
    if len(args)<3:
        # Example usage:
        input_csv = 'test.csv'  # Change this to the name of your input CSV file
    else:
        input_csv = args[-1] 
    remove_scientific_notation(input_csv)
