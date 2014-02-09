from setuptools import setup, find_packages

setup(
    name = "django-viewrouter",
    version = "0.1",
    packages = find_packages(exclude=['myapp', 'manage.py']),
)
