# qualer_sdk.ServicePricingApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get**](ServicePricingApi.md#get) | **GET** /api/service/pricing | 
[**update**](ServicePricingApi.md#update) | **PUT** /api/service/pricing | 


# **get**
> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse] get(service_pricing_id, service_group_id=service_group_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServicePricingApi()
service_pricing_id = 56 # int | 
service_group_id = 56 # int | optional (optional)

try:
    # 
    api_response = api_instance.get(service_pricing_id, service_group_id=service_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicePricingApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_pricing_id** | **int**|  | 
 **service_group_id** | **int**| optional | [optional] 

### Return type

[**list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]**](QualerApiModelsServiceOrdersToServiceOrderTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse] update(models)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServicePricingApi()
models = [qualer_sdk.QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel()] # list[QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel] | 

try:
    api_response = api_instance.update(models)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicePricingApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models** | [**list[QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel]**](QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel.md)|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]**](QualerApiModelsServiceOrdersToServiceOrderTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

