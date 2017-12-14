#coding=utf-8
import jieba
import pandas as pd
 
def getext():
	mydata_txt = pd.read_csv('C:\\Users\\skyamz\\Desktop\\paipaidai_segmentation\\PPDWords.txt', sep='\n')
	return mydata_txt

def fenci(text):
	_STOP_WORD = set()
	for line in open('Chinese_stop.txt'):
	    line = line.decode('utf-8','ignore')
	    line = line.strip("\n")
	    _STOP_WORD.add(line)
	word_list = []
	words = list(jieba.cut(text))#seperate the word
	for vob in words:
		if vob in _STOP_WORD:
		    continue
		elif vob.isdigit():
		    continue
		word_list.append(vob)
	seg = " ".join(word_list)
	return seg
post_list = getext()
print post_list
with open('Sentence.txt','w') as f:
	for post in post_list:
		f.write(fenci(post).encode("utf-8")+'\n')