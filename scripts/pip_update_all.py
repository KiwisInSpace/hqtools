#!/usr/bin/env

import pip
from subprocess import call
from datetime import datetime

ts = datetime.now().strftime('%Y-%m-%d_%H%M%S')
fn = "pip_freeze_%s.txt" % ts

with open(fn, 'a') as the_file:
    for dist in pip.get_installed_distributions():
        the_file.write("%s==%s\n" % (dist.project_name, dist.version))
        call("pip install --upgrade " + dist.project_name, shell=True)
        print "==> Upgraded", dist.project_name
