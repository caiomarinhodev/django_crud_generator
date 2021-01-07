import codecs
from setuptools import setup


def readme():
    with codecs.open('README.md') as f:
        return f.read()


setup(
    name='django_crud_generator',
    version='0.3.10',
    description='A simple scaffolding for django applications',
    long_description=readme(),
    long_description_content_type="text/markdown",
    keywords='django scaffolding tool',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
    license='MIT',
    packages=['django_crud_generator', 'django_crud_generator.base_django', 'django_crud_generator.base_django.*'],
    scripts=['django_crud_generator/bin/django-crud-generator.py'],
    zip_safe=False,
    include_package_data=True,
)
