from setuptools import setup, find_packages


setup(
    author_name='Abhishek Bhatia',
    author_email='bhatiaabhishek8893@gmail',
    name='src',
    version='0.0.1',
    packages=find_packages(include=['src', 'src', 'project', 'project.*']),
    python_requires='>=3.6.*'
)