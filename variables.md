There is no explicit declaration, example: name = 'Diego'
A variable only exists when you declare a value to it.

Variables are Snake_Case, example: my_age_now = 20
- Types: Integer, Float, Long, Complex, String, List
- Integer: age = 50
- Float: salary = 7500.50
- Long: size = 10L
- Complex: total = 7500.50j
- String: name = "Diego" or name = 'Diego'

You can declare more than one variable at time.
```
>>> name , cpf = 'Diego', 123456789
```

Slice and concat:
```
>>> name = 'Diego Leonardo Urban'
>>> first_name = name[0:5]
>>> 'My first name is ' + first_name
>>> age = 28
>>> 'My first name is ' + first_name + ', age ' + age // will cause type error
>>> print 'My first name is %s, age %s' % (name, age)
```
