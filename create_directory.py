import os

#-----------Function------------------#
def createdirectory(folder):
    try:
        if not os.path.exists(folder):
            os.makedirs(folder)
            print ('Creating directory sucess ' + folder)
    except OSError:
        print ('Error creating the folder' + folder)
#-------------------------------------#
createdirectory('master_dir')
#-------------------------------------#
os.chdir('./master_dir')
obj = '20180801,20180802,20180803,20180804,20180805'
print (obj.split(','))
for obj1 in obj.split(','):
    print (obj1)
    if not obj1 is None:
        createdirectory(obj1)
    else:
        print ('ERROR: Directory creation failed' + obj1)
