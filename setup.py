from setuptools import setup

setup(
    name='data_structures_and_algo',
    packages=[
        'src',
        'src.trees',
        'src.linked_lists',
        'src.arrays',
        'src.sorting',
        'src.heaps',
        'src.queues',
        'src.recursion'
    ],
    include_package_data=True,
    install_requires=[],
    setup_requires=['pytest-runner'],
    tests_require=['pytest'],
)
