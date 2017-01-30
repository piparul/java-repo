def findPanagram(str):
	dict1={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0,'h':0,'i':0,'j':0,'k':0,'l':0,'m':0,'n':0,'o':0,'p':0,'q':0,'r':0,'s':0,'t':0,'u':0,'v':0,'w':0,'x':0,'y':0,'z':0}
	s=str.lower()
	for c in s:
		if c not in dict1:
			dict1.update({c:1})
		else:
			value=dict1.get(c)
			value+=1
			dict1.update({c:value})
	absent=0
	for key,value in dict1.iteritems():
		#print key,value
		if value==0:
			absent+=1
	#print 'absent: ',absent
	if absent==0:
		return 'pangram'
	else:
		return 'not pangram'
		


a = raw_input().strip()
print findPanagram(a)