from os import path
from setuptools import find_packages, setup

with open(path.join(path.dirname(__file__), 'README.md')) as readme:
    LONG_DESCRIPTION = readme.read()

setup(
    name='jupyter_bookkeeping',
    version = "0.0.2",
    description='jupyter widgets for working with financial data',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    url='https://github.com/dimonf/jupyter-bookkeeping',
    author='Dmitri Kurbatskiy',
    author_email='camel109@gmail.com',
    license='GPL-3.0',
    keywords='jupyter widget financial',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'ipywidgets',
    ],
    zip_safe=False,
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Financial and Insurance Industry',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3.6',
        'Topic :: Office/Business :: Financial :: Accounting',
        'Topic :: Office/Business :: Financial :: Investment',
    ],
    python_requires='>=3.6',
)
