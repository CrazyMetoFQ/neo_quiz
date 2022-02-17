import json
from random import randint
from quiz_thing.mcq import mcq


with open(r"C:\Users\Ali Hussain\Quiz\general.json") as f:

    st = json.load(f)

def rand_q(n=1):

    l  = []
    for i in range(n):
        
        r = randint(1,3200)
        d = st[r:r+1][0]

        q = mcq(d.get("Questions"),
                    [d.get(i) for i in ["A","B","C","D"]],
                    d["Correct"])

        l.append(q)
    
    return l

# q.show()