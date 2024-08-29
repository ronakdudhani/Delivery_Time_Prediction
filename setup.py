import setuptools
from typing import List

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

__version__ = "0.0.1"
NAME = "Delivery-Time-Prediction"
REPONAME = "Delivery_Time_Prediction"
AUTHOR = "Ronak Agrawal"
AUTHOR_EMAIL = "ronakdudhani@gmail.com"
AUTHOR_USER_NAME = "ronakdudhani"
REQUIREMENTS_FILE_NAME = "requirements.txt"


HYPHEN_E_DOT = "-e ."
# Requriments.txt file open
# read
# \n ""


def get_requirements_list() -> List[str]:
    with open(REQUIREMENTS_FILE_NAME, encoding="utf-8") as requriment_file:
        requriment_list = requriment_file.readlines()
        requriment_list = [
            requriment_name.replace("\n", "") for requriment_name in requriment_list
        ]

        if HYPHEN_E_DOT in requriment_list:
            requriment_list.remove(HYPHEN_E_DOT)

        return requriment_list


setuptools.setup(
    name=REPONAME,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A end to end machine learning project to predict Delivery Times.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),  # comma added here
    install_requries=get_requirements_list(),
)
