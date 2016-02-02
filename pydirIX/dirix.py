# Copyright 2015 BigWaveIT. All rights reserved.
#
# The contents of this file are licensed under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with the
# License. You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations under
# the License.

import json
import urllib

class dirIX:

    def __init__(self, url):
        """
        Init Euro-IX IXP member list in JSON format
        :param url: url to the json schema source
        """
        self.url = url

    def get(self):
        """
        Import the Euro-IX IXP member list
        """
        response = urllib.urlopen(self.url)
        data = json.loads(response.read())
        self.data = data

    def list(self):
        """
        List members at IXP
        """
        # init result list
        result = []
        # collect data 
        for member in self.data['member_list']:
            result.append(member['name'])
        # return result list
        return result

    def list_asn(self):
        """
        List ASNs at IXP
        """
        # init result list
        result = []
        # collect data 
        for member in self.data['member_list']:
            result.append(member['asnum'])
        # return result list
        return result

    def list_ip(self):
        """
        List IPs at IXP
        """
        # init result list
        result = []
        # collect data 
        for member in self.data['member_list']:
            for connection in member['connection_list']:
                 for vlan in connection['vlan_list']:
                    if 'ipv4' in vlan:
                        result.append(vlan['ipv4']['address'])
        # return result list
        return result

    def list_ipv6(self):
        """
        List IPs at IXP
        """
        # init result list
        result = []
        # collect data 
        for member in self.data['member_list']:
            for connection in member['connection_list']:
                 for vlan in connection['vlan_list']:
                    if 'ipv6' in vlan:
                        result.append(vlan['ipv6']['address'])
        # return result list
        return result

    def list_members_by_asn(self):
        """
        Show member data by ASN
        """
        # init result dict
        result = {}
        # collect data 
        for member in self.data['member_list']:
            asn = member['asnum']
            result[asn] = {}
            result[asn]['name'] = member['name']
            result[asn]['ip'] = []
            result[asn]['ipv6'] = []
            for connection in member['connection_list']:
                 for vlan in connection['vlan_list']:
                    if 'ipv4' in vlan:
                        result[asn]['ip'].append(vlan['ipv4']['address'])
                    if 'ipv6' in vlan:
                        result[asn]['ipv6'].append(vlan['ipv6']['address'])
        # return result dict
        return result

