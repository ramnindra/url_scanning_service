

import pytest

from urlapp.server import app

@pytest.fixture(scope='module')
def test_client():
    app.testing = True
    return app.test_client()

