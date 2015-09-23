# pydirix
A Python parser to the Euro-IX JSON schema for IXP member lists

Install
=======

To install, execute:

```
pip install pydirix
```

Documentation
=============

### Init Member Lists
Get IXP member lists:
```python
>>> from pydirIX import dirIX
>>> members = dirIX(urls='...')
>>> members.get()
```

### Get AS Numbers
call asns():
```python
>>> members.asns()
>>>
```

License
======

Copyright 2015 BigWaveIT.

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
