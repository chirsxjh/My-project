import os
import sys
import commands
import pdb


cmds = ('python {}'.format(sys.argv[1]))
#res = os.system(('python {}'.format(sys.argv[1])))



 
result=  commands.getstatusoutput(cmds)
#if result[]
print result[0]

pdb.set_trace()
if result[0] == 256:
    print result[1][40:]
    

#print (result[0])
#print ('it ok')