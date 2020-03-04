from setuptools import setup, Extension
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
  name = 'aaransia',         # How you named your package folder (MyLib)
  packages = ['aaransia'],   # Chose the same as "name"
  version = '0.31',      # Start with a small number and increase it with every change you make
  license='Apache License 2.0',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Languages and Dialects transliteration',   # Give a short description about your library
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Amine M. Boulouma',                   # Type in your name
  author_email = 'amine@boulouma.com',      # Type in your E-Mail
  url = 'https://github.com/3aransia/3aransia',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/3aransia/3aransia/dist/aaransia-0.1.2.tar.gz',    # I explain this later on
  keywords = ['python', 'nlp', 'language', 'moroccan', '3aransia'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'pandas',
          'numpy',
          'unidecode',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: Apache Software License',   # Again, pick a license
    'Programming Language :: Python :: 3',      #Specify which pyhton versions that you want to support
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)