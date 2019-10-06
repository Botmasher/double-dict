# Implement dictionary where both keys and values are unique

class DoubleDict(dict):
    def __init__(self, *args, **kw):
        super(DoubleDict, self).__init__(*args, **kw)
        self.iterkeys = [k for k in super(DoubleDict, self).keys()]
    
    def __setitem__(self, k, v):
        self.iterkeys += [k]
        super(DoubleDict, self).__setitem__(k, v)
    
    def __iter__(self):
        return iter(self.iterkeys)
    
    def keys(self):
        return self.iterkeys
    
    def values(self):
        return [v for v in self.values()] 
    
    def itervalues(self):
        return (v for v in self.values())

    def set_keytype(self, keytype):
        self.keytype = keytype
    
    def get_keytype(self):
        return self.keytype

    # TODO: allow for None entry
    def get(self, k=None):
        if k is None:
            return self
        return self[k]

    # TODO: move logic to __setitem__
    #   - also override get and setdefault
    def add(self, k, v):
        if not isinstance(k, self.keytype) or not isinstance(v, self.keytype):
            raise TypeError(f"doubledict add failed - expected type {self.keytype}")
        if v in self or v in self.values():
            raise ValueError(f"doubledict cannot add existing value {v}")
        self[k] = v

d = DoubleDict()
print(d)
d.keytype = str
d[1] = ['a']        # error
d['a'] = 1          # error
d['a'] = ['b']      # {'a': 'b'}
d['b'] = ['c']      # {'a': 'b', 'b': 'c'}
d['c'] = ['a']      # {'a': 'b', 'b': 'c', 'c': 'a'}
d['a'] = ['c']      # error
d['a'] = ['d']      # overwrite k:v
