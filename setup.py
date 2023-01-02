from setuptools import setup

setup(
	  name='ALIOCrawler', 
	  version='1.0.2',  
	  description='::A simple tool to extract job info. from ALIO website::',
	  long_description= 'This is the first upload...', 
	  author='wjgoarxiv',
	  author_email='woo_go@yahoo.com',
	  url='https://pypi.org/project/ALIOCrawler/',
	  license='MIT',
	  py_modules=['ALIOCrawler'],
	  python_requires='>=3.8', #python version required
	  install_requires = [
	  'selenium',
	  'beautifulsoup4',
	  'html5lib',
	  'requests',
	  'pandas',
	  'argparse',
	  'numpy',
	  'matplotlib',
		'seaborn',
		'chromedriver-autoinstaller',
		'pyfiglet'
	  ],
	  packages=['ALIOCrawler'],
		entry_points={
			'console_scripts': [
				'aliocrawler = ALIOCrawler.__main__:main'
			]
		}
)