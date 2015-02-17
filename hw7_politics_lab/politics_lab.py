# version code 122ffbc9f6c3+
coursera = 1
# Please fill out this stencil and submit using the provided submission script.

# Be sure that the file voting_record_dump109.txt is in the matrix/ directory.


import re
MAX = float('inf')

#
# Find a list of a particular party, uses a regular expression so 
# we can wildcard.
#
def find_members_of_party(strlist,party):
    members = {}
    for i in strlist:
        t = i.split()
        if re.match(party,t[1],re.I):
          members[t[0]] = t[1] 
    return members

#
# Find a list of a particular party, uses a regular expression so 
# we can wildcard.
#
def find_senators_in_state(strlist,state):
    members = {}
    for i in strlist:
        t = i.split()
        if re.match(state,t[2],re.I):
          members[t[0]] = t[2] 
    return members


## 1: (Task 2.12.1) Create Voting Dict
def create_voting_dict(strlist):
    """
    Input: a list of strings.  Each string represents the voting record of a senator.
           The string consists of 
              - the senator's last name, 
              - a letter indicating the senator's party,
              - a couple of letters indicating the senator's home state, and
              - a sequence of numbers (0's, 1's, and negative 1's) indicating the senator's
                votes on bills
              all separated by spaces.
    Output: A dictionary that maps the last name of a senator
            to a list of numbers representing the senator's voting record.
    Example: 
        >>> vd = create_voting_dict(['Kennedy D MA -1 -1 1 1', 'Snowe R ME 1 1 1 1'])
        >>> vd == {'Snowe': [1, 1, 1, 1], 'Kennedy': [-1, -1, 1, 1]}
        True

    You can use the .split() method to split each string in the
    strlist into a list; the first element of the list will be the senator's
    name, the second will be his/her party affiliation (R or D), the
    third will be his/her home state, and the remaining elements of
    the list will be that senator's voting record on a collection of bills.

    You can use the built-in procedure int() to convert a string
    representation of an integer (e.g. '1') to the actual integer
    (e.g. 1).

    The lists for each senator should preserve the order listed in voting data.
    In case you're feeling clever, this can be done in one line.
    """
    vr = {}
    for i in strlist:
        t = i.split()
        vr[t[0]] = [int(j) for j in t[3:]]
    return vr

mylist = list(open('voting_record_dump109.txt'))
t = create_voting_dict(mylist)
#print(t['Snowe'])
#print(t['Sarbanes'])


## 2: (Task 2.12.2) Policy Compare
def policy_compare(sen_a, sen_b, voting_dict):
    """
    Input: last names of sen_a and sen_b, and a voting dictionary mapping senator
           names to lists representing their voting records.
    Output: the dot-product (as a number) representing the degree of similarity
            between two senators' voting policies
    Example:
        >>> voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
        >>> policy_compare('Fox-Epstein','Ravella', voting_dict)
        -2
    
    The code should correct compute dot-product even if the numbers are not all in {0,1,-1}.
        >>> policy_compare('A', 'B', {'A':[100,10,1], 'B':[2,5,3]})
        253
        
    You should definitely try to write this in one line.
    """
    return sum([voting_dict[sen_a][i]*voting_dict[sen_b][i] for i in range(len(voting_dict[sen_a]))])


# OPTIONAL:
# Compare the two senators from Washington, Patty Murry and Maria Cantwell.  They 
# are pretty similar
#
# wa = list(find_senators_in_state(mylist, 'WA').keys())
# print(policy_compare(wa[0], wa[1], t)) # there are two senators for each state

#print(policy_compare('Snowe','Sarbanes',t))
#voting_dict = {'Fox-Epstein':[-1,-1,-1,1],'Ravella':[1,1,1,1]}
#print(policy_compare('Fox-Epstein','Ravella', voting_dict))


## 3: (Task 2.12.3) Most Similar
def most_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is most
            like the input senator (excluding, of course, the input senator
            him/herself). Resolve ties arbitrarily.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> most_similar('Klein', vd)
        'Fox-Epstein'

    Note that you can (and are encouraged to) re-use you policy_compare procedure.
    """
    who = ""
    c = -MAX
    for i in voting_dict.keys():
        # if i == sen: continue 
        t = policy_compare(sen,i,voting_dict)
        if t > c:
           who = i
           c = t
    return who


# vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
# print(most_similar('Klein', vd))

## 4: (Task 2.12.4) Least Similar
def least_similar(sen, voting_dict):
    """
    Input: the last name of a senator, and a dictionary mapping senator names
           to lists representing their voting records.
    Output: the last name of the senator whose political mindset is least like the input
            senator.
    Example:
        >>> vd = {'a': [1,1,1], 'b': [1,-1,0], 'c': [-1,0,0]}
        >>> least_similar('a', vd)
        'c'
    """
    who = ""
    c = MAX
    for i in voting_dict.keys():
        if i == sen: continue 
        t = policy_compare(sen,i,voting_dict)
        if t < c:
           who = i
           c = t
    return who

# vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
# print(most_similar('Klein', vd))


## 5: (Task 2.12.5) Chafee, Santorum
most_like_chafee    = most_similar('Chafee', create_voting_dict(mylist))
least_like_santorum = least_similar('Santorum', create_voting_dict(mylist))

## 6: (Task 2.12.7) Most Average Democrat
def find_average_similarity(sen, sen_set, voting_dict):
    """
    Input: the name of a senator, a set of senator names, and a voting dictionary.
    Output: the average dot-product between sen and those in sen_set.
    Example:
        >>> vd = {'Klein': [1,1,1], 'Fox-Epstein': [1,-1,0], 'Ravella': [-1,0,0]}
        >>> find_average_similarity('Klein', {'Fox-Epstein','Ravella'}, vd)
        -0.5
    """
    return sum([policy_compare(sen,i,voting_dict) for i in sen_set])/len(sen_set)



## 7: (Task 2.12.8) Average Record
def find_average_record(sen_set, voting_dict):
    """
    Input: a set of last names, a voting dictionary
    Output: a vector containing the average components of the voting records
            of the senators in the input set
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> find_average_record({'Fox-Epstein','Ravella'}, voting_dict)
        [-0.5, -0.5, 0.0]
        >>> d = {'c': [-1,-1,0], 'b': [0,1,1], 'a': [0,1,1], 'e': [-1,-1,1], 'd': [-1,1,1]}
        >>> find_average_record({'a','c','e'}, d)
        [-0.6666666666666666, -0.3333333333333333, 0.6666666666666666]
        >>> find_average_record({'a','c','e','b'}, d)
        [-0.5, 0.0, 0.75]
        >>> find_average_record({'a'}, d)
        [0.0, 1.0, 1.0]
    """
    return [sum([voting_dict[sen][i] for sen in sen_set])/len(sen_set) for i in range(len(list(voting_dict.values())[0]))]

#
# Exercise #6 should really be swapped with #7.
#

#
# Generate a list of democrats
#
democrats = find_members_of_party(mylist,'D')
democrat_voting = {name:t[name] for name in democrats}

#
# find the overall average record.
#
average_Democrat_record = find_average_record(democrats, create_voting_dict(mylist))
# 
# Create the prototype "Average" Democrat
#
democrat_voting['Average'] = average_Democrat_record
#
# Find who they're most similar to
#
most_average_Democrat = most_similar ('Average', democrat_voting) 
least_average_Democrat = least_similar ('Average', democrat_voting) 


print(most_average_Democrat)
print(least_average_Democrat)

## 8: (Task 2.12.9) Bitter Rivals
def bitter_rivals(voting_dict):
    """
    Input: a dictionary mapping senator names to lists representing
           their voting records
    Output: a tuple containing the two senators who most strongly
            disagree with one another.
    Example: 
        >>> voting_dict = {'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}
        >>> br = bitter_rivals(voting_dict)
        >>> br == ('Fox-Epstein', 'Ravella') or br == ('Ravella', 'Fox-Epstein')
        True
    """
    who = ()
    rivals = {}
    compare = MAX
    #
    # For each senator, find the least similar.
    #
    for i in voting_dict.keys():
        rivals[i] = least_similar(i, voting_dict)
    #
    # Now find who are the most extreme.
    #
    for i in rivals:
        t = policy_compare(i, rivals[i], voting_dict)
        if t < compare:
            compare = t
            who = (i, rivals[i])
    return who

# print(bitter_rivals ({'Klein': [-1,0,1], 'Fox-Epstein': [-1,-1,-1], 'Ravella': [0,0,1]}))
