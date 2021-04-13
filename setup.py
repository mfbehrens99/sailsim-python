"""Install the package sailsim."""

import setuptools

setuptools.setup(
    name='sailsim',
    version='0.0.1',
    description='A program to simulate sailboats and test sailing algorithms.',
    author='Tillman Keller & Michael Behrens',
    author_email='mfbehrens99@gmail.com',
    packages=setuptools.find_packages(),
    url='https://github.com/mfbehrens99/sailsim',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    python_requires='>=3',
    install_requires=['opensimplex'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'sailsim.gui:main',
    #     ]
    # }
)
