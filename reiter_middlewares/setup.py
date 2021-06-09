import os
from setuptools import setup, find_packages


version = "0.1"

install_requires = [
    "horseman",
    "reiter.application",
    "fanstatic",
    "wsgi-basic-auth"
]

test_requires = [
]


setup(
    name='reiter_middleware',
    version=version,
    author='Souheil Chelfouh',
    author_email='contact@example.com',
    url='http://www.example.com',
    download_url='',
    description='A demo.',
    long_description="Horsebox deployment for a minimal Reiter app.",
    license='ZPL',
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Zope Public License',
        'Programming Language :: Python:: 3 :: Only',
    ],
    packages=find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    zip_safe=False,
    install_requires=install_requires,
    extras_require={
        'test': test_requires,
    },
    entry_points={
       "fanstatic.libraries": [
          "reiter_middleware = reiter_middleware:library",
       ],
    }
)
