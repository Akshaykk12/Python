"""
You have write a function that accepts, a string which length is “len”, the 
string has some “#”, in it you have to move all the hashes to the front of the 
string and return the whole string back and print it.

example :-
Sample Test Case
Input:
Move#Hash#to#Front

Output:
MoveHashtoFront
"""
def hash_to_front(sent):
    count = sent.count("#")
    output = "#" * count
    sents = sent.split("#")
    output = output + "".join(sents)
    return output
    
sent = input()
print(hash_to_front(sent))