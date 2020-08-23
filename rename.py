import os
import sys

  
CURRENT_PATH = os.path.abspath(os.getcwd()) + '/'
arr = []
ind = []
for filename in os.listdir(CURRENT_PATH):
    if(filename.__contains__('indian_model')):
        for img in os.listdir(CURRENT_PATH + filename):
            print(filename)
            os.rename(CURRENT_PATH + filename+ '/'+ img, CURRENT_PATH + 'indian_mode'+ '/'+ img )
        # exit(0)
