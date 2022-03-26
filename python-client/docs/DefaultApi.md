# hochwasserzentralen.DefaultApi

All URIs are relative to *https://www.hochwasserzentralen.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vhosts_geojson_bundesland_version_geojson_get**](DefaultApi.md#vhosts_geojson_bundesland_version_geojson_get) | **GET** /vhosts/geojson/bundesland.{version}.geojson | Geojson der Bundesländer
[**webservices_get_infosbundesland_php_post**](DefaultApi.md#webservices_get_infosbundesland_php_post) | **POST** /webservices/get_infosbundesland.php | Infos zu einem Bundesland.
[**webservices_get_infospegel_php_post**](DefaultApi.md#webservices_get_infospegel_php_post) | **POST** /webservices/get_infospegel.php | Infos zu einem Pegel.
[**webservices_get_lagepegel_php_get**](DefaultApi.md#webservices_get_lagepegel_php_get) | **GET** /webservices/get_lagepegel.php | Lage der Pegel mit Pegelnummern


# **vhosts_geojson_bundesland_version_geojson_get**
> str vhosts_geojson_bundesland_version_geojson_get(version)

Geojson der Bundesländer

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    version = "20211130" # str | 

    # example passing only required values which don't have defaults set
    try:
        # Geojson der Bundesländer
        api_response = api_instance.vhosts_geojson_bundesland_version_geojson_get(version)
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling DefaultApi->vhosts_geojson_bundesland_version_geojson_get: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**|  |

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webservices_get_infosbundesland_php_post**
> str webservices_get_infosbundesland_php_post()

Infos zu einem Bundesland.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    id = "HE" # str | Bundeslandkürzel (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Infos zu einem Bundesland.
        api_response = api_instance.webservices_get_infosbundesland_php_post(id=id)
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling DefaultApi->webservices_get_infosbundesland_php_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Bundeslandkürzel | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webservices_get_infospegel_php_post**
> str webservices_get_infospegel_php_post()

Infos zu einem Pegel.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import default_api
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)
    pgnr = "HE_24820206" # str | Pegelnummer (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Infos zu einem Pegel.
        api_response = api_instance.webservices_get_infospegel_php_post(pgnr=pgnr)
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling DefaultApi->webservices_get_infospegel_php_post: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pgnr** | **str**| Pegelnummer | [optional]

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webservices_get_lagepegel_php_get**
> LagePegel webservices_get_lagepegel_php_get()

Lage der Pegel mit Pegelnummern

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import default_api
from deutschland.hochwasserzentralen.model.lage_pegel import LagePegel
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = default_api.DefaultApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lage der Pegel mit Pegelnummern
        api_response = api_instance.webservices_get_lagepegel_php_get()
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling DefaultApi->webservices_get_lagepegel_php_get: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LagePegel**](LagePegel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

