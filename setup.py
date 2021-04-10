"""Install the package sailsim."""

import setuptools

setuptools.setup(
    name='sailsim',
    version='0.1',
    description='A program to simulate sailboats',
    author='Tillman Keller & Michael Behrens',
    author_email='mfbehrens99@gmail.com',
    packages=setuptools.find_packages(),
    url='github.com/mfbehrens99/sailsim',
    long_description=open('README.md').read(),
    python_requires='>=3',
    install_requires=['opensimplex', "PySide6"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
    ],
    # entry_points={
    #     'console_scripts': [
    #         'sailsim.gui:main',
    #     ]
    # }
)
