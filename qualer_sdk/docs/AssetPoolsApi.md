# swagger_client.AssetPoolsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_pools_get**](AssetPoolsApi.md#asset_pools_get) | **GET** /api/assetpools/{id} | 
[**asset_pools_get_all**](AssetPoolsApi.md#asset_pools_get_all) | **GET** /api/assetpools | 


# **asset_pools_get**
> QualerApiModelsAssetPoolsToAssetPoolModel asset_pools_get(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetPoolsApi()
id = 56 # int | 

try:
    api_response = api_instance.asset_pools_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetPoolsApi->asset_pools_get: %s\n" % e)
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

# **asset_pools_get_all**
> list[QualerApiModelsAssetPoolsToAssetPoolModel] asset_pools_get_all()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetPoolsApi()

try:
    api_response = api_instance.asset_pools_get_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetPoolsApi->asset_pools_get_all: %s\n" % e)
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

