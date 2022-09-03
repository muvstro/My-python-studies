import pytest
import logging

logging.basicConfig(level=logging.DEBUG)
TEST_LOG_NAME = 'my-even-logger'

@pytest.fixture
def log():
    return logging.getLogger(TEST_LOG_NAME)
