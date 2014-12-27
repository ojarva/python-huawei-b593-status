Huawei B593 status fetcher
==========================

This small library fetches status information from Huawei B593 4G modem.

Installation:

::

  pip install huawei_b593_status

or clone `the repository <https://github.com/ojarva/python-huawei-b593-status>`_ and run

::

  python setup.py install

Usage:

::

  import huawei_b593_status
  huawei = HuaweiStatus()
  print huawei.read()

Output:

::

  {'WIFI': 'off',
   'SIG': '5',
   'Mode': '4g',
   'Roam': 'home',
   'SIM': 'normal',
   'Connect': 'connected'}

