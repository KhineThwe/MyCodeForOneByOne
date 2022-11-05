#OS module in python
import os
from datetime import datetime
os.chdir('/Users/khine/Desktop/')
#entire directories တစ်ခုလုံးမှာရှိတဲ့ကောင်တွေကိုပြန်ပြပေးတယ်
for dirpath,dirnames,filenames in os.walk("/Users/khine/Desktop/"):
    print("Current Path:",dirpath)
    print("Directories:", dirnames)
    print('Files: ',filenames)

