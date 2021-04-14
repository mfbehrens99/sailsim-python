workon pypi-upload
python setup.py sdist bdist_wheel
twine upload dist/*
pause
