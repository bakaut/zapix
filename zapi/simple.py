#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

statusL Done
date: 12-11-2019
update: 12-11-2019
author: Nikolay Lebedev

Description:

Get zabbix hosts

"""
from zabbix_api import *

url = "https://zbx3.ru/zabbix/api_jsonrpc.php"
username = "Admin"
password = "zabbix"

api = zapi(user=username,password=password,url=url)


get_host = api.request(method="host.get",
                        params={ "output": ["status","error","name","proxy_hostid"], "filter": {"status": 0, "flags": 0}, "limit": 10},
                        action_string="Get all active hosts from z3")


print get_host['result']

api.logout()