#!/usr/bin/env python

from twisted.internet import reactor

from beta.factory import AlphaFactory

reactor.listenTCP(25565, AlphaFactory())
reactor.run()
