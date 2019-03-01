from urllib import request
from bs4 import BeautifulSoup
import os
def main():
	dic=load_in().split("\n")
	print("Display all words")
	display(dic)
	ans=merriam_webster(dic)
	print("Display definitions")
	display(ans)
	write_in(ans)

def load_in():
	try:
		f = open('./txt/input.txt', 'r')
		dic=f.read()
		f.close()
		return dic
	except IOError:
		print("cannot find input file")
		exit(1)

def write_in(ans):
	with open('./txt/output.txt','w+') as fp:
		for ele in ans:
			fp.write(ele+" "+ans[ele]+"\n")
			print("writing "+ele+"'s definitions...")
		fp.close()
	print("write done")

def merriam_webster(dic):
	ans=dict()
	for word in dic:
		url="https://www.merriam-webster.com/dictionary/"+word
		print("requesting "+url+"...")
		req=request.urlopen(url)
		req=req.read()
		print("requested succeeded")
		soup=BeautifulSoup(req,'html.parser')
		try:
			dif=soup.find_all('span',class_="dtText")[0].text.split('\n')[0].strip(':')
			print("word: "+word)
			print("deffinition: "+dif)
			ans[word]=dif
		except:
			print("cannot find definitions")
		print()
		
	return ans

def display(dic):
	print("---------------------------")
	for ele in dic:
		try:
			print(ele+dic[ele])
		except:
			print(ele)
	print("---------------------------")


if __name__ == '__main__':
	main()
