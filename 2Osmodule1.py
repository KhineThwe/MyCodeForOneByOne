#OS module in python
import os
current = os.getcwd()
print("Current Working Directory ",current)
os.chdir('/Users/khine/Desktop/')
print(os.getcwd())
