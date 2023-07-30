import os
import datetime
import shutil
months={
    1:"JAN",
    2:"FEB",
    3:"MAR",
    4:"APR",
    5:"MAY",
    6:"JUN",
    7:"JUL",
    8:"AUG",
    9:"SEP",
    10:"OCT",
    11:"NOV",
    12:"DEC",
        }
def getMonthAndYear(file_path):
    try:
        file_stat = os.stat(file_path)
        timestmp = file_stat.st_mtime
        last_modified_datetime = datetime.datetime.fromtimestamp(timestmp)
        year = last_modified_datetime.year
        month = last_modified_datetime.month
        return [month,year]
    except FileNotFoundError:
        print("File not found!!!")
        return None
    except OSError:
        print("An error occurred while accessing the file.")
        return None

folder_path = input("Enter folder name: ")
dstn_folder_path = input("Enter destination folder name: ")

if not os.path.exists(dstn_folder_path):
    os.mkdir(dstn_folder_path)
else:
    print("Folder already exists!")
#List of all the files in the folder
files_in_folder = os.listdir(folder_path)
for file in files_in_folder:
    path = folder_path+"/"+file
    month = months[getMonthAndYear(path)[0]]
    year = getMonthAndYear(path)[1]
    dstn_path = dstn_folder_path+"/"+str(year)
    if not os.path.exists(dstn_path):
        os.mkdir(dstn_path)
    dstn_path += "/"+month
    if not os.path.exists(dstn_path):
        os.mkdir(dstn_path)
    shutil.copy(path, dstn_path)

print("PROCESS SUCCESSFULLY COMPLETED!")