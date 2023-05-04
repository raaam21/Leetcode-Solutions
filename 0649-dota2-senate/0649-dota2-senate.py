class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        q=list(senate)
        while(True):
            if q[0]=='R':
                i=0
                f=1
                while(i<len(q)):
                    if q[i]=='D':
                        q.pop(i)
                        f=0
                        break
                    else:
                        i+=1
                if f!=0:
                    break
                q.pop(0)
                q.append('R')

            elif q[0]=='D':
                i=0
                f=1
                while(i<len(q)):
                    if q[i]=='R':
                        q.pop(i)
                        f=0
                        break
                    else:
                        i+=1
                if f!=0:
                    break
                q.pop(0)
                q.append('D')

        if q[0]=='R':
            return 'Radiant'
        return 'Dire'