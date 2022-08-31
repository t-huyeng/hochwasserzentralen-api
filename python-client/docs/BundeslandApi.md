# hochwasserzentralen.BundeslandApi

All URIs are relative to *https://www.hochwasserzentralen.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_bundesland_infos**](BundeslandApi.md#get_all_bundesland_infos) | **GET** /webservices/get_infosbundesland.php | Infos zu allen Bundesländern und angeschlossen Gebieten.
[**get_bundesland_geojson**](BundeslandApi.md#get_bundesland_geojson) | **GET** /vhosts/geojson/bundesland.{version}.geojson | Geojson der Bundesländer
[**get_bundesland_infos_by_bundesland**](BundeslandApi.md#get_bundesland_infos_by_bundesland) | **POST** /webservices/get_infosbundesland.php | Infos zu einem Bundesland.


# **get_all_bundesland_infos**
> InfosBundeslaender get_all_bundesland_infos()

Infos zu allen Bundesländern und angeschlossen Gebieten.

Rückgabe von Informationen zu einem Bundesland.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import bundesland_api
from deutschland.hochwasserzentralen.model.infos_bundeslaender import InfosBundeslaender
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
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

### Return type

[**InfosBundeslaender**](InfosBundeslaender.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundesland_geojson**
> BundeslandGeojson get_bundesland_geojson(version)

Geojson der Bundesländer

Rückgabe von Geojson für die Bundesländer und die angeschlossenen Regionen.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import bundesland_api
from deutschland.hochwasserzentralen.model.bundesland_geojson import BundeslandGeojson
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bundesland_api.BundeslandApi(api_client)
    version = "20211130" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Geojson der Bundesländer
        api_response = api_instance.get_bundesland_geojson(version)
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling BundeslandApi->get_bundesland_geojson: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |

### Return type

[**BundeslandGeojson**](BundeslandGeojson.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/geo+json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_bundesland_infos_by_bundesland**
> InfosBundesland get_bundesland_infos_by_bundesland()

Infos zu einem Bundesland.

Rückgabe von Informationen zu einem Bundesland.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import bundesland_api
from deutschland.hochwasserzentralen.model.infos_bundesland import InfosBundesland
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = bundesland_api.BundeslandApi(api_client)
    id = "HE" # str | Bundeslandkürzel (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Infos zu einem Bundesland.
        api_response = api_instance.get_bundesland_infos_by_bundesland(id=id)
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling BundeslandApi->get_bundesland_infos_by_bundesland: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bundeslandkürzel | [optional]

### Return type

[**InfosBundesland**](InfosBundesland.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/html


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

