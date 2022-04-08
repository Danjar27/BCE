from distutils.core import setup

setup(
    name='getBCE',
    packages=['getBCE'],
    package_data={"getBCE": ["VERSION"]},
    version="1.5.1",
    description='Download data from BCE (Banco Central del ecuador) webpage',
    author='S. Daniel Jaramillo',
    author_email='losteven2018@outlook.com',
    url='https://github.com//Daniejar27/BCE',
    download_url='https://github.com//Daniejar27/BCE',
    keywords=['Economics', 'Banco Central', 'BCE', 'economía'],
    python_requires=">= 3.8",
    classifiers=[],
    install_requires=['requests', 'pandas', 'bs4', 'urllib3']
)
