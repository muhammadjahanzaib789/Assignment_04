import os
import re # regulor expression
print('Selected Directory :', os.getcwd())
user_input = input('Do You Want To Proceed?(y/n)')
if user_input.capitalize() == 'Y':
     string =input('Enter The Name You Want To Give To Each File')
     no = 0
     replace_name = ''
     for file_names in os.listdir():
          if file_names == 'renamer.py' or file_names == 'renamer.exe':
               continue
          extension_finder = re.compile(r'\..+$')
          ext = extension_finder.search(file_names)
          no += 1
          replace_name = f'{string}-{no}{file_names[ext.start():ext.end()]}'
          os.rename(file_names,replace_name)