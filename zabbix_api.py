# -*- coding: utf-8 -*-

"""
Zabbix api wrapper

"""
import os
import requests
import json
import sys
import random
import logging

class zapi(object):
    def login(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url

        data_auth = {
            "jsonrpc": "2.0",
            "method": "user.login",
            "params": {
                "user": self.username,
                "password": self.password
            },
            "id": 1
        }

        answer_auth = requests.post(url=self.url, json=data_auth)
        pretty_auth = answer_auth.json()
        return pretty_auth['result']

    def request(self, method, params, auth_token, url, action_string):
        global answer, pretty
        self.method = method
        self.params = params
        self.auth_token = auth_token
        self.url = url
        self.action_string = action_string

        ids = int(random.random() * 100)
        data = {"jsonrpc": "2.0", "method": method, "params": params,
                "auth": auth_token,"id": ids}
        try:
            answer = requests.post(url=url, json=data)
        except Exception, e:
            error_str = action_string + ". Error. Wrong request " + str(e)
            logging.warning(error_str)

        if answer.status_code == 200:
            pretty = answer.json()
            if "result" in answer.json():
                error_str = action_string + " Success"
                logging.debug(error_str)
                return pretty
            else:
                error_str = action_string + ". Error in request responce " + pretty['error']['data']
                if "already" in pretty['error']['data']:
                    logging.info(error_str)
                else:
                    logging.warning(error_str)
        else:
            error_str = action_string + ". Error. Wrong request " + str(answer.status_code)
            logging.warning(error_str)
