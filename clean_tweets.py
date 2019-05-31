# Author: Mohammad Rasooli, Noura Farra
import re,os,sys,codecs
#from urlparse import urlparse
from urllib.parse import urlparse


rep = '' if len(sys.argv)<4 else sys.argv[3].strip()

writer = codecs.open(os.path.abspath(sys.argv[2]),'w')
c = 0
for line in codecs.open(os.path.abspath(sys.argv[1]),'r'):
#    line = line.decode('utf-8','ignore').encode("utf-8")
    #line = line.replace("#", "");
   # line = line.replace("RT", "");
    #line = line.replace("RT","rt");
    line = line.strip()
    line = line.replace("\"", "")
#    line = line.replace("\"", "\"\"")	 
    
    line = line.lower()
   # line = re.sub(r'http[.]\b', "LINK", line);
   # line = re.sub(r'https[.]\b', "LINK", line);
  #  out = ' '.join([e if not urlparse(e).scheme else rep for e in line.split()])
  #  out = ' '.join([e  for e in out.split() if not e.startswith('@')])
  #  out = ' '.join([e  for e in out.split() if not e.startswith('@')])
    #out = ' '.join([e  for e in out.split() if not e.startswith('#')])
   # line = re.sub(r'^https?:\/\/.*[\r\n]*', '', line, flags=re.MULTILINE)
    line = re.sub(r'http\S+', '', line)
    line = line.replace('&quot;','"').replace('&amp;','\'').replace('&lt;','<').replace('&gt;','>')
    writer.write(line+'\n')
    c+=1
    if c%10000==0: sys.stdout.write(str(c)+'...')

writer.close()
print('done!')
