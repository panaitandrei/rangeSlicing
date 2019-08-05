import setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(
     name='rangeSlicing',
     version='0.1.3',
     scripts=['rangeSlicing'] ,
     author="Andrei Panait",
     author_email="pnt_andrei@yahoo.com",
     description="A range splitting package to divide a longer range in smaller batches.",
     long_description=open("README.md").read(),
     long_description_content_type="text/markdown",
     url="https://github.com/panaitandrei/rangeSlicing",
     packages=setuptools.find_packages(),
     py_modules=['rangeSlicing'],
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: Apache Software License",
         "Operating System :: OS Independent",
     ],
 )
