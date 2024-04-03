# Open the input file and read its contents
with open('The Joy Of Painiting - Subject Matter', 'r') as file:
    data = file.readlines()

# Open a new file for writing
with open('episode_subject.csv', 'w') as output_file:
    # Write the header line without quotes
    header = data[0].replace('"', '')
    output_file.write(header)

    for line in data[1:]:
        # Remove quotes from the line
        line = line.replace('"', '')
        output_file.write(line)
       