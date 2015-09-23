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

### Import Member List
Import an IXP member list, given a source URL to the JSON schema
```python
>>> from pydirIX import dirIX
>>> members = dirIX(url='https://www.ecix.net/memberlist_BER.json')
>>> members.get()
```

### List Member Data

#### List imported data by Network Name
```python
>>> members.list()
>>> [u'Telefonica Germany GmbH & Co OHG', u'ConnectingBytes GmbH', u'TIRASTEL GmbH', u'PCH Packet Clearing House', u'pop-interactive GmbH', u'Hofnetz & IT Services GmbH', u'e.discom Telekommunikation GmbH', u'CloudFlare Inc.', u'Strato AG', u'Hurricane Electric', u'OMCnet Internet Service GmbH', u'IPB Internet Provider in Berlin GmbH', u'Chaos Computer Club e.V.', u'Speedbone GmbH', u'PCH Packet Clearing House', u'wilhelm.tel GmbH Norderstedt', u'Freifunk Rheinland e.V.', u'TNG - The Net Generation AG/Ennit', u'Clusters KG', u'noris network AG', u'Google Inc.', u'IPHH Internet Port Hamburg GmbH', u'D-Hosting GmbH', u'Artfiles New Media GmbH', u'Google Inc.', u'QSC AG', u'ADDIX Internet Services GmbH', u'Opteamax GmbH', u'Akamai Technologies', u'Hibernia Networks', u'Kabel Deutschland Vertrieb und Service GmbH', u'Wieskes Crew GmbH', u'ScaleUp Technologies GmbH & Co. KG', u'SOCO Network Solutions GmbH', u'OpenCarrier e.G.', u'GOPAS Solutions GmbH', u'Kaia Global Networks Ltd.', u'Individual Network Berlin e.V.', u'Netsign GmbH', u'PHADE Software - PowerWeb', u'AS112 Project hosted by IN-Berlin', u'MESH GmbH', u'terralink GmbH', u'DENIC eG, Anycast .de DNS service', u'MPeX.net GmbH', u'AS250.net Network Operations', u'Inter.Net Germany', u'Telef\xf3nica Deutschland']
```

#### List imported data by ASN
```python
>>> members.list_asn()
>>> [13184, 34568, 1547, 3856, 20783, 50324, 12693, 13335, 6724, 6939, 15388, 20647, 50472, 15657, 42, 15943, 201701, 13101, 41391, 12337, 36040, 12731, 12732, 8893, 15169, 20676, 25415, 48200, 20940, 5580, 31334, 13135, 29014, 12759, 41692, 13157, 251, 29670, 31078, 35053, 112, 25074, 59507, 31529, 35833, 250, 34171, 6805]
```

#### List imported data by IP
```python
>>> members.list_ip()
>>> [u'194.9.117.17', u'194.9.117.8', u'194.9.117.68', u'194.9.117.9', u'194.9.117.52', u'194.9.117.66', u'194.9.117.50', u'194.9.117.74', u'194.9.117.61', u'194.9.117.51', u'194.9.117.56', u'194.9.117.72', u'194.9.117.48', u'194.9.117.25', u'194.9.117.7', u'194.9.117.64', u'194.9.117.75', u'194.9.117.19', u'194.9.117.36', u'194.9.117.29', u'194.9.117.71', u'194.9.117.49', u'194.9.117.3', u'194.9.117.2', u'194.9.117.15', u'194.9.117.34', u'194.9.117.53', u'194.9.117.44', u'194.9.117.47', u'194.9.117.73', u'194.9.117.67', u'194.9.117.60', u'194.9.117.62', u'194.9.117.63', u'194.9.117.20', u'194.9.117.12', u'194.9.117.42', u'194.9.117.13', u'194.9.117.57', u'194.9.117.55', u'194.9.117.5', u'194.9.117.6', u'194.9.117.4', u'194.9.117.31', u'194.9.117.112', u'194.9.117.1', u'194.9.117.58', u'194.9.117.37', u'194.9.117.41', u'194.9.117.114', u'194.9.117.26', u'194.9.117.39', u'194.9.117.38', u'194.9.117.54']
```

#### List imported data by IPv6
```python
>>> members.list_ipv6()
>>> [u'2001:7f8:8:5:0:3380:0:1', u'2001:7f8:8:5:0:60b:0:1', u'2001:7f8:8:5:0:f10:0:1', u'2001:7f8:8:5:0:512f:0:1', u'2001:7f8:8:5:0:c494:0:1', u'2001:7f8:8:5:0:3195:0:1', u'2001:7f8:8:5:0:3417:0:1', u'2001:7f8:8:5:0:1a44:0:1', u'2001:7f8:8:5:0:1b1b:0:1', u'2001:7f8:8:5:0:3c1c:0:1', u'2001:7f8:8:5:0:50a7:0:1', u'2001:7f8:8:5:0:c528:0:1', u'2001:7f8:8:5:0:3d29:0:1', u'2001:7f8:8:5:0:2a:0:1', u'2001:7f8:8:5:0:3e47:0:1', u'2001:7f8:8:5:3:13e5:0:1', u'2001:7f8:8:5:0:332d:0:1', u'2001:7f8:8:5:0:a1af:0:1', u'2001:7f8:8:5:0:31bb:0:1', u'2001:7f8:8:5:0:31bc:0:2', u'2001:7f8:8:5:0:31bc:0:1', u'2001:7f8:8:5:0:22bd:0:1', u'2001:7f8:8:5:0:3b41:0:1', u'2001:7f8:8:5:0:50c4:0:1', u'2001:7f8:8:5:0:6347:0:1', u'2001:7f8:8:5:0:bc48:0:1', u'2001:7f8:8:5:0:51cc:0:2', u'2001:7f8:8:5:0:51cc:0:1', u'2001:7f8:8:5:0:15cc:0:1', u'2001:7f8:8:5:0:7a66:0:1', u'2001:7f8:8:5:0:7a66:0:2', u'2001:7f8:8:5:0:334f:0:1', u'2001:7f8:8:5:0:7156:0:1', u'2001:7f8:8:5:0:31d7:0:1', u'2001:7f8:8:5:0:a2dc:0:1', u'2001:7f8:8:5:0:fb:0:1', u'2001:7f8:8:5:0:73e6:0:1', u'2001:7f8:8:5:0:73e6:0:2', u'2001:7f8:8:5:0:7966:0:1', u'2001:7f8:8:5:0:70:0:1', u'2001:7f8:8:5:0:7b29:0:1', u'2001:7f8:8:5:0:fa:0:2', u'2001:7f8:8:5:0:fa:0:1', u'2001:7f8:8:5:0:857b:0:1', u'2001:7f8:8:5:0:1a95:0:1']
```

License
======

Copyright 2015 BigWaveIT.

Licensed under the Apache License, Version 2.0: http://www.apache.org/licenses/LICENSE-2.0
