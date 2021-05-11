import os
from tqdm import tqdm
'''creat label'''
for root,dir,files in tqdm(os.walk("unzip/")):
    for d in dir:
        if d[-1] !='a':
            """zai objnames zhong """
            with open("unzip/" + d + '/obj.names' ) as t_xt:
                contexts = t_xt.readlines()
            for index,context in enumerate (contexts):
                if context=='sink\n':
                    sink=index
                if context=='lidopenwithobj\n':
                    lidopenwithobj=index
                if context=='lidclose\n':
                    lidclose=index
                if context=='lidopen\n':
                    lidopen=index
                if context=='wash\n':
                    wash=index
            # print(contexts)
            project_list=[lidopen,lidclose,sink,lidopenwithobj,wash]
            targetdir=os.path.join(root,d,'obj_train_data')
            files_obj_train_data=os.listdir(targetdir)
            for file_obj_train_data in files_obj_train_data:
                if file_obj_train_data[-3:]=='txt':
                    # print(file_obj_train_data)
                    with open(targetdir+'/'+file_obj_train_data,'r') as obj_txt:
                        obj_txt_contexts=obj_txt.readlines()
                    output=[]
                    for obj_txt_context in obj_txt_contexts:
                        obj_txt_context_new=str(project_list.index(int(obj_txt_context[0])))+obj_txt_context[1:]
                        output.append(obj_txt_context_new)
                    with open(targetdir+'/'+file_obj_train_data,'w') as obj_txt:
                        for line in output:
                            print(line)
                            obj_txt.write(line)
