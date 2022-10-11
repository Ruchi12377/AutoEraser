import os
import sys

#extract python file of rt component via listdir
for f in [f for f in os.listdir("./") if os.path.isdir(os.path.join("./", f)) & os.path.isfile("./{0}/{0}.py".format(f)) & ((f in sys.argv) == False)]:
    r = open("./{0}/{0}.py".format(f), 'r')
    c = r.read()
    r.close()
    p = open("./{0}/{0}.py".format(f), 'w')
    p.write(c.replace('    ', '\t'))
    p.close()

print("Done")