from setuptools import setup, find_packages

print('PACKAGES: ',find_packages())

setup(
    name='foliumgee',
    version='0.1',
    description='Package to view Google Earth Engine Tile Layer in Folium.',
    classifiers=[
        'Programming Language :: Python :: 3.6',
    ],
    keywords='folium gee gis',
    author='Ryan McCarthy',
    author_email='mccarthyryanc@gmail.com',
    license='MIT',
    install_requires=[
        'oauth2client',
        'folium',
        'earthengine-api',
    ],
    package_dir={'': '.'},
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
)