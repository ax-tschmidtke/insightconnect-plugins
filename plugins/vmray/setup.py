# GENERATED BY KOMAND SDK - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="vmray-rapid7-plugin",
      version="5.0.1",
      description="Analyze and detect malware before it lands, protecting internal infrastructure",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['komand'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_vmray']
      )