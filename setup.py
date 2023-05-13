import setuptools

with open('README.md', 'r', encoding='utf-8') as fh:
    long_description = fh.read()

exec(open("src/slexil/version.py").read())

setuptools.setup(
    name='slexil_package',
    version = __version__,	
    author='Paul Shannon',
    author_email='paul.thurmond.shannon@gmail.com',
    description='Software Linking ELAN XML to Illuminated Language',
    keywords='slexil, ELAN, IJAL',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/paul-shannon/slexil2',
    project_urls={
        'Documentation': 'https://github.com/paul-shannon/slexil2',
        'Bug Reports':
        'https://github.com/paul-shannon/slexil2/issues',
        'Source Code': 'https://github.com/paul-shannon/slexil2',
        # 'Funding': '',
        # 'Say Thanks!': '',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        # see https://pypi.org/classifiers/
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
    # install_requires=['Pillow'],
    extras_require={
        'dev': ['check-manifest'],
        # 'test': ['coverage'],
    },

)
