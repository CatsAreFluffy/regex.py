def match(reg,inp):
    '''reg is the regex,
inp is what you want to match,
returns [start,end] of match'''
    debug=False
    tokens=[""] #token array
    incharclass=False
    for i in reg: #tokenize input
        if debug:print(tokens)
        if incharclass:
            if i=="]" and tokens[-1][-1]!="":
                incharclass=False
            else:
                tokens[-1]+=i
        else:
            if i=="[":
                incharclass=True
                tokens+=""
            else:
                tokens+=i               
    tokens=tokens[1:]
    tkindex=0 #position in token list
    inindex=0 #position in input
    start=0 #start of match
    while tkindex<len(tokens): #stay in the regex
        if True: #free indent block, yay
            if inindex==len(inp): #fell out of the text
                start+=1
                if start>len(inp):
                    return []
                inindex,tkindex=start,0
            else: #still in the text
                if inp[inindex] in tokens[tkindex]:
                    tkindex+=1
                    inindex+=1
                else:
                    start+=1
                    if start>len(inp):
                        return []
                    inindex,tkindex=start,0
    return [start,inindex]
