import os
import sys
import io
import datetime

dataFile = open('data.txt', 'w')

time = datetime.datetime.now().strftime('%d/%m/%y %I:%M %S %p')

dataFile.write('hello world! ' + time)

print(sys.argv)

