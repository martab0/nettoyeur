import csv
import re

def has_invisible_characters(text):
    # Regular expression to match invisible Unicode characters
    invisible_chars_pattern = re.compile(r'[\u200B-\u200D\uFEFF]')
    return bool(invisible_chars_pattern.search(text))

def process_csv(input_file, output_file, deleted_rows_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile, \
         open(output_file, 'w', newline='', encoding='utf-8') as outfile, \
         open(deleted_rows_file, 'w', newline='', encoding='utf-8') as deletedfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        deleted_writer = csv.writer(deletedfile)

        seen = {}  # To keep track of unique source terms and their target terms

        for row in reader:
            # Join the row elements into a single string
            line = ','.join(row)

            # Check conditions
            if (',' not in line or                  # No comma
                line.count(',') > 1 or              # More than one comma
                # '"' in line or                      # Contains quotation marks
                # re.search('<[^>]+>', line) or       # Contains HTML tags
                line.startswith(',') or             # Empty field before comma
                line.endswith(',') or               # Empty field after comma
                ',,' in line):                     # Empty field between commas
                # line.strip() != line or             # Starts or ends with whitespace
                # has_invisible_characters(line)):    # Contains invisible Unicode characters
                deleted_writer.writerow(row)  # Write to deleted rows file
                continue  # Skip this row

            # Split the row into source and target terms
            if len(row) == 2:
                source_term, target_term = row

                # If the source term is new or matches the existing target term, add/keep it
                if source_term not in seen or seen[source_term] == target_term:
                    seen[source_term] = target_term
                else:
                    deleted_writer.writerow(row)  # Write to deleted rows file
            else:
                deleted_writer.writerow(row)  # Write to deleted rows file
                continue  # Skip rows that don't have exactly two columns

        # Write the unique entries to the output file
        for source_term, target_term in seen.items():
            writer.writerow([source_term, target_term])

def main():
    input_file = input("Enter the input CSV file name: ")
    output_file = input("Enter the output CSV file name: ")
    deleted_rows_file = input("Enter the file name for deleted rows: ")

    try:
        process_csv(input_file, output_file, deleted_rows_file)
        print(f"Processing complete. Output saved to '{output_file}'.")
        print(f"Deleted rows saved to '{deleted_rows_file}'.")
    except FileNotFoundError:
        print(f"Error: The file '{input_file}' does not exist.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
