from setuptools import setup, find_packages

setup(
    name="termmux-cli",
    version="1.0.0",
    description="TermMux-CLI - 轻量级终端多路复用与AI Agent感知管理器",
    long_description=open("README.md", "r", encoding="utf-8").read() if os.path.exists("README.md") else "",
    long_description_content_type="text/markdown",
    author="gitstq",
    author_email="gitstq@example.com",
    url="https://github.com/gitstq/TermMux-CLI",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "rich>=13.0.0",
        "psutil>=5.9.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "termmux=termmux-cli:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Software Development :: Build Tools",
        "Topic :: Terminals",
    ],
    python_requires=">=3.8",
)

import os
