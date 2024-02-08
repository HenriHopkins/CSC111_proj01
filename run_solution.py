import sys
import subprocess
p = subprocess.getoutput("{} ./adventure.py < everyitem.txt".format(sys.executable))
print(p)
