#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import, print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    return io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get('encoding', 'utf8')
    ).read()

with open("requirements.txt", "r") as f:
    install_requires = [x.strip() for x in f.readlines() if not
                        x.startswith(("ddb-", "http", "git"))]


setup(
    name='ddb-ngsflow',
    version='0.1.0',
    license='BSD',
    description='A toil based NGS workflow manager',
    long_description='%s\n%s' % (
        re.compile('^.. start-badges.*^.. end-badges', re.M | re.S).sub('', read('README.rst')),
        re.sub(':[a-z]+:`~?(.*?)`', r'``\1``', read('CHANGELOG.rst'))
    ),
    author='Dan Gaston',
    author_email='daniel.gaston@deaddriftbio.com',
    url='https://github.com/dgaston/ddb-ngsflow',
    packages=['ddb_ngsflow', 'ddb_ngsflow.align', 'ddb_ngsflow.utils', 'ddb_ngsflow.variation',
              'ddb_ngsflow.variation.sv', 'ddb_ngsflow.rna', 'ddb_ngsflow.qc', 'ddb_ngsflow.coverage'],
    # package_dir={'ddb-ngsflow': 'ddb_ngsflow'},
    # py_modules=[splitext(basename(path))[0] for path in glob('ddb_ngsflow/*.py')],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list: http://pypi.python.org/pypi?%3Aaction=list_classifiers
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: Unix',
        'Operating System :: POSIX',
        'Operating System :: Microsoft :: Windows',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        # uncomment if you test on these interpreters:
        # 'Programming Language :: Python :: Implementation :: IronPython',
        # 'Programming Language :: Python :: Implementation :: Jython',
        # 'Programming Language :: Python :: Implementation :: Stackless',
        'Topic :: Utilities',
    ],
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    install_requires=install_requires,
    requires=['python (>=2.7, <3.0)'],
    extras_require={
        # eg:
        #   'rst': ['docutils>=0.11'],
        #   ':python_version=="2.6"': ['argparse'],
    },
)
