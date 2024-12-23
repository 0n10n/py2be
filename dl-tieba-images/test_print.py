import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)
print(parent_dir)
pass

from utils.tools import print_msg

print_msg('hello','world',sep=',')    

