# qualer_sdk.AssetPoolsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](AssetPoolsApi.md#get) | **GET** /api/assetpools/{id} | 
[**get_all**](AssetPoolsApi.md#get_all) | **GET** /api/assetpools | 


# **get**
> QualerApiModelsAssetPoolsToAssetPoolModel get(id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetPoolsApi()
id = 56 # int | 

try:
    api_response = api_instance.get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetPoolsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QualerApiModelsAssetPoolsToAssetPoolModel**](QualerApiModelsAssetPoolsToAssetPoolModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[QualerApiModelsAssetPoolsToAssetPoolModel] get_all()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetPoolsApi()

try:
    api_response = api_instance.get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetPoolsApi->get_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsAssetPoolsToAssetPoolModel]**](QualerApiModelsAssetPoolsToAssetPoolModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

