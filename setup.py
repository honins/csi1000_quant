from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

with open("requirements.txt", "r", encoding="utf-8") as fh:
    requirements = [line.strip() for line in fh if line.strip() and not line.startswith("#")]

setup(
    name="csi1000-quant",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="中证1000指数相对低点识别量化系统",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/csi1000-quant",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require={
        "dev": ["pytest>=6.2.0", "black>=21.0.0", "flake8>=3.9.0"],
        "deep": ["tensorflow>=2.6.0"],
        "torch": ["torch>=1.9.0"],
    },
)

