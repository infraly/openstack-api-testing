#!/usr/bin/env python3

import openstack
from timeit import default_timer as timer

conn = openstack.connect(cloud="openstack")

print("OpenStack API performance testing on {}".format(conn.auth["auth_url"]))
print()


def timing(name):
    global start
    print("{}:\t{:.3f} s".format(name, timer() - start))


start = timer()
conn.auth_token
timing("Keystone token issue")

start = timer()
list(conn.compute.servers())
timing("Nova server list")

start = timer()
list(conn.image.images())
timing("Glance image list")

start = timer()
list(conn.network.networks())
timing("Network network list")
