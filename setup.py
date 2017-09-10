from setuptools import setup

setup(
    name = 'snapbtr',
    description = 'Simple btrfs snapshots management',
    version = '0.1',
    scripts = ['snapbtr'],
    url = 'https://github.com/yvolchkov/snapbtr',
    keywords = ['btrfs', 'snapshot', 'backup'],

    author = 'Yuri Volchkov',
    author_email = 'yuri.volchkov@gmail.com',
    install_requires=[
        'colorama',
    ],

    python_requires='>=2.7, <3',

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Topic :: System :: Filesystems',
        'Intended Audience :: System Administrators',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ]
)
