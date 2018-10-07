from netaddr import *
import pprint
i=str(input("enter ip:"))
ip =IPNetwork(i)
print("ip.cidr=%s" % ip.cidr)
print("ip.first.ip=%s" %ip[0])
print("ip.last.ip=%s" %ip[-1])
