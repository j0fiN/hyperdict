# `hyperdict`
### *Python dictionaries, but on steroids.*
`hyperdict` works just like the old dictionary but with more additional features. It makes working with dictionaries relatively quicker and easier!

- Built for clean and shorter adders, getters, and setters.
- It significantly reduces the lines of code written for dictionary manipulations.
- `hyperdict` retrieve keys when values are given (value-key pairs). 
- Inbuilt unary operations developed with specific functionalities.
- All inbuilt python dictionary methods work in `hyperdict`.

## Installation
```sh-session
$ pip install hyperdict
---> 100%
```
## To get started
```python
import hyperdict as hd
```
### Create a hyperdict object
Using the `HyperDict` class, we can build a hyper dictionary.
```python
d = hd.HyperDict()
```
### Usage
Multiple keys can be assigned in a single line.
```python
d[1, 2, 'name'] = None 
# HyperDict({1: None, 2: None, 'name': None})

# without hyperdict
a = [1, 2, 'name']
d = {i: None for i in a}
```
Using `each()` function, multiple keys can be assigned with coressponding multiple values.
```python
d['name', 'age', 'skills'] = hd.each('Magnus', 31, ['chess', 'football'])
# HyperDict({'name': 'Magnus', 'age': 31, 'skills': ['chess', 'football']})

# without hyperdict
d['name'] = 'Magnus'
d['age'] = 31
d['skills'] = ['chess', 'football']
```
Multiple values can also be retrieved and can also be delelted using the same syntax.
```python
d['name', 'age']
# ('Magnus', 31)
d['email'] # predefined value for a missing key is None
# None
del d['skills', 'email'] # 'skills' key will be deleted
# trial.py:23: Warning: Missing keys: email
...
... # execution continues after warning...
```
### `hyperdict` as a callable object
One of the most unique things about hyperdict is value-key retrieval. On accepting value(s), the hyperdict return the keys.  
The hashable types(namely `int()`, `bool()`, `str()`, `tuple()`) are cached along with the keys for quicker retrieval from the hyperdict. The cache is cleared when the hyperdict internal dictionary is changed.
```python
d = hd.Hyperdict()
d[1, 2, 3] = hd.each(0, 1, 0)
d(0)
# (1, 3)
d(4) # default value for a missing key
# None
d(0, 1)
# ((1, 3), (2,))
d() # return a dict() of all the value-key pairs.
# {0: (1, 3), 1: (2,)}
```
### Attributes and Operators
```python
d.i # same as list(d.items())
d.k # same as list(d.keys())
d.v # same as list(d.values())

inv_d = ~d # Invertor Operation: Returns an Inverts key-values to value-key
# WARNING: This operation works as expected if 
# - values are hashable types (raises an Exception)
# - values are unique like the keys (overwrites the prev key with a new key.)

cpy_d = +d # Copy Operation: Returns a python dictionary deep-copied from the hyperdict object

-d # Clear Operation: similar to clear() method of python dictionary. Clears the hyperdict dictionary.
```

### Methods and functions.
**`to_hd(*a)`**: Creates a `hyperdict` using the variable name as keys.
```python
name, age, skills = foo_get_data()
h = hd.to_hd(name, age, skills) 
# HyperDict({'name': 'Magnus', 'age': 24, 'skills': ['chess', 'football']})
```
**`change_no_value(any)`** and **`change_no_key(any)`**: Changes default values for missing key and value(default is `None`).
```python
d.change_no_key('No key found!')
d['name', 'random key']
# ('Magnus', 'No key found!')

d.change_no_value('')
d(24, 'random value')
# (('age',), '')
```
**`hash()`**: Creates hash of the dictionary exclusively.
```python
d.hash() # hash of the dictionary alone.
# 123...
hash(d) # hash of the whole hyperdict instance.
# 321...
```
**`each(*a)`**: Helper function which is used to map the corresponding values to the given keys.
```python
d['name', 'age', 'skill'] = hd.each('Magnus', 31, ['Chess', 'Football'])
```
### Docstrings
```python
import hyperdict as hd
help(hd)
```
### In-built dictionary methods
***All the methods of python inbuilt dictionary works just the same in hyperdict.***

### Related Python libraries
The `to_hd()` function in hyperdict uses [executing](https://github.com/alexmojaki/executing) by [@alexmojaki](https://github.com/alexmojaki) to retrieve object's name and use it as a corresponding key for the value.