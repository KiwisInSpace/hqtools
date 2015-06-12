#!/usr/bin/env

import pip
from subprocess import call
from datetime import datetime

ts = datetime.now().strftime('%Y-%m-%d_%H%M%S')
fn = "pip_freeze_%s.txt" % ts
dn = "C:\\vol\\cache\\pypi"

with open(fn, 'a') as the_file:
    for dist in pip.get_installed_distributions():
        the_file.write("%s==%s\n" % (dist.project_name, dist.version))
        # call("pip install --download %s %s" % (dn, dist.project_name), shell=True)
        call("pip install --upgrade " + dist.project_name, shell=True)
        print "==> Upgraded", dist.project_name
