#!/bin/bash

# Oracle Libs Init
python -c "import os; os.putenv( 'LD_LIBRARY_PATH','/usr/lib/oracle/12.1/client64/lib'); os.system('/var/www/cgi-bin/odbrs/kernel.py')"

