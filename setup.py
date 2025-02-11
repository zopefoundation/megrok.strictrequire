import os.path

from setuptools import setup


version = '5.1.dev0'


detailed = open(
    os.path.join('src', 'megrok', 'strictrequire', 'README.rst')).read()


changes = open('CHANGES.rst').read()


long_description = '\n\n'.join([detailed, changes, ''])


tests_require = [
    'zope.component',
    'zope.interface',
    'zope.securitypolicy',
    'zope.testing',
    'zope.testrunner >= 6.4',
]


setup(
    name='megrok.strictrequire',
    version=version,
    description=(
        'Checks that all grokked "view-like" components '
        'require a permission.'),
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "License :: OSI Approved :: Zope Public License",
        "Natural Language :: English",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
    ],
    keywords=[],
    author='The Health Agency',
    author_email='zope-dev@zope.dev',
    url='https://github.com/zopefoundation/megrok.strictrequire/',
    license='ZPL-2.1',
    package_dir={'': 'src'},
    packages=['megrok.strictrequire'],
    include_package_data=True,
    zip_safe=False,
    python_requires='>=3.9',
    install_requires=[
        'setuptools',
        'martian',
        'grok >= 5.0a1',
    ],
    extras_require={
        'test': tests_require
    },
    tests_require=tests_require,
    entry_points={},
)
