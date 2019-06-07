"""
href: https://www.testdome.com/questions/25970

Write a function that provides change directory (cd) function for an abstract file system.

Notes:

    Root path is '/'.
    Path separator is '/'.
    Parent directory is addressable as '..'.
    Directory names consist only of English alphabet letters (A-Z and a-z).
    The function should support both relative and absolute paths.
    The function will not be passed any invalid paths.
    Do not use built-in path-related functions.

For example:

    path = Path('/a/b/c/d')
    path.cd('../x')
    print(path.current_path)
    
should display '/a/b/c/x'
"""

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        if not new_path.strip():
            self.current_path = "/"
            return
        elif new_path.startswith("/"):
            current_path = ['']
            new_path = new_path[1:]
        else:            
            current_path = self.current_path.split('/')
        index = len(current_path)
        for dirname in new_path.split("/"):
            if dirname == "." or dirname == "":
                continue
            elif dirname == "..":
                if index > 0:
                    index -= 1
            elif dirname.isalpha():
                if index < len(current_path):
                    current_path[index] = dirname
                else:
                    current_path.append(dirname)
                index += 1                    
            else:
                raise ValueError("abstract: cd: {}: No such file or directory"
                                 .format(new_path))
        self.current_path =  "/".join(current_path[:index])
        if not self.current_path.startswith("/"):
            # FIXME remove this fix and write better code
            self.current_path = '/' + self.current_path

if __name__ == '__main__':
    path = Path('/a/b/c/d')
    print(path.current_path)
    path.cd('../x') # /a/b/c/x
    print(path.current_path)
    path.cd('/../x') # x
    print(path.current_path)
    path = Path('/a/b/c/d')    
    path.cd('..')
    print(path.current_path)

