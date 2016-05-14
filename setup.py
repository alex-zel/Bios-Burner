from distutils.core import setup
import py2exe
import sys
import os

sys.path.insert(0, r'C:\Python34\Lib\site-packages\psutil')

sys.argv.append('py2exe')

setup(console=[{"script": "main.py"}],
      options={'py2exe': {'packages': ["psutil"], 'bundle_files': 2, 'compressed': True}},
      zipfile=None,)


