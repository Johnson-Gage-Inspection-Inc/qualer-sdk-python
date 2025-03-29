# swagger_client.ClientAssetAttributesApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_asset_attributes_get_asset_attributes**](ClientAssetAttributesApi.md#client_asset_attributes_get_asset_attributes) | **GET** /api/service/clients/assets/{assetId}/attributes | 
[**client_asset_attributes_upsert_asset_attributes**](ClientAssetAttributesApi.md#client_asset_attributes_upsert_asset_attributes) | **PUT** /api/service/clients/assets/{assetId}/attributes | 

# **client_asset_attributes_get_asset_attributes**
> list[QualerApiModelsAssetAttributesToAssetAttributesResponse] client_asset_attributes_get_asset_attributes(asset_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientAssetAttributesApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.client_asset_attributes_get_asset_attributes(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetAttributesApi->client_asset_attributes_get_asset_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**list[QualerApiModelsAssetAttributesToAssetAttributesResponse]**](QualerApiModelsAssetAttributesToAssetAttributesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_asset_attributes_upsert_asset_attributes**
> object client_asset_attributes_upsert_asset_attributes(body, asset_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientAssetAttributesApi()
body = [swagger_client.QualerApiModelsCommonFromAttributeModel()] # list[QualerApiModelsCommonFromAttributeModel] | 
asset_id = 56 # int | 

try:
    api_response = api_instance.client_asset_attributes_upsert_asset_attributes(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetAttributesApi->client_asset_attributes_upsert_asset_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[QualerApiModelsCommonFromAttributeModel]**](QualerApiModelsCommonFromAttributeModel.md)|  | 
 **asset_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

