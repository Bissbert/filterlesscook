from setuptools import setup, find_packages

setup(
    name='RecipeGenerator',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'ollama',  # assuming 'ollama' needs to be installed via pip
    ],
    entry_points={
        'console_scripts': [
            'recipe-generator=recipeGenerator:main',
        ],
    },
    author='Your Name',
    author_email='your.email@example.com',
    description='Generate LaTeX formatted food recipes using the ollama library.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='http://github.com/yourusername/recipegenerator',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='recipe generator latex',
)