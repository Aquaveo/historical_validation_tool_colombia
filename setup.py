from setuptools import setup, find_namespace_packages
from tethys_apps.app_installation import find_resource_files

# -- Apps Definition -- #
app_package = 'historical_validation_tool_colombia'
release_package = 'tethysapp-' + app_package

# -- Python Dependencies -- #
dependencies = []

# -- Get Resource File -- #
resource_files = find_resource_files('tethysapp/' + app_package + '/templates', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/public', 'tethysapp/' + app_package)
resource_files += find_resource_files('tethysapp/' + app_package + '/workspaces', 'tethysapp/' + app_package)

setup(
    name=release_package,
    version='1.2',
    description='This app combines the observed data and the simulated data from the GEOGloWS ECMWF Streaamflow Services in Colombia.',
    long_description='',
    keywords='"Hydrology", "Time Series", "Bias Correction", "Hydrostats", "GEOGloWS", "Historical Validation Tool", "Colombia"',
    author='Jorge Luis Sanchez-Lozano, Jhonatan Rodriguez Chaves',
    author_email='jorgessanchez7@gmail.com, jhrodriguezch@unal.edu.co',
    url='',
    license='',
    packages=find_namespace_packages(),
    package_data={'': resource_files},
    include_package_data=True,
    zip_safe=False,
    install_requires=dependencies,
)
