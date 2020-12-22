import os
from distutils.core import setup
from distutils.command.sdist import sdist

import bowditch  # safe, because __init__.py contains no import statements

class my_sdist(sdist):
    def make_distribution(self):
        # See https://github.com/skyfielders/python-skyfield/issues/378
        for path in self.filelist.files:
            os.chmod(path, 0o644)
        sdist.make_distribution(self)

setup(
    cmdclass={'sdist': my_sdist},
    name='bowditch',
    version=bowditch.__version__,
    description=bowditch.__doc__.split('\n', 1)[0],
    long_description=open('README.md', 'rb').read().decode('utf-8'),
    license='MIT',
    author='Josh Paterson',
    author_email='mail@joshpaterson.com',
    url='http://github.com/JoshPaterson/bowditch/',
    packages=[
        'bowditch',
        'bowditch.data',
        'bowditch.tests',
        ],
    install_requires=[
        'numpy',
        ],
)