from setuptools import setup

setup(
    name='dev_aberto_guilhermedr',
    version='0.1',
    packages=['dev_aberto'],
    author='Guilherme Rameh',
    python_requires='>=3.6',
    install_requires=[
        'requests',
        'Babel'
    ],
    scripts=['scripts/hello.py'],
)