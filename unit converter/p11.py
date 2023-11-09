def write_reverse_conversions(input_line, output_file):
    parts = input_line.strip().split('=')
    if len(parts) == 2:
        left, right = [part.strip() for part in parts]
        left_value, left_unit = left.split()
        right_value, right_unit = right.split()

        left_value = float(left_value)
        right_value = float(right_value)

        reverse_left = 1 / right_value
        reverse_right = 1 / left_value

        output_file.write(f"1 {left_unit} = {reverse_left:.2f} {right_unit}.\n")
        output_file.write(f"1 {right_unit} = {reverse_right:.2f} {left_unit}.\n")

# Main program
input_file_name = "inConvert.txt"
output_file_name = "outConvert.txt"

with open(input_file_name, "r") as input_file, open(output_file_name, "w") as output_file:
    for line in input_file:
        write_reverse_conversions(line, output_file)

print("Conversion completed. Results written to 'outConvert.txt'.")
