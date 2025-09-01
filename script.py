# this will be a script that will be solunk will use to extract information out of the 


# libs and config setting.....

import pandas as pd 
import re
import datetime
import pathlib



 # working on geeting the log info to another file and extracting>>>
file_object = open('sample_logs.txt', 'r')

new_da = file_object.readlines()

#print(len(new_da))
#print("First log entry:", new_da[0])

for log_line in new_da:
    if "logout" in log_line.lower():
        logout_count += 1
    if "login" in log_line.lower():
        login_count += 1
    if "[ERROR]" in log_line:
        error_count += 1

print("Number of logout events:", logout_count)
print("Number of login events:", login_count)
print("Number of error events:", error_count)
