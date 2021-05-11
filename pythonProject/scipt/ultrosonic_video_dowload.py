import os
import pandas as pd
import ast
import requests
from tqdm import tqdm

# df = pd.read_csv('ultraundetacted_03-22.txt')
#
#
# for index, row in tqdm(df.iterrows()):
#     did = row['device_id']
#     url = row["video_url"]
#     filename = url.split('/')[-1]
#     r = requests.get(url, allow_redirects=True)
#     video_store_path = os.path.join('/home/zhen/Downloads/ultrosonic_undetected',filename)
#     open(video_store_path, 'wb').write(r.content)
path = '/home/zhen/Downloads/ultrosonic_undetected'
deviceid = []
device_list = os.listdir(path)

for d in device_list:
    id = d.split('_')[0]
    deviceid.append(id)
print(deviceid)