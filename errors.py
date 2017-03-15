from models import *

file = None

try:
    file = open('not-exists.csv','r')
    print('file open')
    values = file.readLine().split(':')
    Profile(*valores)
    file.close()
except IOError as error:
    print('Error reading file')
except TypeError as error:
    print('Invalid type')
finally:
    if(file is not None):
        print('Closing file')
        file.close()
