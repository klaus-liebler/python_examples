from pathlib import Path
from datetime import datetime
import os
myPath = Path("c:\\", "repos", "sensact")
print("OS-spezifischer Pfad:", myPath, "existiert" if  myPath.exists() else "existiert nicht")
deeperPath= myPath / "hardware" / "test.txt"
print("OS-spezifischer tieferer Pfad 2:", deeperPath)

print("CurrentWorkingDirectory:", Path.cwd())
newCwd = Path.cwd() / "test01"
os.chdir(newCwd)
print("CurrentWorkingDirectory:", Path.cwd())
os.makedirs(newCwd / datetime.now().strftime("%Y%m%d_%H%M%S"))
test_path = Path.cwd() / "test.txt"
if test_path.exists() and test_path.is_file():
    print("Die Testdatei existiert!")
else:
    print("Die Testdatei existiert NICHT!")
for file_or_directory in os.listdir(Path.cwd()):
    print(file_or_directory)
