from setuptools import setup

setup(
    name='dnd-cli',
    version='0.1',
    py_modules=['dnd_cli'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        dnd=dnd_cli:cli
    ''',
)
