'''
Created on 14-Apr-2020

@author: navbharti
'''
class Node(object):
    '''
    classdocs
    '''
    data = 0
    next = None
    
    def __init__(self, params):
        '''
        Constructor
        '''
        self.data = params
        self.next = None
        
    def display(self):
        print("Node Data: %d"%(self.data)) 
        