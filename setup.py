from setuptools import setup, find_packages

def get_requirements(file_path: str) -> list[str]:
    """
    Reads a requirements.txt file and returns a list of package names.
    Ignores empty lines and comments.
    """
    try:
        with open(file_path, "r") as file_obj:
            requirements = [
                line.strip() for line in file_obj.readlines()
                if line.strip() and not line.startswith("#") and line.strip() != "-e ."
            ]
        return requirements
    except FileNotFoundError:
        print(f"Error: {file_path} not found.")
        return []


setup(  
name='mnist_draw',
version='0.0.1',
author='Ellie Davies',
author_email='ellie.davies33@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)