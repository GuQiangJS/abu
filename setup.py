from setuptools import setup,find_packages

NAME='abupy'


def readme():
    with open('README.md', encoding='utf-8') as f:
        return f.read()


setup(
    name=NAME,
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    keywords='data',
    packages=find_packages(),
    zip_safe=False,
    exclude_package_data={'': ['test_*.py']}
)