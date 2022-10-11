<a name="__pageTop"></a>
# hochwasserzentralen.apis.tags.bundesland_api.BundeslandApi

All URIs are relative to *https://www.hochwasserzentralen.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_bundesland_infos**](#get_all_bundesland_infos) | **get** /webservices/get_infosbundesland.php | Infos zu allen Bundesländern und angeschlossen Gebieten.
[**get_bundesland_geojson**](#get_bundesland_geojson) | **get** /vhosts/geojson/bundesland.{version}.geojson | Geojson der Bundesländer
[**get_bundesland_infos_by_bundesland**](#get_bundesland_infos_by_bundesland) | **post** /webservices/get_infosbundesland.php | Infos zu einem Bundesland.

# **get_all_bundesland_infos**
<a name="get_all_bundesland_infos"></a>
> InfosBundeslaender get_all_bundesland_infos()

Infos zu allen Bundesländern und angeschlossen Gebieten.

Rückgabe von Informationen zu einem Bundesland.

### Example

```python
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.apis.tags import bundesland_api
from deutschland.hochwasserzentralen.model.infos_bundeslaender import InfosBundeslaender
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)

# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundesland_api.BundeslandApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Infos zu allen Bundesländern und angeschlossen Gebieten.
        api_response = api_instance.get_all_bundesland_infos()
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling BundeslandApi->get_all_bundesland_infos: %s\n" % e)
```
### Parameters
This endpoint does not need any parameter.

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_bundesland_infos.ApiResponseFor200) | OK

#### get_all_bundesland_infos.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**InfosBundeslaender**](../../models/InfosBundeslaender.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_bundesland_geojson**
<a name="get_bundesland_geojson"></a>
> BundeslandGeojson get_bundesland_geojson(version)

Geojson der Bundesländer

Rückgabe von Geojson für die Bundesländer und die angeschlossenen Regionen.

### Example

```python
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.apis.tags import bundesland_api
from deutschland.hochwasserzentralen.model.bundesland_geojson import BundeslandGeojson
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)

# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundesland_api.BundeslandApi(api_client)

    # example passing only required values which don't have defaults set
    path_params = {
        'version': "20211130",
    }
    try:
        # Geojson der Bundesländer
        api_response = api_instance.get_bundesland_geojson(
            path_params=path_params,
        )
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling BundeslandApi->get_bundesland_geojson: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
path_params | RequestPathParams | |
accept_content_types | typing.Tuple[str] | default is ('application/geo+json', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### path_params
#### RequestPathParams

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
version | VersionSchema | | 

# VersionSchema

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
str,  | str,  |  | 

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bundesland_geojson.ApiResponseFor200) | OK
404 | [ApiResponseFor404](#get_bundesland_geojson.ApiResponseFor404) | Not Found

#### get_bundesland_geojson.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyApplicationGeojson, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyApplicationGeojson
Type | Description  | Notes
------------- | ------------- | -------------
[**BundeslandGeojson**](../../models/BundeslandGeojson.md) |  | 


#### get_bundesland_geojson.ApiResponseFor404
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | Unset | body was not defined |
headers | Unset | headers were not defined |

### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_bundesland_infos_by_bundesland**
<a name="get_bundesland_infos_by_bundesland"></a>
> InfosBundesland get_bundesland_infos_by_bundesland()

Infos zu einem Bundesland.

Rückgabe von Informationen zu einem Bundesland.

### Example

```python
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.apis.tags import bundesland_api
from deutschland.hochwasserzentralen.model.infos_bundesland import InfosBundesland
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)

# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = bundesland_api.BundeslandApi(api_client)

    # example passing only optional values
    body = dict(
        id="HE",
    )
    try:
        # Infos zu einem Bundesland.
        api_response = api_instance.get_bundesland_infos_by_bundesland(
            body=body,
        )
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling BundeslandApi->get_bundesland_infos_by_bundesland: %s\n" % e)
```
### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
body | typing.Union[SchemaForRequestBodyApplicationXWwwFormUrlencoded, Unset] | optional, default is unset |
content_type | str | optional, default is 'application/x-www-form-urlencoded' | Selects the schema and serialization of the request body
accept_content_types | typing.Tuple[str] | default is ('text/html', ) | Tells the server the content type(s) that are accepted by the client
stream | bool | default is False | if True then the response.content will be streamed and loaded from a file like object. When downloading a file, set this to True to force the code to deserialize the content to a FileSchema file
timeout | typing.Optional[typing.Union[int, typing.Tuple]] | default is None | the timeout used by the rest client
skip_deserialization | bool | default is False | when True, headers and body will be unset and an instance of api_client.ApiResponseWithoutDeserialization will be returned

### body

# SchemaForRequestBodyApplicationXWwwFormUrlencoded

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**id** | str,  | str,  | Bundeslandkürzel | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_bundesland_infos_by_bundesland.ApiResponseFor200) | OK

#### get_bundesland_infos_by_bundesland.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**InfosBundesland**](../../models/InfosBundesland.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

