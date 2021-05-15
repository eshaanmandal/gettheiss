import requests
from datetime import datetime, time
import sys,time

''' A module which helps in obtaining the data from iss and using it in your python programs'''

class ISS:
    def __init__(self, url):
        '''Initializes what url to use'''
        self.url = url
    
    @property
    def sat_data(self):
        if requests.get(self.url).status_code in range(200,202):
            return requests.get(self.url).json()
        return -1


    def fetch_data(self, times = 1):
        '''Prints the '''
        json_data=[]
        
        for _ in range(times):
            d = self.sat_data
            if d != -1 :
                json_data.append(d)
                time.sleep(3)
            
        return json_data

        
                
    def __repr__(self):
        return f"ISS({self.url})"




iss = ISS('https://api.wheretheiss.at/v1/satellites/25544')


# print(iss.fetch_data(2))


print(iss.sat_data)
