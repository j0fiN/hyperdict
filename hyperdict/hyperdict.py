import typing as t


class NoValue:

    def __new__(cls, ob=None):
        return ob

class NoKey:
    def __new__(cls, ob=None):
        return ob

class EachHyperDictAssist:

    def __new__(cls): return 'EachHyperDictAssist'

class HyperDictError(Exception):
    ...



class HyperDict(dict):
    '''
    HyperDict\n
    Python Dictionary, but on steroids.

    >>> # import the library
    >>> from hyperdict import HyperDict as HD
    '''
    def __init__(self, dict_obj: dict={}, no_val=None, no_key=None):
        '''
        Creates a instance of HyperDict super dictionary.
        >>> from hyper import HyperDict
        >>> hyper = HyperDict()         
        >>> hyper
        HyperDict({'name': 'Magnus', 'age': 31})
        '''
        self.__hyper = dict_obj
        self.__key_cache = {}
        self.k = list(self.__hyper.keys())
        self.v = list(self.__hyper.values())
        self.i = tuple(self.__hyper.items())
        self.no_val = no_val
        self.no_key = no_key

    
    def __getitem__(self, item):
        '''
        
        '''
        if type(item).__name__ == 'tuple':
            _values = list()
            for key in item:
                try:
                    _values.append(self.__hyper[key])
                except:
                    _values.append(NoValue(self.no_key))
            return tuple(_values)
        else:
            try:
                return self.__hyper[item]
            except:
                return NoValue(self.no_val)
            
    
    def __setitem__(self, key, value):
        if type(key).__name__ in 'tuple':
            if type(value).__name__ == 'list' and value[-1] == 'EachHyperDictAssist':
                value.pop()
                for neu, val in zip(key, value):
                    self.__hyper[neu] = val
            else:
                for neu in key:
                    self.__hyper[neu] = value
        else:
            self.__hyper[key] = value
        self.__update()
    

    def __delitem__(self, key):
        if type(key).__name__ in 'tuple':
            for i in key:
                del self.__hyper[i]
        else:
            del self.__hyper[key]
        self.__update()
        
    
    def __repr__(self):
        return "HyperDict(" + str(self.__hyper) + ')'


    def __iter__(self):
        self.x = -1
        return self


    def __next__(self):
        neu = list(self.__hyper.keys())
        if self.x < len(neu)-1:
            self.x += 1
            return list(self.__hyper.keys())[self.x]
        else:
            raise StopIteration


    def items(self):
        return self.__hyper.items()

    def keys(self):
        return self.__hyper.keys()

    def values(self):
        return self.__hyper.values()

    def __get_key(self, value):
        try:
            if value in self.__key_cache:
                return self.__key_cache[value]
        except TypeError:
            ...
        keys = [i[0] for i in self.__hyper.items()]
        values = [i[1] for i in self.__hyper.items()]
        indices = []
        count = 0
        for i in values:
            if value == i:
                indices.append(count)
            count += 1
        
        if indices == []:
            return NoKey(self.no_key)
        else:
            try:
                result_tup = tuple([keys[i] for i in indices])
                self.__key_cache[value] = result_tup
                return self.__key_cache[value]
            except TypeError:
                return result_tup
            


    def __call__(self, *a):
        try:
            trial = a[1]
            del trial
            result = []
            for i in a:
                result.append(self.__get_key(i))
            return tuple(result)
        except IndexError:
            return self.__get_key(a[0])

    def __invert__(self):
        __lis = self.__hyper
        __result = {}
        for i, j in __lis.items():
            __result[j] = i
        return HyperDict(__result, no_val=self.no_key, no_key=self.no_val)

    @staticmethod
    def each(*arr):
        arr = list(arr)
        arr.append(EachHyperDictAssist())
        return arr

    def __update(self):
        self.k = list(self.__hyper.keys())
        self.v = list(self.__hyper.values())
        self.i = tuple(self.__hyper.items())
        self.clear_key_cache()
    
    def __dict__(self):
        return self.__hyper

    def clear_key_cache(self):
        self.__key_cache = {}

    def __hash__(self):
        return hash(str(self.__dict__))

    def hash(self):
        return hash(str(self.__hyper))

    def __contains__(self, key):
        return self.__hyper.__contains__(key)