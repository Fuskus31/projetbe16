from setuptools import setup, find_packages

setup(
    name='Projet de BE 16 SPA',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'cx_Freeze==7.0.0rc0',
        'numpy==1.26.4',
        'pandas==2.2.2',
        'python-dateutil==2.9.0.post0',
        'pytz==2024.1',
        'scipy==1.13.0',
        'six==1.16.0',
        'typing_extensions==4.11.0',
        'tzdata==2024.1',
    ],
    author='Par kevin',
    author_email='nomaildontcontacthismail@email.com',
    description='Allocation student',
    url='URL de votre projet',
)