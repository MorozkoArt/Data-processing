import os
from common.subfolderNotFoundWarning import subfolderNotFoundWarning

def subfolderPaths(root, subfolders):
    left = subfolders.copy()
    paths = []
    for item in os.listdir(root):
        path = os.path.join(root, item)
        if os.path.isdir(path):
            if item in subfolders:
                paths.append(path)
                left.remove(item)
    for item in left:
        subfolderNotFoundWarning(item)
    return paths