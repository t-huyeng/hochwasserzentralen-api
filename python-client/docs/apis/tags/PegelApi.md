<a name="__pageTop"></a>
# hochwasserzentralen.apis.tags.pegel_api.PegelApi

All URIs are relative to *https://www.hochwasserzentralen.de*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_lage_pegel**](#get_all_lage_pegel) | **get** /webservices/get_lagepegel.php | Lage der Pegel mit Pegelnummern
[**get_pegel_infos_by_pegelnummer**](#get_pegel_infos_by_pegelnummer) | **post** /webservices/get_infospegel.php | Infos zu einem Pegel.

# **get_all_lage_pegel**
<a name="get_all_lage_pegel"></a>
> LagePegel get_all_lage_pegel()

Lage der Pegel mit Pegelnummern

Rückgabe von allen Pegeln und deren Lage.

### Example

```python
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.apis.tags import pegel_api
from deutschland.hochwasserzentralen.model.lage_pegel import LagePegel
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)

# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient(configuration) as api_client:
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

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_all_lage_pegel.ApiResponseFor200) | OK

#### get_all_lage_pegel.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**LagePegel**](../../models/LagePegel.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

# **get_pegel_infos_by_pegelnummer**
<a name="get_pegel_infos_by_pegelnummer"></a>
> InfosPegel get_pegel_infos_by_pegelnummer()

Infos zu einem Pegel.

Rückgabe von Informationen zu einem Pegelbetreiber.

### Example

```python
from deutschland import hochwasserzentralen
from deutschland.hochwasserzentralen.apis.tags import pegel_api
from deutschland.hochwasserzentralen.model.infos_pegel import InfosPegel
from pprint import pprint
# Defining the host is optional and defaults to https://www.hochwasserzentralen.de
# See configuration.py for a list of all supported configuration parameters.
configuration = hochwasserzentralen.Configuration(
    host = "https://www.hochwasserzentralen.de"
)

# Enter a context with an instance of the API client
with hochwasserzentralen.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = pegel_api.PegelApi(api_client)

    # example passing only optional values
    body = dict(
        pgnr="HE_24820206",
    )
    try:
        # Infos zu einem Pegel.
        api_response = api_instance.get_pegel_infos_by_pegelnummer(
            body=body,
        )
        pprint(api_response)
    except hochwasserzentralen.ApiException as e:
        print("Exception when calling PegelApi->get_pegel_infos_by_pegelnummer: %s\n" % e)
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
**pgnr** | str,  | str,  | Pegelnummer | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

### Return Types, Responses

Code | Class | Description
------------- | ------------- | -------------
n/a | api_client.ApiResponseWithoutDeserialization | When skip_deserialization is True this response is returned
200 | [ApiResponseFor200](#get_pegel_infos_by_pegelnummer.ApiResponseFor200) | OK

#### get_pegel_infos_by_pegelnummer.ApiResponseFor200
Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
response | urllib3.HTTPResponse | Raw response |
body | typing.Union[SchemaFor200ResponseBodyTextHtml, ] |  |
headers | Unset | headers were not defined |

# SchemaFor200ResponseBodyTextHtml
Type | Description  | Notes
------------- | ------------- | -------------
[**InfosPegel**](../../models/InfosPegel.md) |  | 


### Authorization

No authorization required

[[Back to top]](#__pageTop) [[Back to API list]](../../../README.md#documentation-for-api-endpoints) [[Back to Model list]](../../../README.md#documentation-for-models) [[Back to README]](../../../README.md)

