from os import path
from setuptools import setup

with open(path.join(path.dirname(path.abspath(__file__)), 'README.rst')) as f:
    readme = f.read()

setup(
      name             =   'mpcs',
      version          =   '1.0.12',
      description      =   'This app simulates an MPC compute call and creates a z-score file.', 
      long_description =   readme,
      author           =   'Rudolph Pienaar',
      author_email     =   'rudolph.pienaar@gmail.com',
      url              =   'https://github.com/FNNDSC/pl-mpcs',
      packages         =   ['mpcs'],
      install_requires =   ['chrisapp', 'pudb', 'numpy'],
      test_suite       =   'nose.collector',
      tests_require    =   ['nose'],
      scripts          =   ['mpcs/mpcs.py'],
      license          =   'MIT',
      zip_safe         =   False,
      python_requires  = '>=3.5'
     )
