import requests

from woniuboss4_API.tools.service import Service


class Enterprise:

    def __init__(self):
        self.session=Service.get_session()
    def do_enterprise(self,enterprise_url):
        return self.session.get(enterprise_url)
    def query_enterprise(self,enterprise_url,ent_data,udata):
        return self.session.post(enterprise_url,ent_data,params=udata)