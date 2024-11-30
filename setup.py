from setuptools import setup, find_packages

requirements = [
    'aiohttp',
]

with open('README.md', encoding='UTF-8') as f:
    readme = f.read()

setup(
    name = 'aiolang',
    version = '1.0.0',
    author='stone',
    author_email = 'aiolang.python@gmail.com',
    description = 'A fast and asynchronous text translator library for personal use and frameworks.',
    keywords = ['translate', 'aiolang', 'aio', 'lang', 'google', 'asyncio'],
    long_description = readme,
    python_requires="~=3.9",
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/S5W1n72/aiolang',
    packages = find_packages(),
    exclude_package_data = {'': ['*.pyc', '*__pycache__*']},
    install_requires = requirements,
    classifiers=[
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'License :: OSI Approved :: GNU Lesser General Public License (LGPL)',
        'Topic :: Internet',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Software Development :: Libraries :: Application Frameworks'
    ],
)
