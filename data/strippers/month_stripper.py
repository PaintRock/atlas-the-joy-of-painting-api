# Open the input file and read its contents
with open('The Joy Of Painting - Episode Dates', 'r') as file:
    data = file.readlines()

# Open a new file for writing
with open('date_data.csv', 'w') as output_file:
    for line in data:
        # Split the line by the first comma
        parts = line.split(',', 1)

        # Check if there is a comma
        if len(parts) > 1:
            before_comma = parts[0].strip()
            after_comma = parts[1].strip()

            # Check if there is a space after the comma
            after_comma_parts = after_comma.split(' ', 1)
            if len(after_comma_parts) > 1:
                first_word_after_comma = after_comma_parts[0]
            else:
                first_word_after_comma = after_comma

            # Write the extracted data to the output file
            output_file.write(f"{before_comma},{first_word_after_comma}\n")
        else:
            # Handle lines without a comma
            output_file.write(f"{line.strip()},\n")
            