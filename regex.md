```
>>> import re
>>> result = re.match('Py', 'Python')
>>> result.group()
```

```
>>> result = re.match('py', 'Python')
>>> result.group() // error
```

```
>>> result = re.match('[pP]y', 'Python')
>>> result.group()
```

```
>>> result = re.match('[A-Za-z]y', 'Python')
>>> result.group()
```

```
>>> result = re.findAll('[A-Za-z]y', 'Python ou jython')
>>> result
```

```
>>> result = re.findAll('[A-Za-z]y[A-Za-z]+', 'Python ou jython ou Pypy')
>>> result
```

```
>>> result = re.findAll('\wy\w+', 'Python ou jython ou Pypy')
>>> result
```

Declaring a raw string:
```
r'[A-Z]+'
```

Starts with:
```
r'^www'
```

Ends with:
```
r'.br$'
```