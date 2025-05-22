# qualer_sdk.ServiceOrderItemPartsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_work_item_parts**](ServiceOrderItemPartsApi.md#get_work_item_parts) | **GET** /api/service/workitems/{workItemId}/parts | 


# **get_work_item_parts**
> list[QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel] get_work_item_parts(work_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemPartsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.get_work_item_parts(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemPartsApi->get_work_item_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel]**](QualerApiModelsServiceOrderItemPartsToOrderItemPartResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

