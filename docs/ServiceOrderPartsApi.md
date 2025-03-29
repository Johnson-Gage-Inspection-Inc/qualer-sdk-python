# swagger_client.ServiceOrderPartsApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_parts_create_work_order_parts**](ServiceOrderPartsApi.md#service_order_parts_create_work_order_parts) | **POST** /api/service/workorders/{serviceOrderId}/parts | 
[**service_order_parts_delete_work_order_task**](ServiceOrderPartsApi.md#service_order_parts_delete_work_order_task) | **DELETE** /api/service/workorders/{serviceOrderId}/parts/{serviceOrderItemPartId} | 
[**service_order_parts_get_work_order_parts**](ServiceOrderPartsApi.md#service_order_parts_get_work_order_parts) | **GET** /api/service/workorders/{serviceOrderId}/parts | 
[**service_order_parts_update_work_order_parts**](ServiceOrderPartsApi.md#service_order_parts_update_work_order_parts) | **PUT** /api/service/workorders/{serviceOrderId}/parts | 

# **service_order_parts_create_work_order_parts**
> object service_order_parts_create_work_order_parts(body, service_order_id)



ServiceOrderChargeType: Part, Labor, Charge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPartsApi()
body = swagger_client.QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel() # QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel | 
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_parts_create_work_order_parts(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->service_order_parts_create_work_order_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel**](QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairCreateModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_parts_delete_work_order_task**
> object service_order_parts_delete_work_order_task(service_order_id, service_order_item_part_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPartsApi()
service_order_id = 56 # int | 
service_order_item_part_id = 56 # int | 

try:
    api_response = api_instance.service_order_parts_delete_work_order_task(service_order_id, service_order_item_part_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->service_order_parts_delete_work_order_task: %s\n" % e)
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

# **service_order_parts_get_work_order_parts**
> list[QualerApiModelsServiceOrdersToServiceOrderPartRepairResponse] service_order_parts_get_work_order_parts(service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPartsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_parts_get_work_order_parts(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->service_order_parts_get_work_order_parts: %s\n" % e)
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

# **service_order_parts_update_work_order_parts**
> object service_order_parts_update_work_order_parts(body, service_order_id)



ServiceOrderChargeType: Part, Labor, Charge

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPartsApi()
body = swagger_client.QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel() # QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel | 
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_parts_update_work_order_parts(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPartsApi->service_order_parts_update_work_order_parts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel**](QualerWebMvcAreasApiModelsServiceOrdersFromServiceOrderPartRepairUpdateModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

