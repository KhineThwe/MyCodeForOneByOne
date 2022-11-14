#OS module in python
import os
os.chdir('/Users/khine/Desktop/')
print(os.environ.get("USERPROFILE"))#HOME
file_path = os.path.join(os.environ.get("USERPROFILE"),'test.txt')
print(file_path)
print(os.getlogin())
print(os.path.dirname('/tmp/test.txt'))#it will return directory name
print(os.path.basename('/tmp/test.txt'))#it will return base name
print(os.path.split('/tmp/test.txt'))#will return base+directory
