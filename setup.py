from setuptools import setup, find_packages

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="wagtailmarkdownblock",
    version="0.3.3",
    description="Wagtail Markdown Block provides PrismJS Markdown conversion in Wagtail.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Tim Allen",
    author_email="tallen@wharton.upenn.edu",
    url="https://github.com/FlipperPA/wagtailmarkdownblock",
    include_package_data=True,
    packages=find_packages(),
    zip_safe=False,
    install_requires=[
        "wagtail>=1.8",
        "markdown>=2.5",
        "bleach>=2.0.0",
        "Pygments>=2.3.1",
    ],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Framework :: Django",
        "Framework :: Django :: 2.0",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Topic :: Internet :: WWW/HTTP",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
    ],
)
