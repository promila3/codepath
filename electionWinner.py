def keywithmaxval(d): 
    v=list(d.values())
    k=list(d.keys())
    maxval = max(v)
    maxCandidate =  k[v.index(maxval)]
    if  v.count(maxval) == 1 :
        return [maxCandidate]
    else :
        result = [] 
        for name, votes in d.iteritems():
            if maxval == votes:
                result.append(name)
        return result

def  electionWinner(votes):
    candidates = {}
    for vote in votes:
        if vote in candidates :
            candidates[vote] +=1
        else :
            candidates[vote] = 1
     
    result = keywithmaxval(candidates)  
    if len(result) == 1 :
        return result[0]
    else :
        sort(result)
        return result[-1]       
            
votes = ["Victor","Victor","Max","Max","Mary"]

print electionWinner(votes)        
