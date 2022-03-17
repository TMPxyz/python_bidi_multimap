# bidi multimap

from collections import defaultdict

class MMap:
    "multimap"
    def __init__(self):
        self._m = defaultdict(set)
        self._pair_cnt = 0

    def __contains__(self, k):
        "if a key in mmap"
        return k in self._m
    
    def __getitem__(self, k):
        if k not in self._m: 
            raise KeyError(f"unknown key {k}")
        return frozenset(self._m[k])

    def __len__(self):
        return len(self._m)

    def pair_count(self):
        return self._pair_cnt

    def keys(self):
        return self._m.keys()

    def values(self):
        return self._m.values()

    def items(self):
        return self._m.items()

    def iter_all_pairs(self):
        for k, s in self._m.items():
            for v in s:
                yield k, v

    def clear(self):
        self._m.clear()
        self._pair_cnt = 0

    def has_pair(self, k, v):
        s = self._m.get(k, None)
        if not s: return False
        return v in s
        
    def add_pair(self, k, v):
        "add a pair k,v to mmap"
        self._m[k].add(v)
        self._pair_cnt += 1

    def pop_pair(self, k, v):
        "if k,v pair not present, raise KeyError"
        if k not in self._m:
            raise KeyError(f"unknown key {k}")
        if v not in self._m[k]:
            raise KeyError(f"unknown value {v}")
        self._m[k].remove(v)
        self._pair_cnt -= 1

    def pop_all(self, k, d=None):
        """remove all pairs under given key, return the value
        if k not found, return d or KeyError if d is None
        """
        if k not in self._m:
            if d is None:
                raise KeyError(f"unknown key {k}")
            else:
                return d

        s = self._m.pop(k)
        self._pair_cnt -= len(s)
        return s

class BiMMap:
    """a bidirectional multimap"""
    DEF_NONE = "BIMAP__NONE"

    def __init__(self):
        self._m = MMap()
        self._im = MMap()

    def pair_count(self):
        return self._m.pair_count()

    def keys(self):
        return self._m.keys()
    def rkeys(self):
        return self._im.keys()

    def values(self):
        return self._m.values()
    def rvalues(self):
        return self._im.values()

    def items(self):
        return self._m.items()
    def ritems(self):
        return self._im.items()

    def clear(self):
        self._m.clear()
        self._im.clear()

    def get(self, k, d=DEF_NONE):
        if d is self.DEF_NONE:
            return self._m[k]
        else:
            return self._m[k] if k in self._m else d
    def rget(self, k, d=DEF_NONE):
        if d is self.DEF_NONE:
            return self._im[k]
        else:
            return self._im[k] if k in self._im else d

    def iter_all_pairs(self):
        return self._m.iter_all_pairs()
    def riter_all_pairs(self):
        return self._im.iter_all_pairs()

    def has_pair(self, k, v):
        return self._m.has_pair(k, v)
    def rhas_pair(self, k, v):
        return self._im.has_pair(k, v)

    def add_pair(self, k, v, dup='raise'):
        if self.has_pair(k, v):
            if dup is 'raise': raise KeyError(f"({k}, {v}) already in map")
            elif dup is 'ignore': return
            else: raise RuntimeError(f"unexpected dup op {dup}")

        self._m.add_pair(k, v)
        self._im.add_pair(v, k)
    def radd_pair(self, k, v, dup='raise'):
        if self.rhas_pair(k, v):
            if dup is 'raise': raise KeyError(f"({k}, {v}) already in map")
            elif dup is 'ignore': return
            else: raise RuntimeError(f"unexpected dup op {dup}")

        self._im.add_pair(k, v)
        self._m.add_pair(v, k)

    def pop_pair(self, k, v):
        self._m.pop_pair(k, v)
        self._im.pop_pair(v, k)
    def rpop_pair(self, k, v):
        self._im.pop_pair(k, v)
        self._m.pop_pair(v, k)

    def pop_all(self, k):
        s = self._m.pop_all(k)
        for v in s:
            self._im.pop_pair(v, k)
    def rpop_all(self, k):
        s = self._im.pop_all(k)
        for v in s:
            self._m.pop_pair(v, k)
    
    

    

    
    
