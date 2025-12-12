class Solution:
    def countMentions(self, n: int, events: List[List[str]]) -> List[int]:
        ans ,  offline = [0]*n , [0]*n 
        events.sort( key = lambda x : (int(x[1]),x[0] == "MESSAGE"))
        for state , time , ids in events:
            if state == "MESSAGE":
                if ids == "ALL":
                    for i in range(n):
                        ans[i] += 1
                elif ids == "HERE":
                    for i in range(n):
                        if int(time) >= offline[i]:
                            ans[i]+=1
                else: 
                    for Id in ids.split(" "):
                        int_id = int(Id[2:])
                        ans[int_id] += 1
            else:
                offline[int(ids)] = int(time) + 60
        return ans





