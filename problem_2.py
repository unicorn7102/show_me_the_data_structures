# coding: utf-8

import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    output = []
    
    if os.path.isfile(path):
        if path.endswith(suffix): output.append(path)
    elif os.path.isdir(path):
        subpaths = os.listdir(path)
        subpaths_full = [os.path.join(path, p) for p in subpaths]
        
        for p in subpaths_full:
            output.extend(find_files(suffix, p))
    
    return output

if __name__ == '__main__':
    
    print(find_files('.c', './testdir'))
    # ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c','./testdir/subdir1/a.c']
    
    print(find_files('.c', './testdir/t1.c'))
    # ['./testdir/t1.c']
    
    print(find_files('.c', ''))
    # []