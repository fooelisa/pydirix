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
>>> members = dirIX(url='https://www.ecix.net/memberlist_BER.json')
>>> members.get()
```

License
======

Copyright 2015 BigWaveIT.

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
