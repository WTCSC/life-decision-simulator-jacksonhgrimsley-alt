#original word count is 720
#new word count is 333
def ask(q,a,b):
    print(q);print(f"A) {a}");print(f"B) {b}")
    return input("(A/B): ").strip().upper()

def ask2(q,a,b):
    print(q);print(f"C) {a}");print(f"D) {b}")
    return input("(C/D): ").strip().upper()

def end(q,a,b):
    print(q);print(f"I) {a}");print(f"J) {b}")
    return input("(I/J): ").strip().upper()

print("Good morning! You wake up bright and early for school.")

c1=ask("What should you do first?","Get up and put clothes on","Stay in bed")

if c1=="A":
    c2=ask2("What's next?","Go eat breakfast","Skip breakfast and study")
    print("Smart choice — breakfast is best!" if c2=="C" else "Hope you don’t get hungry..." if c2=="D" else "wasting time man")
    c3=ask("Kill time on bus?","Study","Sleep")
    print("Helpful choice." if c3=="A" else "You slept past your stop!" if c3=="B" else "not a choice")
    c4=ask("First question: 4+4?","8","77")
    print("Correct." if c4=="A" else "Failed instantly." if c4=="B" else "not a choice")
    c5=end("Last question: John has 18, eats 10, buys 4. Final apples?","14","12")
    print("So close but fail." if c5=="I" else "You passed!" if c5=="J" else "not valid")

else:
    c2=ask2("Finally get up?","Eat and get ready","Go back to sleep")
    print("Refreshed but late." if c2=="C" else "You slept all day." if c2=="D" else "not an option")
    c3=ask("You miss the bus. Walk or ask mom?","Walk","Ask mom")
    print("Beautiful walk but late." if c3=="A" else "Mom is mad but drives you." if c3=="B" else "not valid")
    c4=ask("You forgot a test. Skip or wing it?","Skip","Wing it")
    print("Grounded + fail." if c4=="A" else "Test is easier than expected." if c4=="B" else "not valid")
    c5=end("Final question: 400 - 200 + 50×5?","370","450")
    print("Close but parents upset." if c5=="I" else "You passed relieved" if c5=="J" else "not valid")
