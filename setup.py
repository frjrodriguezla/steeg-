from setuptools import setup , find_packages

classifiers = [
    #'Development Status :: 5 - Production/Stable',
    'Development Status :: 4 - Beta',
    'Intended Audience :: Science/Research',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3 :: Only',
]

with open('README.md') as f:
    long_description = f.read()

setup(

  name = 'steeg',
  packages = find_packages('src'),
  package_dir={'': 'src'},
  version = '0.1.4',
  description = ' ',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author = 'Francisco R. Lanza',
  author_email = 'frjrodriguezla@unal.edu.co',
  license='MIT',
  url = 'https://github.com/frjrodriguezla/oecx',
  keywords = ['mne', 'eeg','nolds'],
  classifiers = classifiers,
  install_requires=['mne','nolds','numpy'],
  python_requires='~=3.3',
  py_modules=['steeg']
)
