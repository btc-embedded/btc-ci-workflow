from setuptools import setup, find_packages

setup(
    name='btc_rest_api',
    version='23.2.0',
    description='API wrapper for BTC EmbeddedPlatform 23.2p0 REST API',
    author='Thabo Krick',
    author_email='thabo.krick@btc-embedded.com',
    url='https://github.com/btc-embedded/btc-ci-workflow/examples/api',
    packages=find_packages(),  # Automatically discover and include all packages
    install_requires=['requests'],
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
