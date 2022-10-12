from distutils.core import setup


long_description1 = """
                      This package can be used to classify associates on their performance of total fulfiled and total unfulfiled with
                      two different groups.

                      In easy words let's say we want to see performance (good and bad) salesman for urban market, 
                      rural market, and here we can use this package by passing a dataframe, column name of salesman id, 
                      column name of saleflag (indicating 0 for unsold and 1 for sold), column name of grouping column 
                      (having only two unique values or levels).
                      
                      By default,
                      by calling the result() method after creating object we can get the Top 30 percentage and Bottom 30 percentage salesman.

                      We can change this top and bottom percentage by passing argument (e.g. n=20) inside this result() method.
                      By default this percentage is set to 30%, i.e. n=30 is default argument.


                      
                      You can get the description by reading the README.md file from my github.
                      link of github:

                      https://github.com/bhargabganguli/business_brio.git

                      In that link you can find 

                      - how to install

                      - how to create object and use the method

                      - how to call the method and print the output
                    """

setup(name='business_brio',
      packages = ['business_brio'],
      version='0.0.4',
      description='A very much helpful package to see performance rankings',
      long_description= long_description1,
      url='https://github.com/bhargabganguli/business_brio.git',
      download_url = 'https://github.com/bhargabganguli/business_brio/archive/0.0.4.tar.gz', #FILL IN LATER
      author='Bhargab',
      author_email='bhargab.ganguli@gmail.com',
      keywords = ['chi_test',],
      license='MIT', #YOUR LICENSE HERE!

      install_requires=['pandas','numpy','scipy',],  #YOUR DEPENDENCIES HERE
  

      classifiers=[
        'Development Status :: 3 - Alpha',      # "3 - Alpha", "4 - Beta" or "5 - Production/Stable"
        'Intended Audience :: Developers',      
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License', # Your License Here  
        'Programming Language :: Python :: 3',    # List Python versions that you support Here  
        'Programming Language :: Python :: 3.4',
        ],
)