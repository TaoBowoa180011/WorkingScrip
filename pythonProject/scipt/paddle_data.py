import os

lines = []
for root,dirs,files in os.walk('/home/zhen/PycharmProjects/workingscripts/autocollection/hand_classify_dataset/train'):
    for idx, d in enumerate(dirs):
        fs = os.listdir(os.path.join(root,d))
        for f in fs:
            line = "{} {}"

            line = line.format(os.path.join('train',d,f), idx)
            lines.append(line+'\n')
    break
print()
with open('/home/zhen/PycharmProjects/workingscripts/autocollection/hand_classify_dataset/train_list.txt', 'a') as txt:
    txt.writelines(lines)