## dir_list
Prints the folder structure to a text file. Text file is created in the same directory of the given folder.

For example:

"""  
Folder structure:  
  
test_dir/  
└─── test_dir2/  
│    └─── test_dir3/  
│    │    
│    └─── test_file4.txt  
│    └─── test_file3.txt  
│    
└─── test_file.txt  
└─── test_file2.txt  
"""  


### Running dir_list

Run the following in shell:

```
python dir_list.py <PATH_TO_FOLDER>
```


### Options
-h, --help:  show this help message and exit
-d depth:   maximal print depth
-l length:   maximal print length of a folder
-f folder:   folder with no printing length boundry
