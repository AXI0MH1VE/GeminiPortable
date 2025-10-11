from setuptools import setup, find_packages

setup(
    name="gemini-portable",
    version="0.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "gemini=gemini_portable.cli:main",
        ],
    },
)
