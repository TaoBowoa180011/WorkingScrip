import pandas as pd
import os
global num_lidclose
global num_lidopen
global num_lidopenwithobj
global num_wash

lidclose=[]
lidopen=[]
lidopenwithobj=[]
wash=[]
device_number=[]



# df=pd.DataFrame({'device_number','num_lidclose','num_lidopen','num_lidopenwithobj','num_wash'})

# for root,dir,files in os.walk("finalfile/"):
#     for d in dir:
#         for r , d1 ,fs in os.walk("finalfile/"+d):
#             if fs != []:
#                 num_lidclose=len(list(filter(lambda x:x.split('_')[-3]=='lidclose',fs)))
#                 num_lidopen=len(list(filter(lambda x:x.split('_')[-3]=='lidopen',fs)))
#                 num_lidopenwithobj=len(list(filter(lambda x:x.split('_')[-3]=='lidopenwithobj',fs)))
#             else:
#                 num_lidclose=num_lidopen=num_lidopenwithobj=0
#         dst='valid2/'+d
#         if not os.path.isdir(dst):
#             num_wash=0
#         else:
#             for rr, dd1 ,ffs in os.walk(dst):
#                 num_wash=len(ffs)
#         lidclose.append(num_lidclose)
#         lidopen.append(num_lidopen)
#         lidopenwithobj.append(num_lidopenwithobj)
#         device_number.append(d.split('_')[1])
#         wash.append(num_wash)
#         # print(d)
#         # print('num_lidclose:'+str(num_lidclose))
#         # print('num_lidopen:'+str(num_lidopen))
#         # print('num_lidopenwithobj:'+str(num_lidopenwithobj))
#         # print('num_wash:'+str(num_wash))
# file=pd.DataFrame({'device_number':device_number,'num_lidclose':lidclose,'num_lidopen':lidopen,'num_lidopenwithobj':lidopenwithobj,'num_wash':wash})
# file.to_csv('device_num.csv')
flag=0
for root,dir,files in os.walk("finalfile/"):
    flag+=len(files)
print(flag)