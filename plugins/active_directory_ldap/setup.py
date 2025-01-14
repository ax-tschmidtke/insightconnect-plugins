# GENERATED BY INSIGHT-PLUGIN - DO NOT EDIT
from setuptools import setup, find_packages


setup(name="active_directory_ldap-rapid7-plugin",
      version="9.0.1",
      description="This plugin utilizes Microsoft's Active Directory service to create and manage domains, users, and objects within a network",
      author="rapid7",
      author_email="",
      url="",
      packages=find_packages(),
      install_requires=['insightconnect-plugin-runtime'],  # Add third-party dependencies to requirements.txt, not here!
      scripts=['bin/komand_active_directory_ldap']
      )
