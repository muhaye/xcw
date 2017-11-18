#!/usr/bin/env python3
from subprocess import Popen, PIPE, run
import re
import os
cmd = "xcodebuild  -list"

cfinal = ['xcodebuild', '-workspace', '$workspace', '-scheme', '${scheme}', 'build']
for file in os.listdir("./"):
    if file.endswith(".xcworkspace"):
        cfinal[2] = file
        break

p = Popen(cmd , shell=True, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
if ( p.returncode == 0 ) :
    outstri = out.rstrip().decode('utf-8')
    m = re.search('[\n\r][ \t]*Schemes:\n[ \t]*([^\n\r]*)', outstri)
    scheme = m.group(1)
    print("Executing sheme : %s"% scheme)
    cfinal[4] = scheme 
    print(*cfinal)
    run(cfinal) 
else:
    print("Error %s"% (err.rstrip()))
