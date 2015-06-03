from distutils.core import setup

add_keywords = dict(
    entry_points={
        'console_scripts': ['logmein-windows = logmein-windows.main:main'],
    }, )

fhan = open('requirements.txt', 'rU')
requires = [line.strip() for line in fhan.readlines()]
fhan.close()
#print('We require: ', requires)
try:
    import pypandoc
    long_description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    fhan = open('README.txt')
    long_description = fhan.read()
    fhan.close()

setup(
    name='LogMeIn Windows',
    description='LogMeIn Windows provides a GUI over LogMeIn',
    version='0.0.8',
    packages=['logmein-windows'],
    license='GPLv3+',
    author='Shubham Chaudhary',
    author_email='me@shubhamchaudhary.in',
    url='https://github.com/DevelopFreedom/logmein-windows',
    long_description=long_description,
    install_requires=requires, **add_keywords)
