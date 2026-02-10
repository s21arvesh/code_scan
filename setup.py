from setuptools import setup, find_packages

setup(
    name="test-project",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "requests==2.25.1",  # Vulnerable dependency
        "urllib3==1.26.0",   # Vulnerable dependency
        "flask==1.0.0"
    ],
    author="Test Author",
    license="MIT"
)
