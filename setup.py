from setuptools import setup, find_packages

#gui scripts allows us to run the program without opening a terminal window
setup(
  name='Document Tag Parser Setup File',
  version='1.0',
  packages=find_packages(),
  entry_points={
    'console_scripts': [
      'my_start=pdf_parser:Ui'
    ]
  }  
)