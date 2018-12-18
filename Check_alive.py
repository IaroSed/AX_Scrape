import sys
import urllib.request as urllib
import encodings
import time
import random
import pandas as pd
import numpy as np


File_out = open('Results_checkalive.txt', 'w')

df_link = pd.read_excel("SF_links_mod.xlsx",encoding='utf-8')
df_link_list = df_link['Link'].tolist()

for link in df_link_list:
	e=0
	d=0
	while d<3:
		print(d)
		try:
			print("Reading page: "+str(link))
			r = urllib.urlopen(link).read()
			File_out.write(link+"^"+"OK"+"\n")
			break
		except:
			print("Oops!  Error occured.. Sleeping for 10 seconds and then trying again!")
			d=d+1
			File_out.write(link+"^"+"KO"+"\n")
			#time.sleep(1)	
	
File_out.close()