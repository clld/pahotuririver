from setuptools import setup, find_packages


setup(
    name='pahotuririver',
    version='0.0',
    description='pahotuririver',
    classifiers=[
        "Programming Language :: Python",
        "Framework :: Pyramid",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: WSGI :: Application",
    ],
    author='',
    author_email='',
    url='',
    keywords='web pyramid pylons',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'clld',
        'clld-audio-plugin>=1.2.0',
        'clldmpg',

],
extras_require={
        'dev': ['flake8', 'waitress'],
        'test': [
            'mock',
            'pytest>=5.4',
            'pytest-clld',
            'pytest-mock',
            'pytest-cov',
            'coverage>=4.2',
            'selenium',
            'zope.component>=3.11.0',
        ],
    },
    test_suite="pahotuririver",
    entry_points="""\
    [paste.app_factory]
    main = pahotuririver:main
""")
