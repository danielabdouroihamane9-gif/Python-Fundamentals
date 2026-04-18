#29 FILE HANDLING = It is used to store data permanently in a file. We can read and write data to a file.
#   Syntax:  file_object = open("file_name.txt", "mode")
#   Modes: 'r' = read, 'w' = write, 'a' = append, 'x' = create, 'b' = binary, 't' = text

# 1. Open a file in reading mode and read its content
f = open("D:/student.txt", "r")
print(f.read())
f.close()   # Always remember to close the file after using it to free up system resources.

#* Using with statement to handle files (it automatically closes the file after the block is executed)
with open("demofile.txt", "r") as f:
    print(f.read())

#* Read Only Part of the File
with open("demofile.txt", "r") as f:
    print(f.read(5))  # Reads the first 5 characters of the file
    print(f.read(10)) # Reads the next 10 characters of the file

#* Read Line by Line
with open("demofile.txt", "r") as f:
    print(f.readline())  # Reads the first line of the file
    print(f.readline())  # Reads the second line of the file

#* Read whole lines by looping through the file object
with open("demofile.txt", "r") as f:
    for line in f:
        print(line)  # Prints each line of the file

# 2. Open a file in append mode and write some content to it
with open("demofile.txt", "a") as f:    # It appends to the end of the file without overwriting existing content.
    f.write("This is an additional line.\n")  # Writes a new line to the file
    f.write("Now the file has more content!")
with open("demofile.txt", "r") as f:
    print(f.read())  # Reads the updated content of the file

# 3. Open a file in write mode and write some content to it
with open("demofile.txt", "w") as f:    # It overwrites the existing content of the file with new content.
    f.write("This is the new content of the file.\n")  # Writes new content to the file
    f.write("All previous content has been replaced!")
with open("demofile.txt", "r") as f:
    print(f.read())  # Reads the new content of the file

# 4. Open a file in create mode and write some content to it
f = open("my.txt", "x")  # It creates a new file. If the file already exists, it raises a FileExistsError.

# 5. Python Delete a File
import os   
os.remove("demofile.txt")  # Deletes the specified file

#* Check if a file exists before deleting it
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
    print("File deleted successfully!")
else:
    print("File does not exist!")

#* Delete a folder
import os
os.rmdir("myfolder")  # Deletes the specified folder (the folder must be empty to be deleted)

import shutil
shutil.rmtree("myfolder")  # Deletes the specified folder and all its contents (use with caution)

with open("settings.py", "w") as f:
    f.write("# This file contains user settings for the application.\n")
    f.write("settings = {}\n")  # Initialize an empty dictionary to store settings