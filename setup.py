from setuptools import setup

setup(
	name='plast',
	version='0.1',
	py_modules=['plast'],
	install_requires=[
		'Click',
	],
	entry_points='''
		[console_scripts]
		plast=plast:cli
	''',
)