import json
import csv
import os
import re

if __name__ == '__main__':
    filenames_in = './home/runner/work/kkrcyrCN/paratranz/'
    filenames_out = '/home/runner/work/kkrcyrCN/csv/'
    pathDir = os.listdir(filenames_in)
    for allDir in pathDir:
        child = re.findall(r"(.+?).json",allDir)
        output_name = filenames_out.join(child) + '.csv'
        domain = os.path.abspath(filenames_in)
        info = os.path.join(domain, allDir)
        domain1 = os.path.abspath(filenames_out)
        outfo = os.path.join(domain1,output_name)
        f = open(info,newline='\n',encoding='utf-8-sig')
        data = json.load(f)
        with open(outfo, 'w', newline='\n', encoding='utf-8-sig') as f:
            writer = csv.writer(f);
            for item in data:
                writer.writerow([item['context'], item['original'],item['translation'],item['id'],item['file'],item['extra'],item['project'],item['key']])
    f.close()
