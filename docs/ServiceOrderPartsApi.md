# qualer_sdk.ServiceOrderPartsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_work_order_parts**](ServiceOrderPartsApi.md#create_work_order_parts) | **POST** /api/service/workorders/{serviceOrderId}/parts | 
[**delete_work_order_task**](ServiceOrderPartsApi.md#delete_work_order_task) | **DELETE** /api/service/workorders/{serviceOrderId}/parts/{serviceOrderItemPartId} | 
[**get_work_order_parts**](ServiceOrderPartsApi.md#get_work_order_parts) | **GET** /api/service/workorders/{serviceOrderId}/parts | 
[**update_work_order_parts**](ServiceOrderPartsApi.md#update_work_order_parts) | **PUT** /api/service/workorders/{serviceOrderId}/parts | 


# **create_work_order_parts**
> object create_work_order_parts(service_order_id, model)



ServiceOrderChargeType: Part, Labor, Charge

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderPartsApi()
service_order_id = 56 # int | 
model = qualer_sdk.QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel() # QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel | 

try:
    api_response = api_instance.create_work_order_parts(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->create_work_order_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel**](QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_order_task**
> object delete_work_order_task(service_order_id, service_order_item_part_id)





### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderPartsApi()
service_order_id = 56 # int | 
service_order_item_part_id = 56 # int | 

try:
    api_response = api_instance.delete_work_order_task(service_order_id, service_order_item_part_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->delete_work_order_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **service_order_item_part_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_order_parts**
> list[QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse] get_work_order_parts(service_order_id)





### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderPartsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_work_order_parts(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->get_work_order_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse]**](QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_work_order_parts**
> object update_work_order_parts(service_order_id, model)



ServiceOrderChargeType: Part, Labor, Charge

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderPartsApi()
service_order_id = 56 # int | 
model = qualer_sdk.QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel() # QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel | 

try:
    api_response = api_instance.update_work_order_parts(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->update_work_order_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel**](QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

