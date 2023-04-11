from setuptools import setup, find_packages
import os

current_folder = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_folder, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(
  name='scaffoldPandas',
  version='0.16',
  description='Helpful functions for pandas',
  long_description=long_description,
  long_description_content_type='text/markdown',
  url='https://github.com/PatrickArchambault-EquipeRecherche/scaffold-pandas',
  author='William Witteman',
  author_email='william@witteman.ca',
  license='GPL3',
  packages=find_packages(exclude='tests'),
  python_requires='>=3.7',
)
