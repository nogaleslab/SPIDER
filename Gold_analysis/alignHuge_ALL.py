#!/usr/bin/env python

import os
import shutil
import glob
import re
import subprocess

list = glob.glob("*en.mrc")

for en in list:
	
	ef = re.sub("en","ef",en)
	efAli = re.sub("en","efAli",en)
	
	cmd="alignhuge %s %s %s" %(ef,en,efAli)
	#system("proc2d %s.xmp %s.img"%(file,file))
	subprocess.Popen(cmd,shell=True).wait()