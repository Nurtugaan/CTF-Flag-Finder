import re

def find_flag(filename):
    try:
        with open(filename, 'r', encoding='latin-1') as file:  # use the encoding you need
            for line in file:
                if "CTF{" in line: # you can write your example of CTF
                    return line.strip()  # Return a string with the found flag without whitespace at the beginning and end
        return "Flag not found in file"
    except FileNotFoundError:
        return "The specified file was not found"

# Name of the file where you want to find the flag
filename = "name_of_your_file"

# Finding a flag in a file
flag = find_flag(filename)
print(flag)