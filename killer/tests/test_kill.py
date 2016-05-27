import pytest

import killer.kill as kk

class TestBasic(object):

    def test_spray(self):
        kk.spray()

    def test_shoot(self):
        kk.shoot()

def test_kick(thing):
    kk.kick(thing)

def test_kick(thing):
    kk.throw(thing)