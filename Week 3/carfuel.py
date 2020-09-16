import sys


def refills(dis, tank, stops):
	refils = 0
	currentpos = 0
	nextpos=0
	stops.append(dis)
	stops.insert(0,0)
	while stops[currentpos]+tank<dis:
		currentpos=nextpos
		#print(stops[currentpos])
		while  nextpos<len(stops) -1 and stops[nextpos+1]  <=stops[currentpos]+tank :
			nextpos = nextpos+1

		if stops[currentpos]+tank<dis:
			refils+=1
		if nextpos==currentpos:
			return -1


	return refils

dis = int(input())
maxdis = int(input())
noofstop = int(input())
stops = list(map(int, input().split()))
#stops = stop.split()

print(refills(dis, maxdis, stops))
