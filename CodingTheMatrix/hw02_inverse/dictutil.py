# Copyright 2013 Philip N. Klein
def dict2list(dct, keylist): return [ dct[keylist[i]] for i in range(len(keylist)) ]

def list2dict(L, keylist): return { (keylist[i]):L[i] for i in range(len(L))}

