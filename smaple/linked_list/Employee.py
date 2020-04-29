'''
Created on 14-Apr-2020

@author: navbharti
'''

class Employee(object):
    '''
    classdocs
    '''
    id = 0;
    name = None
    def display (self):  
        print("ID: %d \nName: %s"%(self.id,self.name)) 
    
    def __init__(self, id, name):
        '''
        Constructor
        '''
        self.id = id
        self.name = name
        
emp = Employee(10, 'Naveen Kumar')  
emp.display()  