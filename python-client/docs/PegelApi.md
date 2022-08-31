# hochwasserzentralen.PegelApi

All URIs are relative to *https://www.hochwasserzentralen.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_lage_pegel**](PegelApi.md#get_all_lage_pegel) | **GET** /webservices/get_lagepegel.php | Lage der Pegel mit Pegelnummern
[**get_pegel_infos_by_pegelnummer**](PegelApi.md#get_pegel_infos_by_pegelnummer) | **POST** /webservices/get_infospegel.php | Infos zu einem Pegel.


# **get_all_lage_pegel**
> LagePegel get_all_lage_pegel()

Lage der Pegel mit Pegelnummern

Rückgabe von allen Pegeln und deren Lage.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import pegel_api
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
    api_instance = pegel_api.PegelApi(api_client)

    # example, this endpoint has no required or optional parameters
    try:
        # Lage der Pegel mit Pegelnummern
        api_response = api_instance.get_all_lage_pegel()
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling PegelApi->get_all_lage_pegel: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**LagePegel**](LagePegel.md)

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

# **get_pegel_infos_by_pegelnummer**
> InfosPegel get_pegel_infos_by_pegelnummer()

Infos zu einem Pegel.

Rückgabe von Informationen zu einem Pegelbetreiber.

### Example


```python
import time
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.api import pegel_api
from deutschland.hochwasserzentralen.model.infos_pegel import InfosPegel
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)


# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = pegel_api.PegelApi(api_client)
    pgnr = "HE_24820206" # str | Pegelnummer (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        # Infos zu einem Pegel.
        api_response = api_instance.get_pegel_infos_by_pegelnummer(pgnr=pgnr)
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling PegelApi->get_pegel_infos_by_pegelnummer: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pgnr** | **str**| Pegelnummer | [optional]

### Return type

[**InfosPegel**](InfosPegel.md)

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

