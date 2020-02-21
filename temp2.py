import os.path, time
import glob
import pandas as pd
import tkinter
from tkinter import filedialog
from tkinter import simpledialog

##dialog window file chose
root = tkinter.Tk()
root.withdraw()

def file_path():

    tempdir = filedialog.askdirectory()
    if len(tempdir)>0:
        print("You chose: %s" % tempdir)
    return tempdir

file = file_path()

#file = input("Write folder directroy: ")
file_list=(file+'/')
def file_type():
    temptype = simpledialog.askstring(title="Set file types", prompt="jpg, txt, *, ")
    if len(temptype)>0:
        print("You chose: %s" % temptype)
    return temptype
ftype = file_type()

#ftype = input("Write files type(jpg, txt, .*): ")

list1 = glob.glob(file+"/*."+ftype)
list2=[]

##gather creation date and time
for i in range (len(list1)):
    list2.append(time.ctime(os.path.getctime(list1[i])))

zipObj=zip(list1, list2)
db=dict(zipObj)

##create panda df
pdb = pd.DataFrame.from_dict(db,orient="index")
print(pdb)

##replace name
for k in range (len(list1)):
    dst =file_list + list2[k]+".txt"
    os.rename(list1[k],dst)

print("Done")




