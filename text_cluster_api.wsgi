#! /usr/bin/python

import sys
#Folder where save application files 
sys.path.insert(0, "/var/www/text_cluster_api")
sys.path.insert(0,'/opt/conda/lib/python3.6/site-packages')
sys.path.insert(0, "/opt/conda/bin/")

import os
os.environ['PYTHONPATH'] = '/opt/conda/bin/python'

from text_cluster_api import app as application