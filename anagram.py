import math

def number_needed(a, b):
	dict1={}
	dict2={}
	for c in a:
		if c not in dict1:
			dict1.update({c:1})
		else:
			count1=dict1.get(c)
			count1+=1
			dict1.update({c:count1})
	for s in b:
		if s not in dict2:
			dict2.update({s:1})
		else:
			count2=dict2.get(s)
			count2+=1
			dict2.update({s:count2})
			
	unmatched=0
	pop1=[]
	pop2=[]
	#print dict1, '     ', dict2
	
	for key, value in dict1.iteritems():
		if key not in dict2:
			unmatched+=value
			pop1.append(key)
		else:
			unmatched+=math.fabs(value-dict2.get(key))
			pop1.append(key)
			pop2.append(key)
			
	#print unmatched
	for key, value in dict2.iteritems():
		if key not in dict1:
			unmatched+=value
			pop2.append(key)
			
	#print unmatched
	for k in pop1:
		dict1.pop(k)
	
	for k in pop2:
		dict2.pop(k)	
	#print dict1,'  ', dict2
	for key,value in dict1.iteritems():
		unmatched+=value
	for key,value in dict2.iteritems():
		unmatched+=value
	return int(unmatched)
    

a = raw_input().strip()
b = raw_input().strip()

print number_needed(a, b)