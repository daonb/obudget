# -*- coding: iso-8859-15 -*-
"""first_time FunkLoad test

$Id: $
"""
import unittest
from funkload.FunkLoadTestCase import FunkLoadTestCase
from webunit.utility import Upload
from funkload.utils import Data
#from funkload.utils import xmlrpc_get_credential

class FirstTime(FunkLoadTestCase):
    """XXX

    This test use a configuration file FirstTime.conf.
    """

    def setUp(self):
        """Setting up test."""
        self.logd("setUp")
        self.server_url = self.conf_get('main', 'url')
        # XXX here you can setup the credential access like this
        # credential_host = self.conf_get('credential', 'host')
        # credential_port = self.conf_getInt('credential', 'port')
        # self.login, self.password = xmlrpc_get_credential(credential_host,
        #                                                   credential_port,
        # XXX replace with a valid group
        #                                                   'members')

    def test_first_time(self):
        # The description should be set in the configuration file
        server_url = self.server_url
        # begin of test ---------------------------------------------

        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0001.request
        self.setBasicAuth('guest', 'powertothepeople')
        self.get(server_url + "/",
            description="Get /")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0010.request
        self.get(server_url + "/00?depth=0&callback=__gwt_jsonp__.I0.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0012.request
        self.get(server_url + "/00?year=2010&depth=0&callback=__gwt_jsonp__.I1.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0013.request
        self.get(server_url + "/00?year=2010&depth=1&callback=__gwt_jsonp__.I2.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0014.request
        self.get(server_url + "/00?depth=0&callback=__gwt_jsonp__.I3.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0016.request
        self.get(server_url + "/00?text=j&full=1&num=20&distinct=1&callback=__gwt_jsonp__.I4.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0017.request
        self.get(server_url + "/00?text=%D7%97&full=1&num=20&distinct=1&callback=__gwt_jsonp__.I5.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0018.request
        self.get(server_url + "/00?text=%D7%97%D7%A8&full=1&num=20&distinct=1&callback=__gwt_jsonp__.I6.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0019.request
        self.get(server_url + "/00?text=%D7%97%D7%A8%D7%93%D7%99%D7%9D&full=1&num=20&distinct=1&callback=__gwt_jsonp__.I7.onSuccess",
            description="Get /00")
        # /var/folders/Dl/DllYbarwFamPLNFQgI6D0U+++TI/-Tmp-/tmpMAvg2J_funkload/watch0020.request
        self.get(server_url + "/002031?depth=0&text=%D7%AA%D7%A8%D7%91%D7%95%D7%AA,%D7%AA%D7%A8%D7%91%D7%95%D7%AA%20%D7%AA%D7%95%D7%A8%D7%A0%D7%99%D7%AA,%20%20%20%20%D7%A4%D7%A2%D7%95%D7%9C%D7%95%D7%AA%20%D7%AA%D7%A8%D7%91%D7%95%D7%AA%20%20%20%20%20%20%20%20%20%20%20%D7%9C%D7%97%D7%A8%D7%93%D7%99%D7%9D,%D7%A8%D7%A9%D7%95%D7%AA%20%D7%94%D7%A2%D7%AA%D7%99%D7%A7%D7%95%D7%AA%20%20%20%20%D7%95%D7%9E%D7%AA%D7%A0%22%D7%A1%D7%99%D7%9D&callback=__gwt_jsonp__.I8.onSuccess",
            description="Get /002031")

        # end of test -----------------------------------------------

    def tearDown(self):
        """Setting up test."""
        self.logd("tearDown.\n")



if __name__ in ('main', '__main__'):
    unittest.main()
