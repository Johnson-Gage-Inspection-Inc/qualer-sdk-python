# qualer_sdk.AssetAttributesApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_attributes**](AssetAttributesApi.md#get_asset_attributes) | **GET** /api/assets/{assetId}/attributes | 
[**upsert_asset_attributes**](AssetAttributesApi.md#upsert_asset_attributes) | **PUT** /api/assets/{assetId}/attributes | 


# **get_asset_attributes**
> list[AssetAttributesToAssetAttributesResponse] get_asset_attributes(asset_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetAttributesApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.get_asset_attributes(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAttributesApi->get_asset_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**list[AssetAttributesToAssetAttributesResponse]**](AssetAttributesToAssetAttributesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert_asset_attributes**
> object upsert_asset_attributes(asset_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetAttributesApi()
asset_id = 56 # int | 
model = [qualer_sdk.CommonFromAttributeModel()] # list[CommonFromAttributeModel] | 

try:
    api_response = api_instance.upsert_asset_attributes(asset_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetAttributesApi->upsert_asset_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **model** | [**list[CommonFromAttributeModel]**](CommonFromAttributeModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

