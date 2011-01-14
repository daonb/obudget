import csv
import json

f = csv.reader(file('2011.csv'))
out = file('out.json','w')

for l in f:
    print l
    try:
        code, title, net, tar = l[0], l[1], l[2], l[3]
    except:
        continue

    code = "00"+code.strip()
    net = int(net)
    gross = net + int(tar)
    
    out.write( json.dumps( {'year':2011,'code':code, 'title':title, 'net_allocated':net, 'gross_allocated':gross})+'\n' )
