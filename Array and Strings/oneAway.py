def oneAway(s1,s2):
	if abs(len(s1)-len(s2))>1:
		return False
	p1,p2=0
	madeEdit=False
	while p1<len(s1) and p2<len(s2):
		if s1[p1]==s2[p2]:
			p1+=1
			p2+=1
		elif not madeEdit:
			madeEdit=True
			if len(s1)==len(s2):
				p1+=1
				p2+=1
			elif len(s1)<len(s2):
				p2+=1
			elif len(s1)>len(s2):
				p1+=1
		else:
			return False
	return True	
					
