from itertools import groupby
import requests
import os
from tqdm import tqdm

with open('2021-01-19-17-35-42_EXPORT_CSV_2007555_660_0.csv','r')as txt:
    lines = txt.readlines()
res = [list(i) for j, i in groupby(lines, lambda a: a.split(',')[0])]
res = res[1:]
for group in tqdm(res):
    try:
        video = group[3]
    except Exception:
        video = group[0]
    url = video.split(',')[1].strip('\"')
    did = video.split(',')[0].strip('\"')
    vidname = url.split('/')[0]
    r = requests.get(url, allow_redirects=True)
    if not os.path.exists(os.path.join(os.getcwd(),'videos',did)):
        os.makedirs(os.path.join(os.getcwd(),'videos',did))
    open(os.path.join(os.getcwd(),'videos',did,vidname), 'wb').write(r.content)