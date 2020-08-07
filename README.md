a cool package w/ some DS helper functions

dependencies: scikit-learn numpy pandas python 3.8

to install package: 'pip install -i https://test.pypi.org/simple/ alienell-saiyan'

url for the package: 'https://test.pypi.org/project/alienell-saiyan/'

to upload to pypi: pipenv install -d twine

to make a new version: delete the current build and dist files ,then revise version value in setup.py file

then type this:

python setup.py sdist bdist_wheel and this twine upload --repository-url https://test.pypi.org/legacy/ dist/* OR twine upload --skip-existing --repository-url https://test.pypi.org/legacy/ dist/*



