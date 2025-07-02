import csv

input_file = 'PATH HERE'   # Replace with your file name
output_file = 'filtered_STATE.csv'
state_column_name = 'state'  # Replace with your column name if different, like if is "States" OR whatever. 

with open(input_file, newline='', encoding='utf-8') as infile, \
     open(output_file, 'w', newline='', encoding='utf-8') as outfile:
    
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, fieldnames=reader.fieldnames)
    
    writer.writeheader()

# REPLACE THE "ST" WITH THE STATES TWO DIGIT CODE. EXAMPLES ARE CA, NY, NJ, FL, etc. 
    for row in reader:
        if row[state_column_name].strip().upper() == "ST":
            writer.writerow(row)

print(f"Filtered rows saved to {output_file}")
