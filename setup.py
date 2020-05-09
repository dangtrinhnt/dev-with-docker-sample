from setuptools import setup, find_packages


def requirements():
    with open('requirements.txt') as f:
        req = f.read().splitlines()
    return req


def test_requirements():
    with open('test-requirements.txt') as f:
        req = f.read().splitlines()
    return req


def readme():
    with open('README.md') as f:
        return f.read()


setup(
    name='dev-with-docker-sample',
    version='0.0.1',
    description='Development with Docker Sample',
    long_description=readme(),
    classifiers=[
        'Development Status :: Active',
        'License :: OSI Approved :: Apache 2.0 License',
        'Programming Language :: Python :: 3',
    ],
    keywords='',
    url='https://github.com/dangtrinhnt/dev-with-docker-sample/',
    author='Trinh Nguyen',
    author_email='dangtrinhnt@gmail.com',
    license='Apache 2.0',
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),
    install_requires=requirements(),
    setup_requires=[],
    tests_require=test_requirements(),
    cmdclass={},
    include_package_data=True,
    zip_safe=False
)