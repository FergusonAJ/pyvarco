# pyvarco - PYthon VARiable COmbinations
A simple python package to easily create all desired combinations of variables!

## Install 
```pip install pyvarco```

## Quickstart
All functionality is included as a single class, ```pyvarco.CombinationCollector```

To get started, create an instance of the class (it doesn't accept any arguments):
```
from pyvarco import CombinationCollector
combos = CombinationCollector()
```
Next, we need to register all the variables to be used. 
This is done via the ```register_var(var_name)``` method. 
Here, we register two variables:
```
combos.register_var('breed')
combos.register_var('color')
```
_Note_: the order we register variables matters. 
As a quick example, the variable registered last is permuted every step, while the first variable changes last. 

Once the variables are registered, we can add values to them!
This done using the ```add_val(var_name, val)``` method. 
The ```val``` argument can be a single value, list, or tuple. 
If it is a list or tuple, _all_ elements of the container will be add as values to that variable. 
```
combos.add_val('breed', 'dalmation')
combos.add_val('breed', 'chihuahua')
combos.add_val('breed', 'labrador')
combos.add_val('color', ['black', 'white', 'brown'])
```

That's it!
The combination collector instance now contains all the neceessary data. 
To retrieve all combinations we call the ```get_combos()``` method (no arguements). 
```
print(combos.get_combos())
```
This returns a list of dictionaries. 
Each dictionary contains exactly one value for each variable, and in our example we see all 3 * 3 = 9 combinations: 
```
[
  {'color': 'black', 'breed': 'dalmation'}, 
  {'color': 'white', 'breed': 'dalmation'}, 
  {'color': 'brown', 'breed': 'dalmation'}, 
  {'color': 'black', 'breed': 'chihuahua'}, 
  {'color': 'white', 'breed': 'chihuahua'}, 
  {'color': 'brown', 'breed': 'chihuahua'}, 
  {'color': 'black', 'breed': 'labrador'}, 
  {'color': 'white', 'breed': 'labrador'}, 
  {'color': 'brown', 'breed': 'labrador'}
]
```

The CombinationCollector class also includes two helper functions to convert between dictionaries and strings. 
First, ```get_str(D, sep_in, sep_between)``` takes a dictionary that has keys for each variable and returns a formatted string with all the information encoded. 
Conversely, ```get_dict(s, sep_in = '_', sep_between = '__')``` takes a formatted string and returns the matching dictionary entry. 
For example: 
```
s = combos.get_str(combos.get_combos()[0]) 
print(s) # yields 'breed_dalmation__color_black'
D = combos.get_dict(s)
print(D) # yields {'breed': 'dalmation', 'color': 'black'}
```
The ```sep_in``` optional argument determines what character/string separates the variable's name from its value, while the ```sep_between``` optional argument determines what separates variable name/value pairs. 
For example: 
```
combos.get_str(combos.get_combos()[0], sep_in='=', sep_between=', ') 
# Yields: 'breed=dalmation, color=black'
```
### Exceptions
But wait!
Dalmations are white with black dots; they are not brown (I think, not a dalmation expert)!

We can account for this by using exceptions. 
To do this, we use the ```add_exception(exception_dict)``` method.
The ```exception_dict``` argument should be a dictionary with variables (that we registered) as keys. 
Not all variables need be keys in the dictionaries. 
Values in the dictionary can be single elements (shown here), or tuples/lists. 
```
combos.add_exception({'breed': 'dalmation', 'color':'brown'})
print(combos.get_combos())
#Yields:
[
  {'breed': 'dalmation', 'color': 'black'}, 
  {'breed': 'dalmation', 'color': 'white'}, 
  {'breed': 'chihuahua', 'color': 'black'}, 
  {'breed': 'chihuahua', 'color': 'white'}, 
  {'breed': 'chihuahua', 'color': 'brown'}, 
  {'breed': 'labrador', 'color': 'black'}, 
  {'breed': 'labrador', 'color': 'white'}, 
  {'breed': 'labrador', 'color': 'brown'}
]

```
Notice that we only have 8 combinations, ignoring brown dalmations. 
If we used a list or tuple as value for an entry in ```exception_dict``` all values in the container are treated separately. 
For example, if we had done this _instead_: 
```
combos.add_exception({'breed': ['dalmation', 'labrador'], 'color' : 'brown'})
print(combos.get_combos())
#Yields:
[
  {'color': 'black', 'breed': 'dalmation'}, 
  {'color': 'white', 'breed': 'dalmation'}, 
  {'color': 'black', 'breed': 'chihuahua'}, 
  {'color': 'white', 'breed': 'chihuahua'}, 
  {'color': 'brown', 'breed': 'chihuahua'}, 
  {'color': 'black', 'breed': 'labrador'}, 
  {'color': 'white', 'breed': 'labrador'}
]
```


That's it! Let me know / open an issue if you have any comments, concerns, or improvements! 
