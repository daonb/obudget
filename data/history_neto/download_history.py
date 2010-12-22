import os
import re
import csv
import json

baseurl = 'http://www.ag.mof.gov.il'
xls = re.compile('[^"\']+xls')

for fn in ['history0.html','history1.html']:
    data = file(fn).read()
    xlss = xls.findall(data)
    for x in xlss:
        #print os.popen('wget %s%s' % (baseurl, x)).read()
        x = x.split('/')[-1]
        x1 = x.split('.')[0]+'.csv'
        #print os.popen('xls2csv %s | tail -n+14 > %s' % (x, x1)).read()

out = file('history.json','w')

for y in range(1992,2010):
    fn = 'history%d.csv' % y
    r = csv.reader(file(fn))
    for l in r:
        name = l[0].strip()
        if name == "": continue
        code,title = name.split('-',1)
        code=code.strip()
        title=title.strip()
        try:
            allocated = int(l[1])
        except:
            allocated = None
        try:
            revised = int(l[2])
        except:
            revised = None
        try:
            used = int(l[3])
        except:
            used = None
        if code == '0000':
            income_allocated = allocated 
            income_revised = revised 
            income_used = used
            title = 'הכנסות המדינה'            
        if code == '00':
            allocated -= income_allocated 
            revised -= income_revised 
            used -= income_used
            title = 'המדינה'            
        if code.startswith('0000'):
            allocated = -allocated
            revised = -revised
            used = -used
        j = { 'year':y, 'code' : code, 'title' : title, 'net_allocated' : allocated, 'net_revised' : revised, 'net_used' : used }
        out.write(json.dumps(j)+'\n')
        