#!/usr/bin/env python

import os
import hashlib

PASSWORD = os.environ['BLOCKCHAIN_PASSWORD']

m = hashlib.sha256()
m.update(PASSWORD)
print m.hexdigest()
