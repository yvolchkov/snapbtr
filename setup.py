from setuptools import setup

setup(
    name = 'snapbtr',
    description = 'Simple btrfs snapshots management',
    version = '0.1',
    scripts = ['snapbtr'],

    author = 'Yuri Volchkov',
    author_email = 'yuri.volchkov@gmail.com',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Filesystems',
        'Intended Audience :: System Administrators',
    ]
)
