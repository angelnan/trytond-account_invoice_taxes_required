#!/usr/bin/env python
#This file is part of Tryton.  The COPYRIGHT file at the top level of
#this repository contains the full copyright notices and license terms.

from setuptools import setup
import re

info = eval(open('__tryton__.py').read())
major_version, minor_version, _ = info.get('version', '0.0.1').split('.', 2)
major_version = int(major_version)
minor_version = int(minor_version)

requires = ['python-dateutil']
for dep in info.get('depends', []):
    if not re.match(r'(ir|res|workflow|webdav)(\W|$)', dep):
        requires.append('trytond_%s >= %s.%s, < %s.%s' %
                (dep, major_version, minor_version, major_version,
                    minor_version + 1))
requires.append('trytond >= %s.%s, < %s.%s' %
        (major_version, minor_version, major_version, minor_version + 1))

setup(name='account_invoice_taxes_required',
    version=info.get('version', '0.0.1'),
    description=info.get('description', ''),
    author=info.get('author', ''),
    author_email=info.get('email', ''),
    url=info.get('website', ''),
    download_url=("https://bitbucket.org/albertnan/account_invoice_taxes_required" + 
            info.get('version', '0.0.1').rsplit('.', 1)[0] + '/'),
    package_dir={'trytond.modules.account_invoice_taxes_required': '.'},
    packages=[
        'trytond.modules.account_invoice_taxes_required',
        'trytond.modules.account_invoice_taxes_required.tests',
        ],
    package_data={
        'trytond.modules.account_invoice_taxes_required': (
            info.get('xml', []) 
            + info.get('translation', []) 
            + ['*.odt', 'icons/*.svg']
            ),
        },
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Plugins',
        'Framework :: Tryton',
        'Intended Audience :: Developers',
        'Intended Audience :: Financial and Insurance Industry',
        'Intended Audience :: Legal Industry',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Office/Business',
        'Topic :: Office/Business :: Financial :: Accounting',
    ],
    license='GPL-3',
    install_requires=requires,
    zip_safe=False,
    entry_points=("""
    [trytond.modules]
    account_invoice_taxes_required = trytond.modules."""
        "account_invoice_taxes_required"),
    test_suite='tests',
    test_loader='trytond.test_loader:Loader',
)
