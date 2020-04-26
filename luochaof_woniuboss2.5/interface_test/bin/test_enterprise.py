import unittest
from woniuboss2.interface_test.lib.enterprise import Enterprise
from woniuboss2.interface_test.tools.utility import Utility


class EnterpriseTest(unittest.TestCase):

    def setUp(self) -> None:
        self.enterprise=Enterprise()
        self.data_config_info=Utility.get_json('..\\conf\\testdata.conf')
    def test_enterprise_add(self):
        ent_url_list=Utility.get_excel_to_dict(self.data_config_info[3])
        for info in ent_url_list:
            url=info['URL']
            content=info['CONTENT']
            resp=self.enterprise.do_enterprise(url).text

            self.assertEqual(resp,content)


    def test_enterprise_update(self):
        ent_url_list = Utility.get_excel_to_dict(self.data_config_info[4])
        for info in ent_url_list:
            url = info['URL']
            content = info['CONTENT']
            resp = self.enterprise.do_enterprise(url).text

            self.assertEqual(resp, content)

    def test_enterprise_query(self):
        enterprise_info=Utility.get_excel_to_dict(self.data_config_info[5])

        for info in enterprise_info:
            url=info['URL']
            data=info['DATA']
            print(url,data)
            body_data={'pageSize':data['pageSize'],'pageIndex':data['pageIndex']}
            body_para={'companyName':data['companyName']}
            resp=self.enterprise.query_enterprise(url,body_data,body_para).json()

            flag=self.assertEqual(resp,info['CONTENT'])
            if flag:
                print('enterprise_query test ok')
            else:
                print('enterprise_query test fail')



    def tearDown(self) -> None:
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)