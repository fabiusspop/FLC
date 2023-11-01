# Ex 1 - Create a DFA in Python that checks if a word belongs to a language where the words are composed only by 1s (1+). Provide at least 2 examples

"""

def belongstoDFA(s):

    if len(s)<0:
        return "Input doesn't belong to the specific language. :("
        
    if s[0]=='1':
        for i in range(1,len(s)):
            if(s[i]!='1'):
                return "Input doesn't belong to the specific language. :("
        return "Input belongs to the specific language! :)"


print(belongstoDFA("1111"))            
print(belongstoDFA("1101"))

"""  

# Ex 2 - Create a DFA in Python that checks if a word belongs to a language where the words start with an even numbers of 0s followed by at least one 1 ((00)+1+).Provide at least 2 examples

"""

dfa = {0:{'0':1}, 1:{'0':2}, 2:{'0':3,'1':5}, 3:{'0':4}, 4:{'0':3,'1':5}, 5:{'1':5}}

def belongstoDFA(transitions,start,final,s):
    
        state=start
        try:
            for i in s:
                state=transitions[state][i]
            if(state in final):
                 return "The string belongs to the specific language! :)"
            else:
                return "The string doesn't belong to the specific language. :("
        except:
            return "The string doesn't belong to the specific language. :("   
    
    
print(belongstoDFA(dfa,0,{5},"000011"))            
print(belongstoDFA(dfa,0,{5},"0000011"))

"""  

# Ex 3 - Create a DFA in Python that checks if a word belongs to a language of words that start and end with the same letter. Provide at least 2 examples.

def belongstoDFA(s):
    
    if len(s)<0:
        return "The string doesn't belong to the specific language. :("
    
    if(s[0]==s[-1]):
        return "The string belongs to the specific language! :)"
    return "The string doesn't belong to the specific language. :("    
   
print(belongstoDFA("goodExampleg"))            
print(belongstoDFA("badExample"))
