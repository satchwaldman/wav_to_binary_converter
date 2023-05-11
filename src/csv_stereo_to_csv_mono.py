import csv

input_file = "src/output_data.csv"
output_file = "src/output_data_mono.csv"

# Open the input and output files
with open(input_file, "r") as file_in, open(output_file, "w", newline="") as file_out:
    lines = file_in.readlines()
    writer = csv.writer(file_out)
    
    # Iterate over each line in the input file
    for line in lines:
        # Remove brackets and leading/trailing whitespaces
        line = line.strip().strip("[]")
        
        # Split the line into elements
        elements = line.split()
        
        # Extract the first element
        first_element = elements[0]
        
        # Write the first element to the output file
        writer.writerow([first_element])
