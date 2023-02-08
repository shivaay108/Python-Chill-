# for creating and writing into files
import os
with open('file.txt' , 'w') as fp:
    fp.write("hello")
# for writing and reading into files
with open('file.txt' , 'r') as fp:
     fp.read()

with open('this.txt' , 'w') as fp:
     fp.writelines("This file is going to delete")

# for renaming files in the directory
os.rename('file.txt' , 'game.txt')
#  for removing the files in the directory
os.remove("this.txt")  
#  in os.remove there are two params i.e first-> filename second-> filepath (no need to give filepath in case of
# absolute path)

print(os.cpu_count())
