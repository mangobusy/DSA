class MapBase('''MultableMapping'''):
    class _item():
        __slots__ = '_key','_value'
        def __init__(self,k,v):
            self._key = k
            self._value = v
        def __eq__(self, other):
            return self._key == other._key
        def __ne__(self, other):
            return not (self == other)
        def __lt__(self, other):
            return self._key < other._key

class UnsortedTableMap(MapBase):
    def __init__(self):
        self._table = []
    def __getitem__(self, k):
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Key Error:'+ repr(k))
    def __setitem__(self, k, v):
        for item in self._table:
            if k == item._key:
                item._value = v
                return
        self._table.append(self._item(k,v))
    def __delitem__(self, k):
        for j in range(len(self._table)):
            if k == self._table[j]._key:
                self._table.pop(j)
                return
        raise KeyError('Key Error:'+ repr(k))
    def __len__(self):
        return len(self._table)
    def __iter__(self):
        for item in self._table:
            yield item._key

# Hash哈希表
# 优点：可快速插入修改元素、删除元素、查找元素
# 缺点：哈希表中的数据是没有顺序的；数据不允许重复
import pprint
class Hashtable():
    def __init__(self,elements):
        self.bucket_size = len(elements)
        self.buckets = [[] for i in range(self.bucket_size)]
        self._assign_buckets(elements)
    def _assign_buckets(self,elements):
        for key, value in elements:
            hashed_value = hash(key)
            index = hashed_value % self.bucket_size
            self.buckets[index].append((key,value))
    def get_value(self,input_key):
        hashed_value = hash(input_key)
        index = hashed_value % self.bucket_size
        bucket = self.buckets[index]
        for key, value in bucket:
            if key == input_key:
                return(value)
        return None
    def __str__(self):
        return pprint.pformat(self.buckets)

import random
class HashMapBase(MapBase):
    def __init__(self,cap=11,p=109345121):
        self._table = cap * [None]
        self._n = 0
        self._prime = p
        self._scale = 1 + random.randrange(p - 1)
        self._shift = random.randrange(p)
    def _hash_function(self,k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)
    def __len__(self):
        return self._n
    def __getitem__(self,k):
        j = self._hash_function(k)
        return self._bucket_getitem(j,k)
    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j,k,v)
        if self._n > len(self._table) // 2:
            self._resize(2 * len(self._table)-1)
    def __delitem__(self,k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)
        self._n -=1
    def _resize(self,c):
        ole = list(self.items())
        self._table = c * [None]
        self._n = 0
        for (k,v) in ole:
            self[k] = v

class ChainHashMap(HashMapBase):
    def _bucket_getitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        return bucket[k]
    def _bucket_setitem(self,j,k,v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize:
            self._n += 1
    def _bucket_delitem(self,j,k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error: ' + repr(k))
        del bucket[k]
    def __iter(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key
