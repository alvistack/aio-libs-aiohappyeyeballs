# -*- coding: utf-8 -*-
from setuptools import setup

package_dir = \
{'': 'src'}

packages = \
['aiohappyeyeballs']

package_data = \
{'': ['*']}

setup_kwargs = {
    'name': 'aiohappyeyeballs',
    'version': '2.4.4',
    'description': 'Happy Eyeballs for asyncio',
    'author': 'J. Nick Koston',
    'author_email': 'nick@koston.org',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'https://github.com/aio-libs/aiohappyeyeballs',
    'package_dir': package_dir,
    'packages': packages,
    'package_data': package_data,
    'python_requires': '>=3.8',
}


setup(**setup_kwargs)
