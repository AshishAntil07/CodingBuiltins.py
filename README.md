<table align='center' border='0'><tr><td><img src='https://github.com/AshishAntil07/AshishAntil07/blob/home/5pointedStar.svg' height='65px' width='65px'></td> <td><h1>Coding Built-in Functions</h1></td></tr></table>
Coding some built-in functions in Python.<br>
Here, you will get reduce function, replace function, format method(as a function), and many more!<br>

## How to use :
### Replace function
```python
MyString = 'They are fighting in the table in the floor.'
MyString = replace(MyString, 'in', 'on')                            # 4th parameter will state whether all matches will be replaced or not, by default it is true.
print(MyString)

'''
Output:
They are fighting on the table on the floor.
'''
```

### Format function
```python
MyString = 'They are {1} on the {0} on the {2}.'
MyString = format(MyString, 'table', 'fighting', 'floor')
             # OR
# MyString = format(MyString, ['table', 'fighting', 'floor'])
print(MyString)

'''
Output:
They are fighting on the table on the floor.
'''
```

### Reduce function
```python
l = [1, 2, 3, 4, 5]
def function(num1, num2):
  return num1+num2[0]+num2[1]

val = reduce(function, l, 3)          # the third argument will state the length of group of elements you want, by default it is 2.
print(val)                            # if the length is greater than 2, then it will pass the 2nd argument as a list.

'''
Output:
22
'''
```

### List Flatter
```python
multiDimensional = [
  'al;edg',
  [289, [420, '29803age4', [2893]], 'glj'],
  [2893, ['gj;la', ['28934'], 6903], 90],
  2384,
  [28347, [58023, [32409783, 532489, [50923, [258709], 198], 59], 7], 20, 59]
]

print(multiDimensional)
print(flat(multiDimensional))

'''
Output:

['al;edg', [289, [420, '29803age4', [2893]], 'glj'], [2893, ['gj;la', ['28934'], 6903], 90], 2384, [28347, [58023, [32409783, 532489, [50923, [258709], 198], 59], 7], 20, 59]]
['al;edg', 289, 420, '29803age4', 2893, 'glj', 2893, 'gj;la', '28934', 6903, 90, 2384, 28347, 58023, 32409783, 532489, 
50923, 258709, 198, 59, 7, 20, 59]
'''
```

## License :
This repository is licensed under [MIT License](https://github.com/AshishAntil07/CodingBuiltins.py/blob/main/LICENSE)
