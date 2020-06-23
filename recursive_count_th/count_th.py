'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
  #Check length of word
    if len(word) < 2:#base case
        return 0
    #Begin recurssion 
    if word[:2] == 'th':
        #If found return 1 and keep going
        return 1 + count_th(word[2:])
    else:
        #Otherwise return zero and keep going
        return 0 + count_th(word[1:])
    