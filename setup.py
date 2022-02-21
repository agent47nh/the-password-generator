from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

setup(
    name='thepasswordgenerator',
    version='1.0.0',
    author='Naimul Hasan',
    author_email='agent47nh9@gmail.com',
    url='https://github.com/agent47nh/the-password-generator',
    license='AGPLv3',
    description='Generate passwords within your scripts or programs in one line!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    package_dir={'': 'src'},
    packages=find_packages(where='src'),
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3.9',
    ],
    keywords='passwords generator password-generator',
    project_urls={
        'Documentation': 'https://github.com/agent47nh/the-password-generator/blob/master/README.md',
        'Source': 'https://github.com/agent47nh/the-password-generator',
        'Tracker': 'https://github.com/agent47nh/the-password-generator/issues',
    },
    python_requires='>=3',
)
