import time
import random

'''
urating  = dict()
infile = open('us.txt')
for line in infile.readlines():
	arr = line.strip().split('\t')
	uid = arr[0]
	sid = arr[1]
	if uid not in urating:
		urating[uid] = set()
	urating[uid].add(sid)
infile.close()

for uid in urating:
	print len(urating[uid])
		

uset = set()
uid_nuid = dict()
infile = open('user')
for line in infile.readlines():
	arr = line.strip().split('\t')
	uid_nuid[arr[0]] = arr[1]
	uset.add(arr[0])
infile.close()

sset = set()
sid_nsid = dict()
infile = open('shop')
for line in infile.readlines():
	arr = line.strip().split('\t')
	sid_nsid[arr[0]] = arr[1]
	sset.add(arr[0])
infile.close()

rating_dict = dict()
infile = open('/data1/dataset/dianping/data1_fromshop/final_data/review_content')
for line in infile.readlines():
	arr = line.strip().split('\t')
	uid = arr[1]	
	sid = arr[2]	
	if uid in uset and sid in sset:
		nuid = uid_nuid[uid]
		nsid = sid_nsid[sid]
		timestr = arr[11]
		if timestr == 'NULL':
			addtime = 0
		else:
			addtime = time.mktime(time.strptime(timestr,'%Y-%m-%d %H:%M:%S')) 
		rating = int(arr[7])
		if rating == 0:
			continue
		rating /= 10
		key = nuid+'_'+nsid
		if key not in rating_dict:
			rating_dict[key] = list()
			rating_dict[key].append(addtime)
			rating_dict[key].append(rating)	
		else:
			if addtime > rating_dict[key][0]:
				rating_dict[key][0] = addtime
				rating_dict[key][1] = rating	
infile.close()

print len(rating_dict)
outfile = open('tmp.txt','w')
for key in rating_dict:
	arr = key.strip().split('_')
	uid = arr[0]
	sid = arr[1]
	rating = str(rating_dict[key][1])
	outfile.write(uid+'\t'+sid+'\t'+rating+'\n')
outfile.close()	
'''	

	
infile = open('userve.txt.bak')
outfile = open('userve.txt','w')
for line in infile.readlines():
	if random.random()<0.687:
		outfile.write(line)
infile.close()
outfile.close()
