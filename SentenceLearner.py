import random

with open("de_sentences_sorted.txt","r") as f:
    sentences=[line.rstrip() for line in f.readlines()]

lower_bound=1
upper_bound=50000
step=10000
max_sentences=10
while (inp:=input("> ")):
    match inp:
        # First functionality, random sentences by difficulty
        case "-": # input "-" to show sentences at random within bounds
            findings=[sentences[random.randint(lower_bound,upper_bound)] for i in range(max_sentences)]
            for sentence in findings:
                print(sentence)
        case "-ld": #lower_bound down
            if lower_bound-step>0:
                print("lower bound lowered")
                lower_bound-=step
        case "-lu": #lower_bound up
            if lower_bound+step<upper_bound:
                print("lower bound raised")
                lower_bound+=step
        case "-ud": #upper_bound down
            if upper_bound-step>lower_bound:
                print("upper bound lowered")
                upper_bound-=step
        case "-uu": #upper_bound up  
            if upper_bound+step<len(sentences):
                print("upper bound raised")
                upper_bound+=step
        case "-bounds": #set bounds manually
            lower=int(input(f"Input lower bound (1 to {len(sentences)}):"))
            upper=int(input(f"Input upper bound (1 to {len(sentences)}):"))
            if 0<lower and lower<upper and upper<len(sentences):
                lower_bound=lower
                upper_bound=upper
                print(f"Bounds updated to {lower_bound} and {upper_bound}")
        case "-info":
            print(f"There are {len(sentences)} sentences")
            print(f"Bounds are {lower_bound} and {upper_bound}")
            
        # Second functionality, sentences containing substring
        case default: # input any other text (not -, not -ld, ...) to search for it
            findings=[sentence for sentence in sentences if inp in sentence.lower()]
            if len(findings)>0:
                random.shuffle(findings)
                for i in range(min(len(findings),max_sentences)):
                    print(findings[i])
            else:
                print("*QUERY NOT FOUND*")
    print()