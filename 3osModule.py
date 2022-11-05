#OS module in python
import os
os.chdir('/Users/khine/Desktop/')
# os.mkdir('OS-Demo-2/Sub-Dir-1')#error
# os.makedirs('OS-Demo-2/Sub-Dir-1')#recommend this for developer
print(os.listdir())

#deleting folder
#for mkdir
# os.rmdir('OS-Demo-2')
# print(os.listdir())

#deleting folder
#for makedirs
os.removedirs('OS-Demo-2/Sub-Dir-1')
print(os.listdir())
