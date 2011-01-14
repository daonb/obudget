### encoding: utf8

import csv
import json

f = csv.reader(file('state-budget.csv'))
out = file('out.json','w')

lengths = [2,4,6,8]

net_p = {}
gross_p = {}
lastcode = None

f.next()
f.next()

parent_titles = {'00': 'המדינה'}

for l in f:
    p_codes = ['','','']
    p_titles = ['','','']
    try:
        p_codes[0],p_titles[0], p_codes[1],p_titles[1], p_codes[2],p_titles[2], code, title, net, tar = l[0],l[1],l[2],l[3],l[4],l[5],l[6], l[7], l[13], l[14]
    except:
        print l
        continue
    if code.strip() == '':
        if lastcode != None:
            code = lastcode
        else:
            continue
    else:
        code = code.strip()
        code = ((10-len(code))*"0") + code
        
    for p in range(3):
        p_code = p_codes[p].strip()
        p_title = p_titles[p].strip() 
        if p_code != '':
            p_code = (((p+2)*2-len(p_code))*"0") + p_code
            if p_title != '':
                parent_titles[p_code] = p_title
    
    lastcode = code        
               
    try:
        net = int(net)
    except:
        continue
    try:
        gross = net + int(tar)
    except:
        gross = None
    out.write( json.dumps( {'year':2010,'code':code, 'title':title, 'net_allocated':net, 'gross_allocated':gross})+'\n' )
    for g in lengths:
        if code.startswith('0000') and g == 2:
            continue
        sc = code[:g]
        if net != None:
            net_p[sc] = net_p.get(sc,0) + net
        if gross != None: 
            gross_p[sc] = gross_p.get(sc,0) + gross 

k = list(set(net_p.keys() + gross_p.keys()))
k.sort(key=lambda x:"%02d%10s" % (10-len(x),x))
for key in k:
    try:
        title = parent_titles[key]
        out.write( json.dumps( {'title':title, 'year':2010,'code':key, 'net_allocated':net_p.get(key), 'gross_allocated':gross_p.get(key)})+'\n' )
    except:
        print 'parent title: %s' % key
