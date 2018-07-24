#!/usr/bin/env python

import hashlib

PASSWORD = b"blockchainclass"

m = hashlib.sha256()
m.update(PASSWORD)
print m.hexdigest()
