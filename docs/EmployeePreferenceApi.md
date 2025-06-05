# qualer_sdk.EmployeePreferenceApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete**](EmployeePreferenceApi.md#delete) | **DELETE** /api/user/preferences/{elementPage} | 
[**get**](EmployeePreferenceApi.md#get) | **GET** /api/user/preferences/{elementPage} | 


# **delete**
> object delete(element_page)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeePreferenceApi()
element_page = 'element_page_example' # str | 

try:
    api_response = api_instance.delete(element_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeePreferenceApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **element_page** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> list[QualerApiModelsAssetToEmployeePreferenceResponseModel] get(element_page)



elementPage:  AssetManager = 1,  WorkOrders = 2,  ServiceOrderItems = 3,  ServiceSchedules = 4,  ServiceRequests = 5,  Vendors = 6,  VendorAgreements = 7,  ClientAgreements = 8,  WorkCalendar = 9,  Clients = 10,  GlobalAssetManager = 11,  InvoicesManager = 12,  ProductManager = 13,  ProductSpecifications = 14,  DocumentManager = 15

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeePreferenceApi()
element_page = 'element_page_example' # str | 

try:
    api_response = api_instance.get(element_page)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeePreferenceApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **element_page** | **str**|  | 

### Return type

[**list[QualerApiModelsAssetToEmployeePreferenceResponseModel]**](QualerApiModelsAssetToEmployeePreferenceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

