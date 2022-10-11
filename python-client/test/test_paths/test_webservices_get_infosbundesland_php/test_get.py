# coding: utf-8

"""


    Generated by: https://openapi-generator.tech
"""

import unittest
from unittest.mock import patch

import urllib3
from deutschland.hochwasserzentralen import api_client, configuration, schemas
from deutschland.hochwasserzentralen.paths.webservices_get_infosbundesland_php import (  # noqa: E501
    get,
)

from deutschland import hochwasserzentralen

from .. import ApiTestMixin


class TestWebservicesGetInfosbundeslandPhp(ApiTestMixin, unittest.TestCase):
    """
    WebservicesGetInfosbundeslandPhp unit test stubs
        Infos zu allen Bundesländern und angeschlossen Gebieten.  # noqa: E501
    """

    _configuration = configuration.Configuration()

    def setUp(self):
        used_api_client = api_client.ApiClient(configuration=self._configuration)
        self.api = get.ApiForget(api_client=used_api_client)  # noqa: E501

    def tearDown(self):
        pass

    response_status = 200


if __name__ == "__main__":
    unittest.main()
