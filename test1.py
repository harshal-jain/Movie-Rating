
import sys
from project import *

def main(argv):
    mystr=sys.argv[1]
    
    a = final(mystr)
    
    print(a[0])

if(__name__=="__main__"):
    main(sys.argv[1:])




