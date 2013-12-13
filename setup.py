from setuptools import setup, find_packages
import os

version = '1.1.0'

tests_require = [
    'ftw.testing [splinter]',
    'plone.app.testing',
    'plone.resource',
    'unittest2',
    ]

setup(name='ftw.slider',
      version=version,
      description='Slider content type for Plone.',
      long_description=open('README.rst').read() + '\n' +
      open(os.path.join('docs', 'HISTORY.txt')).read(),

      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone :: 4.3',
        'Framework :: Plone',
        'Programming Language :: Python',
        ],
      keywords='',

      author='4teamwork GmbH',
      author_email='mailto:info@4teamwork.ch',
      url='https://github.com/4teamwork/ftw.slider',
      license='GPL2',

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
        'plone.formwidget.contenttree',
        'plone.namedfile',
        'plone.dexterity',
        'plone.app.dexterity',
        'plone.directives.form',
        'z3c.relationfield',
        ],
      tests_require=tests_require,
      extras_require=dict(tests=tests_require),

      entry_points='''
      # -*- Entry points: -*-
      [z3c.autoinclude.plugin]
      target = plone
      ''',
      )
