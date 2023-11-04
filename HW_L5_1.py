# Ex 2 - Create a regex to check if HTML tags are correctly written. Give at least 6 different examples (5 should be with different inconsistencies such as <p, p>, <id=“>, “<p>”, <p/>)

import re

tag_pattern = re.compile(r'^<([a-z1-6]+)(\s+[^>]*)?>.*?</\1>$', re.MULTILINE)

# Examples to test
examples = [
    "<p>Good example.</p>",     
    "<h1>Good example</h1>",                   
    "<div class=\"goodexample\"></div>",                 
    "<h1>Bad Example</h2>",                  
    "<div class=\"badexample\">",            
]

for example in examples:
    print(f"Correct" if tag_pattern.match(example) else "Incorrect")


# Ex 4 - Create a DFA in Python that checks if a word belongs to a language of words that either start or end with ab. (e.g. abaa,aabab are ok, aabba, aabb are not ok). Provide at least 2 examples.

def dfaCheck(word):
    start_ab = word.startswith('ab')  
    end_ab = word.endswith('ab')      
    return start_ab or end_ab         

print("abaa -", dfaCheck("abaa"))   
print("aabab -", dfaCheck("aabab")) 
print("aabba -", dfaCheck("aabba")) 
print("aabb -", dfaCheck("aabb"))   

