from setuptools import setup, find_namespace_packages

setup(name='clean_folder',
      version='1',
      description='Sorting files in folder',
      url='https://github.com/OleksaSolo/Homework07',
      author='Oleksa Sol',
      author_email='9095945s@gmail.com',
      license='UA',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']}
)