# version code d345910f07ae
from dictutil import dict2list, list2dict
from random import randint

coursera = 1
# Please fill out this stencil and submit using the provided submission script.





## 1: (Task 1) Movie Review
## Task 1
def movie_review(name):
    """
    Input: the name of a movie
    Output: a string (one of the review options), selected at random using randint
    """
    blab = ["Smell it!", "Better than bacon!", "Existential crisis-inducer", "Tastes like chicken!", "Better than a stick in the eye!", "I wept!", "Soylent Green is made from people!!"]
    return blab[randint(0,len(blab)-1)]



## 2: (Task 2) Make Inverse Index
def makeInverseIndex(strlist):
    """
    Input: a list of documents as strings
    Output: a dictionary that maps each word in any document to the set consisting of the
            document ids (ie, the index in the strlist) for all documents containing the word.
    Distinguish between an occurence of a string (e.g. "use") in the document as a word
    (surrounded by spaces), and an occurence of the string as a substring of a word (e.g. "because").
    Only the former should be represented in the inverse index.
    Feel free to use a loop instead of a comprehension.

    Example:
    >>> makeInverseIndex(['hello world','hello','hello cat','hellolot of cats']) == {'hello': {0, 1, 2}, 'cat': {2}, 'of': {3}, 'world': {0}, 'cats': {3}, 'hellolot': {3}}
    True
    """
    d = {}
    for x,y in enumerate(strlist):
       for w in y.split():
           if w in d:
             d[w] |= {x} # merge token counter
           else:
             d[w] = {x}  # Add it to set
    return d

# print( makeInverseIndex(['hello world','hello','hello cat','hellolot of cats'])) 

## 3: (Task 3) Or Search
def orSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of document ids that contain _any_ of the specified words
    Feel free to use a loop instead of a comprehension.
    
    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> orSearch(idx, ['Bach','the'])
    {0, 2, 3, 4, 5}
    >>> orSearch(idx, ['Johann', 'Carl'])
    {0, 2, 3, 4, 5}
    """
    d = set()
    for w in query:
      if w in inverseIndex:
         d |= inverseIndex[w]
    return d

## 4: (Task 4) And Search
def andSearch(inverseIndex, query):
    """
    Input: an inverse index, as created by makeInverseIndex, and a list of words to query
    Output: the set of all document ids that contain _all_ of the specified words
    Feel free to use a loop instead of a comprehension.

    >>> idx = makeInverseIndex(['Johann Sebastian Bach', 'Johannes Brahms', 'Johann Strauss the Younger', 'Johann Strauss the Elder', ' Johann Christian Bach',  'Carl Philipp Emanuel Bach'])
    >>> andSearch(idx, ['Johann', 'the'])
    {2, 3}
    >>> andSearch(idx, ['Johann', 'Bach'])
    {0, 4}
    """
    d = set()
    for w in query:
      if w in inverseIndex:
         if not(d):
            d |= inverseIndex[w]
         else:
            d &= inverseIndex[w]
    return d

