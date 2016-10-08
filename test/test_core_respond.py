from core import respond
from nose.tools import assert_true


def test_index_doesnt_crash_without_params():
    resp = respond('index.html', {})
    assert_true('bootstrap' in resp)
