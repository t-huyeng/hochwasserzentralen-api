import typing_extensions
from deutschland.hochwasserzentralen.apis.paths.vhosts_geojson_bundesland_version_geojson import (
    VhostsGeojsonBundeslandVersionGeojson,
)
from deutschland.hochwasserzentralen.apis.paths.webservices_get_infosbundesland_php import (
    WebservicesGetInfosbundeslandPhp,
)
from deutschland.hochwasserzentralen.apis.paths.webservices_get_infospegel_php import (
    WebservicesGetInfospegelPhp,
)
from deutschland.hochwasserzentralen.apis.paths.webservices_get_lagepegel_php import (
    WebservicesGetLagepegelPhp,
)
from deutschland.hochwasserzentralen.paths import PathValues

PathToApi = typing_extensions.TypedDict(
    "PathToApi",
    {
        PathValues.WEBSERVICES_GET_INFOSPEGEL_PHP: WebservicesGetInfospegelPhp,
        PathValues.WEBSERVICES_GET_INFOSBUNDESLAND_PHP: WebservicesGetInfosbundeslandPhp,
        PathValues.WEBSERVICES_GET_LAGEPEGEL_PHP: WebservicesGetLagepegelPhp,
        PathValues.VHOSTS_GEOJSON_BUNDESLAND_VERSION_GEOJSON: VhostsGeojsonBundeslandVersionGeojson,
    },
)

path_to_api = PathToApi(
    {
        PathValues.WEBSERVICES_GET_INFOSPEGEL_PHP: WebservicesGetInfospegelPhp,
        PathValues.WEBSERVICES_GET_INFOSBUNDESLAND_PHP: WebservicesGetInfosbundeslandPhp,
        PathValues.WEBSERVICES_GET_LAGEPEGEL_PHP: WebservicesGetLagepegelPhp,
        PathValues.VHOSTS_GEOJSON_BUNDESLAND_VERSION_GEOJSON: VhostsGeojsonBundeslandVersionGeojson,
    }
)
