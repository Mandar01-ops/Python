import os
directory_path='/home' #specify the directory you want to list
contents=os.listdir(directory_path) # List all files and directories in the specified path
 #Print each file and directory name
print(contents)