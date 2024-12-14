from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    """
    This function will return the list of requirements.
    """
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # Use strip to clean newlines

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)

    return requirements  # Return the list of requirements, not the function itself

setup(
    name='mlproject',
    version='0.0.1',
    author='Himanshu',
    author_email='himanshumore98@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')  # Call the function here
)






setup(
name= 'mlproject',
version='0.0.1',
author= 'Himanshu',
author_email= 'himanshumore98@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)




