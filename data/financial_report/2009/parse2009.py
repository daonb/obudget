import csv
import json

f = csv.reader(file('2009.csv'))
out = file('out.json','w')

lengths = [2,4,6,8]

planned_p = {}
used_p = {}

for l in f:
    code, title, planned, used = l[0], l[1], l[2], l[4]
    if code.strip() == '' or len(code) != 8:
        continue
    code = '00' + code.strip()
    try:
        planned = int(planned.replace(',',''))/1000
    except:
        planned = None
    try:
        used = int(used.replace(',',''))/1000
    except:
        used = None
    out.write( json.dumps( {'year':2009,'code':code, 'title':title, 'gross_revised':planned, 'gross_used':used})+'\n' )
    for g in lengths:
        if code.startswith('0000') and g == 2:
            continue
        sc = code[:g]
        if planned != None:
            planned_p[sc] = planned_p.get(sc,0) + planned
        if used != None: 
            used_p[sc] = planned_p.get(sc,0) + planned 

k = list(set(planned_p.keys() + used_p.keys()))
k.sort(key=lambda x:"%02d%10s" % (10-len(x),x))
for key in k:
    out.write( json.dumps( {'year':2009,'code':key, 'gross_revised':planned_p.get(key), 'gross_used':used_p.get(key)})+'\n' )
