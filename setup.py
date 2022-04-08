import setuptools
import subprocess
import os

remote_version = (
    subprocess.run(["git", "describe", "--tags"], stdout=subprocess.PIPE)
    .stdout.decode("utf-8")
    .strip()
)

if "-" in remote_version:
    v, i, s = remote_version.split("-")
    remote_version = v + "+" + i + ".git." + s

assert "-" not in remote_version
assert "." in remote_version

assert os.path.isfile("remote/version.py")
with open("remote/VERSION", "w", encoding="utf-8") as fh:
    fh.write(f"{remote_version}\n")

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name='getBCE',
    packages=setuptools.find_packages(),
    package_data={"getBCE": ["VERSION"]},
    version=remote_version,
    description='Download data from BCE (Banco Central del ecuador) webpage',
    author='S. Daniel Jaramillo',
    author_email='losteven2018@outlook.com',
    url='https://github.com//Daniejar27/BCE',
    download_url='https://github.com//Daniejar27/BCE',
    keywords=['Economics', 'Banco Central', 'BCE', 'economía'],
    classifiers=[],
    install_requires=['requests', 'pandas', 'bs4', 'urllib3']
)
