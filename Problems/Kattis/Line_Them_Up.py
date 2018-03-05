from itertools import izip, tee


team = []
for _ in range(0,int(raw_input())):
    team.append(raw_input())

t = iter(team)
prev, cur = tee(t, 2)
cur.next()
paired = list(izip(prev,cur))

state = 0
for pair in paired:
    if pair[0] > pair[1]:
       state += -1
    else:
       state += 1

if state == len(team)-1:
    print 'INCREASING'
elif state == -len(team)+1:
    print 'DECREASING'
else:
    print 'NEITHER'

        
