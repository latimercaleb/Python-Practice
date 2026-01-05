# Simple script automation
import time
import os

sourceFldr = ["C:\\Users\Caleb\Desktop\Test"]
targetFldr =  'C:\\Users\Caleb\Desktop\TestBak'

target = targetFldr + os.sep + \
         time.strftime ('%Y%D%M%H%M%S') + '.zip'
print (targetFldr)
if not os.path.exists(targetFldr):
    os.mkdir(targetFldr)

zip_cmd = 'zip -r {0} {1}'.format(target,''.join(sourceFldr))
print (zip_cmd)
if os.system(zip_cmd) ==  0:
    print("Backed up")
else:
    print("err")
