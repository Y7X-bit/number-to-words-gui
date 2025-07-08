from setuptools import setup, find_packages

setup(
    name='number_to_words_gui',
    version='1.0',
    packages=find_packages(),
    install_requires=[
        'customtkinter',
    ],
    entry_points={
        'console_scripts': [
            'number-to-words = main_script:main',
        ],
    },
    author='Yugank Singh',
    description='A beautiful AMOLED-themed GUI app to convert numbers to words.',
)
