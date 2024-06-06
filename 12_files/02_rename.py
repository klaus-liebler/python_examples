import pathlib
import os
fileA = pathlib.Path.cwd() / "renameMe_A.txt"
fileB = pathlib.Path.cwd() / "renameMe_B.txt"
if fileA.exists() and fileA.is_file() and not fileB.exists():
    print("A in B umbenennen")
    os.rename(fileA, fileB)
elif fileB.exists() and fileB.is_file() and not fileA.exists():
    print("B in A umbenennen")
    os.rename(fileB, fileA)
else:
    print("Unerwarteter zustand!")   

