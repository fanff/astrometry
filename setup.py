from setuptools import setup

setup(
    name='astrometry-np',
    version='0.0.1',
    author='Fanf',
    description='Simple python3 tool to quickly correct the rough astronometry given by a telescope for a fits image.',
    entry_points={},
    install_requires=['astroquery',
                      'astropy',
                      'photutils',
                      'matplotlib',
                      'pandas',
                      'numpy',
                      'scipy'
                      ]
)
