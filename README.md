# file_handling
week2_assignment

# Ask the user for a file name
file_name = input("Enter file name: ")

try:
    # Try to open and read the file
    with open(file_name, "r") as file:
        content = file.read()

    # Create a new file and write modified content
    with open("modified_" + file_name, "w") as new_file:
        new_file.write(content.upper())  # Convert text to uppercase

    print("Modified file saved!")

except FileNotFoundError:
    print("Error: File not found!")
except IOError:
    print("Error: Could not read the file!")

