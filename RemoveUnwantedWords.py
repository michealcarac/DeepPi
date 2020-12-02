import shutil

#WARNING:
#This is irreversible, so make sure to have a backup beforehand 
#Establish what words you do not want
words =  [] #Example: ['sheila','bed']
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#to delete unwanted files
#Remove the # for this section if you don't need to delete files, this will comment out the section
#'''
i = 0
while i < len(words):
	shutil.rmtree(words[i])
	i = i + 1
#'''
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#to correct testing_list.txt
f = open('testing_list.txt','r') #Change if different txt file
lst = []
for line in f:
	for word in words:
		if word in line:
			line = line.replace(line,'')
	lst.append(line)
f.close()
f = open('testing_list.txt','w')#Change if different txt file
for line in lst:
	f.write(line)
f.close()
#--------------------------------------------------------------------------
#--------------------------------------------------------------------------
#to correct validation_list.txt
f = open('validation_list.txt','r')#Change if different txt file
lst = []
for line in f:
	for word in words:
		if word in line:
			line = line.replace(line,'')
	lst.append(line)
f.close()
f = open('validation_list.txt','w')#Change if different txt file
for line in lst:
	f.write(line)
f.close()
