from setuptools import find_packages, setup
from typing import List

hype = '-e .'
def get_requirements(file_path:str)->List[str]:
  """
  this returns the list of requirements
  """

  requirements = []
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    [req.replace("\n","") for req in requirements]
 
    if hype in requirements:
      requirements.remove(hype)
  
  return requirements

setup(
name='Data-Science-Project',
version='0.0.1',
author='Purav',
author_email='puravjrpatel@gmail.com',
packages = find_packages(),
install_requires = get_requirements('requirements.txt')
)