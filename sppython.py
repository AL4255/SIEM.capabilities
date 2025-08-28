# this will be a script that will be solunk will use to extract information out of the 


# libs and config setting.....

import pandas as pd 
import re
import datetime
import pathlib



 # working on geeting the log info to another file and extracting>>>
file_object = open('sample_logs.txt', 'r')

new_da = file_object.readlines()

print(len(new_da))

print("First log entry:", new_da[0])
