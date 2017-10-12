#!/usr/bin/env python
"""
Copyright 2015 Brocade Communications Systems, Inc.
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
    http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from clicrud.device.generic import generic
import sys

#command1 = sys.argv[1]
#command2 = sys.argv[2]
#command3 = sys.argv[3]
command1 = "router bgp"
command2 = "neighbor 4.31.141.97 shutdown"
#command3 = "neighbor 2001:2000:3080:617::1 shutdown"
db_as_1 = "10.10.3.95"

# With version 0.3.00, 'b64password' and 'b64enable' also exist as arguments for the below.
# They are decoded and copied to 'password' and 'enable' automatically.

transport = generic(host=db_as_1, username="config", enable="B4nkD4t4",
                    method="telnet", password="br@!wuRst2")

print "==== Disable BGP Peering ===="
if transport.connected:
#   print transport.configure([command2,command3])
    print transport.configure([command1,command2])

print "\r\n==== Show Verification ===="
# Return_type can either be a string or list. One is better for scripts,
# the other better for automation perhaps!
if transport.connected:
    print transport.read("show ip bgp summary | b Address", return_type="string")

# print transport.protocol
# print transport.connected
if transport.connected:
    transport.close()
