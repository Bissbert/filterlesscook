from setuptools import setup, find_packages

setup(
    name='FilterlessCook',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'ollama',  # assuming 'ollama' needs to be installed via pip
    ],
    entry_points={
        'console_scripts': [
            'filterless-cook=filterlesscook:main',
        ],
    },
    author='Bissbert',
    author_email='dev@bissbert.ch',
    description='Generate LaTeX formatted food recipes using the ollama library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/Bissbert/filterlesscook',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='recipe generator latex unfiltered filterless',
)