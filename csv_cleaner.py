import csv
import re

def process_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        seen = set()  # To keep track of unique rows

        for row in reader:
            # Join the row elements into a single string
            line = ','.join(row)

            # Check conditions
            if (',' not in line or                  # No comma
                line.count(',') > 1 or              # More than one comma
                '"' in line or                      # Contains quotation marks
                re.search('<[^>]+>', line) or       # Contains HTML tags
                line.startswith(',') or             # Empty field before comma
                line.endswith(',') or               # Empty field after comma
                ',,' in line or                     # Empty field between commas
                line.strip() != line):              # Starts or ends with whitespace
                continue  # Skip this row

            # Convert the row to a tuple so it can be added to the set
            row_tuple = tuple(row)

            # If the row is not a duplicate, write it to the output file
            if row_tuple not in seen:
                writer.writerow(row)
                seen.add(row_tuple)

def main():
    input_file = input("Enter the input CSV file name: ")
    output_file = input("Enter the output CSV file name: ")

    try:
        process_csv(input_file, output_file)
        print(f"Processing complete. Output saved to '{output_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
