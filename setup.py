import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="sicaptcha",
    version="0.0.5",
    author="siteisleri.com",
    author_email="noreply@siteisleri.com",
    description="Python basic captcha module",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/siteisleri/sicaptcha",
    project_urls={
        "Bug Tracker": "https://github.com/siteisleri/sicaptcha/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=["Pillow","uuid"],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.6",
)