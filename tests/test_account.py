import pytest
import pexpect
import pytest
import logging
import sys

TIMEOUT = 1
logging.basicConfig(level=logging.DEBUG)
log = logging.getLogger('my-even-logger')

@pytest.mark.parametrize("login,password,password2", [("login", "valid_password", "valid_password")])
def test_account(login, password, password2):
    child = pexpect.spawn('python ./account.py')
    child.logfile = sys.stdout.buffer
    while True:
        i = child.expect(['.*username.*', '.*again.*', '.*password'], timeout=TIMEOUT)
        if i==0:
            child.sendline(login)
        elif i==1:
            child.sendline(password2)
            break
        elif i==2:
            child.sendline(password)
        elif i==3:
            child.sendline(password)
            break
