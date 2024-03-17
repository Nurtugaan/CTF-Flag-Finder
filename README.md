CTF Flag Finder

This Python script is designed to search for Capture The Flag (CTF) style flags within a given file. It utilizes regular expressions to locate lines containing the specified flag format.

Usage
Requirements: Python 3.x
Instructions:
Place the script (find_flag.py) in the directory where your file is located or provide the full path to your file.
Modify the filename variable in the script to point to the file where you want to search for the flag.
Run the script in a Python environment.
How it Works
The script reads the specified file line by line. If a line contains the string "CTF{", it assumes that it has found a flag and returns the line without leading or trailing whitespace. If the script doesn't find any flag-like strings, it returns a message indicating that the flag was not found in the file.

Example
Suppose you have a file named example.txt containing various text, including a line with a CTF flag like CTF{example_flag_here}. By running the script with example.txt specified as the filename, it will output the found flag, if any.

Notes
Make sure to specify the correct encoding for your file in the script if it's not in UTF-8.
If the specified file is not found, the script will return a corresponding error message.
Feel free to use and modify this script according to your needs. Happy flag hunting!
