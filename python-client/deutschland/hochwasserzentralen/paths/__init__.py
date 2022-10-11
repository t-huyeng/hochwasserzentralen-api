# do not import all endpoints into this module because that uses a lot of memory and stack frames
# if you need the ability to import all endpoints from this module, import them with
# from deutschland.hochwasserzentralen.apis.path_to_api import path_to_api

import enum


class PathValues(str, enum.Enum):
    WEBSERVICES_GET_INFOSPEGEL_PHP = "/webservices/get_infospegel.php"
    WEBSERVICES_GET_INFOSBUNDESLAND_PHP = "/webservices/get_infosbundesland.php"
    WEBSERVICES_GET_LAGEPEGEL_PHP = "/webservices/get_lagepegel.php"
    VHOSTS_GEOJSON_BUNDESLAND_VERSION_GEOJSON = (
        "/vhosts/geojson/bundesland.{version}.geojson"
    )
