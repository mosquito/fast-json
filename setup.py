from setuptools import setup


setup(
    name='fast-json',
    version='0.2.1',
    platforms="all",
    author="Dmitry Orlov",
    author_email="me@mosquito.su",
    maintainer="Dmitry Orlov",
    maintainer_email="me@mosquito.su",
    description="Combines best parts of json and ujson for fast serialization",
    package_dir={'': 'src'},
    packages=[''],
    install_requires=["ujson"],
    license="Apache 2",
    long_description=open('README.rst').read(),
    classifiers=[
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
