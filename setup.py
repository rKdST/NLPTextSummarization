import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()


__version__ = "0.0.0"

REPO_NAME = "NLPTextSummarization"
AUTHOR_USER_NAME = "rKdST"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "10r.kulkarni@gmail.com"


#the below mentioned will look for the constructor file(__init__.py) in every folder and install it.
setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="NLP pakage using pyton",
    long_description=long_description,
    long_description_content="text/markdowm",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")

)