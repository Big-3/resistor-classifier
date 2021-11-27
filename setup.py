#!/usr/bin/env python3

from setuptools import setup
from pathlib import Path

BASE_DIR=Path(__file__).resolve()
setup(
	name='resistor-classifier',
	version='0.0.1',
	packages=['classifierlib', 'test'],
	install_requires=[
		'matplotlib', 
		'Pillow', 
		'scikit-image', 
		'scikit-learn',
		'chain'
	]
)