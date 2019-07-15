#!/bin/bash

# enter anaconda virtual env
source activate jupyter

# run jupyter notebook on background
nohup jupyter notebook & 1> /dev/null 2> /var/log/jupyter/error.log



# jupyter config (~/.jupyter/jupyter_notebook_config.py)
import os
from IPython.lib import passwd

c.NotebookApp.ip = '0.0.0.0'
c.NotebookApp.port = 8888
c.NotebookApp.open_browser = False

c.NotebookApp.password = ''
c.NotebookApp.token = ''
