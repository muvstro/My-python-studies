import pytest
import pexpect
import pytest
import sys
from time import sleep

TIMEOUT = 1

@pytest.mark.parametrize("login,password,password2", [("login", "valid_password", "valid_password")])
def test_account(login, password, password2):
    child = pexpect.spawn('python ./account.py')
    child.logfile = sys.stdout.buffer
    while True:
        i = child.expect(['.*username.*', '.*again.*', '.*password'], timeout=TIMEOUT)
        if i==0:
            child.sendline(login)
            sleep(0.1)
        elif i==1:
            child.sendline(password2)
            sleep(0.1)
            break
        elif i==2:
            child.sendline(password)
            sleep(0.1)
        elif i==3:
            child.sendline(password)
            sleep(0.1)
            break
