import os
import argparse


"""
This file prints the folder structure to a txt file.
For example:

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

def check_target(target_folder, foldername):
    return foldername==target_folder
    

def path_loop(file, path, flag, max_depth=3, max_length=10, 
              target_folder=None, depth=0):
    
    if depth > max_depth:
        return None
    
    depth_string = "│    "*depth

    dir_list = []
    onlyfolders = [dir_list.append(f) for f in os.listdir(path) if 
                                        os.path.isdir(os.path.join(path, f))]
    onlyfiles = [dir_list.append(f) for f in os.listdir(path) if 
                                        os.path.isfile(os.path.join(path, f))]

    for i,f in enumerate(dir_list):
        
        if i >= max_length and flag!=True:
            file.write(depth_string + '└─── ...\n')
            break 
            
        new_path=os.path.join(path, f)
        if os.path.isdir(new_path):
            file.write(depth_string + '└─── {}/\n'.format(f))

            fl = check_target(target_folder, f)
            path_loop(file, new_path, fl, max_depth, max_length, target_folder, 
                      depth + 1)

        else:
            file.write(depth_string + '└─── {}\n'.format(f)) 
            
    if depth != 0:
        file.write(depth_string+"\n")
    

def main(terms):
    
    path = terms['path']
    max_depth = terms['d']
    max_length = terms['l']
    target_folder = terms['f']
        
    path = os.path.abspath(path)  
    txt_file = open(os.path.join(os.path.dirname(path), "dir_list.txt"), "w")
    txt_file.write('"""\nFolder structure:\n\n')
    txt_file.write('{}\n'.format(os.path.join(
                                 os.path.basename(os.path.normpath(path)),'')))

    flag = check_target(target_folder, path)
    path_loop(txt_file, path, flag, max_depth, max_length, target_folder, 
              depth=0)

    txt_file.write('"""\n')
    txt_file.close()


"""
To run from terminal enter:
python dir_list.py <foldername> -d <int> -l <int> -f <foldername>
For example:
python dir_list.py test -d 3 -l 10 -f test2
"""
parser = argparse.ArgumentParser()
parser.add_argument('path', help='path of the folder to print')
parser.add_argument('-d', type=int, default=3, metavar='depth', 
                          help='maximal print depth boundry')
parser.add_argument('-l', type=int, default=10, metavar='length', 
                          help='maximal print length boundry of a folder')
parser.add_argument('-f', metavar='folder', 
                          help='folder without printing boundries applied')                          
terms = vars(parser.parse_args())

main(terms)