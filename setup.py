from setuptools import find_packages,setup
from typing import List

editable_mode='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the list of requirements

    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","") for req in requirements]
        '''
        We are removing the newline comment from the 
        requirements while reading
        '''
    if editable_mode in requirements:
        requirements.remove(editable_mode)

    return requirements

setup(
    name='FirstMlProject',
    version='0.0.1',
    author="Magesh",
    author_email="mageshvirat017@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)