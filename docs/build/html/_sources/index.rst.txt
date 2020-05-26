.. spectRRa documentation master file, created by
   sphinx-quickstart on Fri Apr 24 11:55:57 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Software Documentation
*************************************


Configuration of Project Environment
=====================================

Developing a Developer tool/GUI for performing spectral analysis.

Overview on How to Run this project
===================================
1. Either install a Python IDE or create a Python virtual environment to install the packages required
2. Install packages required

Setup procedure
================
1. Create a Python Virtual Environment
    - Install virtualenv::

        pip install virtualenv

    - Create virtialenv::

        virtualenv -p python3 <name of virtualenv>
        or
        conda create -n yourenvname python=x.x anaconda

    - Activate virtualenv::

    	source <name of virtualenv>/bin/activate


    - Install requirements::

        pip install -r requirements.txt

2. Install Sphinx and Rinotype
    - Install via cmd::

      	pip install Sphinx
      	pip install rinohtype

    - Setup Sphinx::

    	  sphinx-quickstart

    - Open source/conf.py::
    	  Configure path to root directory. The path should point to the root directory of the project and looking at the project structure, from conf.py we should reach the root by going up two parent directories

    - Create the final document
        make html/confluence


CODE DOCUMENTATION
====================================

.. toctree::
   :hidden:

   index


1. LOAD DATA
=============

interpolate
=====================
.. automodule:: interpolate
   :members:

2. PREPROCESSING
=================

featureSelection
=====================
.. automodule:: featureSelection
   :members:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
