
def keywithmaxval(d):
 
    v=list(d.values())
    k=list(d.keys())
    return k[v.index(max(v))]

def  electionWinner(votes):
    candidates = {}
    for vote in votes:
        if vote in candidates :
            candidates[vote] +=1
        else :
            candidates[vote] = 1
    ##print max(candidates.iterkeys(), key=lambda k: candidates[k])
    print keywithmaxval(candidates)
    print candidates        
            
votes = ["Victor","Victor","Max","Max","Mary"]

print electionWinner(votes)        
