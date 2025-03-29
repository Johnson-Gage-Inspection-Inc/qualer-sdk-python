# swagger_client.ServicePricingApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_pricing_get**](ServicePricingApi.md#service_pricing_get) | **GET** /api/service/pricing | 
[**service_pricing_update**](ServicePricingApi.md#service_pricing_update) | **PUT** /api/service/pricing | 

# **service_pricing_get**
> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse] service_pricing_get(service_pricing_id, service_group_id=service_group_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicePricingApi()
service_pricing_id = 56 # int | 
service_group_id = 56 # int | optional (optional)

try:
    api_response = api_instance.service_pricing_get(service_pricing_id, service_group_id=service_group_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicePricingApi->service_pricing_get: %s\n" % e)
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

# **service_pricing_update**
> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse] service_pricing_update(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicePricingApi()
body = [swagger_client.QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel()] # list[QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel] | 

try:
    api_response = api_instance.service_pricing_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicePricingApi->service_pricing_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel]**](QualerWebMvcAreasApiModelsServicePricesFromServicePriceBulkEditModel.md)|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]**](QualerApiModelsServiceOrdersToServiceOrderTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

