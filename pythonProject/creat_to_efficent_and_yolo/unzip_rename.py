import os
from tqdm import tqdm
filename='/home/zhen/Desktop/useway_1_needtofilter/'

# for root,dir,files in os.walk(filename):
#     for d in  dir:
#         for r , d1 , f in os.walk(os.path.join(filename,d)):
#             for ff in f:
#                 print(os.path.join(filename,d)+'/'+ff)
#                 print(filename+ff)
#                 os.rename(os.path.join(filename,d)+'/'+ff,filename+ff)
#         os.rmdir(os.path.join(filename,d))
