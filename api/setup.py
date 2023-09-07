from setuptools import find_packages, setup

setup(
    name='btc_rest_api',
    version='2.11.1',
    description='API wrapper for BTC EmbeddedPlatform 2.11p1 REST API',
    author='Thabo Krick',
    author_email='thabo.krick@btc-embedded.com',
    url='https://github.com/btc-embedded/btc-ci-workflow/api',
    packages=find_packages(),
    install_requires=[ 'requests', 'pyyaml' ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
