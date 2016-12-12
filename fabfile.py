from fabric.api import *

def notebook():
    with lcd("notebook"):
        local("jupyter notebook --ip=\"0.0.0.0\"")
