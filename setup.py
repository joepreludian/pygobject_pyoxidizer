# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['preludian']

package_data = \
{'': ['*']}

install_requires = \
['PyGObject>=3.42.0,<4.0.0']

entry_points = \
{'console_scripts': ['prelude-init = preludian.main:run']}

setup_kwargs = {
    'name': 'mypygtk',
    'version': '0.1.0',
    'description': '',
    'long_description': '# PyGObject Hello world\n\nSimple POC application in order to validate GTK3 project;\n',
    'author': 'Jonhnatha Trigueiro (Compute Engineer)',
    'author_email': 'joepreludian@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'entry_points': entry_points,
    'python_requires': '>=3.9,<4.0',
}


setup(**setup_kwargs)

# This setup.py was autogenerated using poetry.