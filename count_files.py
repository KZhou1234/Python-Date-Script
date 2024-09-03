import os
from pathlib import Path
'''Create a Python script that counts the number of items (files and directories) in a specified directory(take dir as input). 
The script should display the total number of items (both files and directories) present in the specified directory. 
Bonus Modify your script to count the number of files and directories separately. Hint: use the os module'''

count_file = 0
count_dir = 0
path = input("Please enter a directory name \n")
print(os.path.join(path, "/home/ubuntu/", path))
if(os.path.exists(path)):
    for path in os.scandir(path):
        if path.is_file():
            count_file += 1
        elif path.is_dir():
            count_dir += 1
else:
    print("This path does not exist")
    exit()
    
print(f"There are total {count_file} of files under {path} and total {count_dir} under {path}.")
    
