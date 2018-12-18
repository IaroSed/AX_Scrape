import sys
import re
import urllib.request as urllib
import encodings
import time
import numpy
import random


File_in = open('Update_20180928.txt', 'r')
File_out1 = open('Appexchange new part1 20180928.txt', 'a', encoding='utf-8')
File_out2 = open('Appexchange new part2 20180928.txt', 'a', encoding='utf-8')

Links=list()
#print(File_in.read())

rr=str.join(" ", str(File_in.read()).splitlines())


PA = re.findall('<li>(.*?)</li>',rr)


print(len(PA))

for p in PA:

	NA = re.findall('data-listing-name="(.*?)"', str(p))
	
	if len(NA)==0:
		NA = ["N/A"]
	print(NA)
	
	ID = re.findall('data-listing-id="(.*?)"',str(p))
		
	if len(ID)==0:
		ID = ["N/A"]
	print(ID)
		
	LI = re.findall('data-listing-url="(.*?)"',str(p))
		
	if len(LI)==0:
		LI = ["N/A"]
	print(LI)
	
	File_out1.write(str(NA[0])+"^"+str(ID[0])+"^"+str(LI[0])+"\n")

	Links.append(str(LI[0]))


#print(len(Links))

	
File_out1.close()
File_in.close()

for link in Links:
	e=0
	d=0
	while d<3:
		try:
			print("Reading page: "+str(link))
			r = urllib.urlopen(link).read()
			break
		except:
			print("Oops!  Error occured.. Sleeping for 30 seconds and then trying again!")
			d=d+1
			time.sleep(30)

	PU = re.findall('<p class="appx-page-header-link">By (.*?)</p>',str(r))
	
	if len(PU)==0:
		PU = ["N/A"]
	print(PU)

	DA1 = re.findall('First Release(.*?)Latest Release', str(r))
	
	if  len(DA1)==0:
		e=1
		DA1 = re.findall('Listed On(.*?)</div>', str(r))
	
	if e==1:
		DA = re.findall('<p>(.*?)</p>', str(DA1[0]))
	else:
		DA = re.findall('<div class="appx-extended-detail-subsection-description">(.*?)</div>', str(DA1[0]))
	
	
	if len(DA)==0:
		DA = ["N/A"]
		
	print(DA)
	
	CA1 = re.findall('>CATEGORIES</p>(.*?)</div>',str(r))
	
	CA = re.findall('<strong>(.*?)</strong>',str(CA1))
	
	if len(CA)==0:
		CA = ["N/A"]
	
	
	
	
	File_out2.write(link+"^"+str(PU[0])+"^"+str(DA[0])+"^"+str(CA[0])+"\n")
	
	
File_out2.close()


