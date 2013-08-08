from setuptools import setup, find_packages
import os

version = '1.0.dev0'

tests_require = [
    'ftw.testing [splinter]',
    'plone.app.testing',
    'plone.resource',
    'unittest2',
    ]

setup(name='ftw.slider',
      version=version,
      description="Slider package",
      long_description=open("README.rst").read() + "\n" +
      open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='Julian Infanger',
      author_email='info@4teamwork.ch',
      url='http://www.4teamwork.ch',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['ftw'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
        'setuptools',
        'Products.GenericSetup',
        'Products.CMFCore',
        'Products.CMFPlone',
        'plone.behavior',
        'plone.namedfile',
        'plone.dexterity',
        'plone.app.dexterity',
        'plone.directives.form',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),
      entry_points="""
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
