# -*- coding: utf-8 -*-
"""
    consus Tests
    ~~~~~~~~~~~~
    Tests the consus application.
    :copyright: (c) 2017 by Mark Murnane.
    :license: MIT, see LICENSE for more details.
"""

import os
import json
import tempfile
import pytest
import consus

@pytest.fixture
def client(request):
    db_fd, db_file = tempfile.mkstemp()
    consus.app.config['TESTING'] = True
    client = consus.app.test_client()
    with consus.app.app_context():
        consus.app.db.connect('sqlite:///' + db_file)

    def teardown():
        os.close(db_fd)
        os.unlink(db_file)
    request.addfinalizer(teardown)

    return client

def test_file_add(client):
    res = client.get('/files')
    data = json.loads(res.data.decode('UTF-8'))
    assert(data == [])