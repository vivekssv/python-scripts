#!/usr/bin/python
#%%
class window():
#     def __init__(self,name):
#         print("During Object Initialization", name)
#         self.name = name
#         print("After name inti", self.name)
    def __init__(self,name,id,joiningdate):
        self.name = name
        self.id = id
        self.joiningdate = joiningdate
    def change_name(self,new_name,new_id):
        self.name = new_name
        self.id = new_id

os = window("windowxp",1,20181011)
#glass = window("mirrors",3)
#krish = window("Radhakrishnan",115)
print(os.name,"\t",os.id,os.joiningdate)
print(glass.name,"\t",glass.id)
print(krish.name, "\t",krish.id)
glass.name = "vino"
glass.id = 360
print(glass.name,glass.id)
setattr(glass, 'name', "ravi")
print(glass.name,getattr(glass,'id'))


#%%



