# swagger_client.ServiceOrderItemTasksApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_item_tasks_create_work_item_task**](ServiceOrderItemTasksApi.md#service_order_item_tasks_create_work_item_task) | **POST** /api/service/workitems/{workItemId}/tasks | 
[**service_order_item_tasks_delete_work_item_task**](ServiceOrderItemTasksApi.md#service_order_item_tasks_delete_work_item_task) | **DELETE** /api/service/workitems/{workItemId}/tasks/{taskId} | 
[**service_order_item_tasks_get_work_item_task**](ServiceOrderItemTasksApi.md#service_order_item_tasks_get_work_item_task) | **GET** /api/service/workitems/{workItemId}/tasks/{taskId} | 
[**service_order_item_tasks_get_work_item_tasks**](ServiceOrderItemTasksApi.md#service_order_item_tasks_get_work_item_tasks) | **GET** /api/service/workitems/{workItemId}/tasks | 

# **service_order_item_tasks_create_work_item_task**
> object service_order_item_tasks_create_work_item_task(body, work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemTasksApi()
body = swagger_client.QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel() # QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel | 
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_item_tasks_create_work_item_task(body, work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->service_order_item_tasks_create_work_item_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel**](QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel.md)|  | 
 **work_item_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_tasks_delete_work_item_task**
> object service_order_item_tasks_delete_work_item_task(work_item_id, task_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 
task_id = 56 # int | 

try:
    api_response = api_instance.service_order_item_tasks_delete_work_item_task(work_item_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->service_order_item_tasks_delete_work_item_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_tasks_get_work_item_task**
> object service_order_item_tasks_get_work_item_task(work_item_id, task_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 
task_id = 56 # int | 

try:
    api_response = api_instance.service_order_item_tasks_get_work_item_task(work_item_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->service_order_item_tasks_get_work_item_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **task_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_tasks_get_work_item_tasks**
> object service_order_item_tasks_get_work_item_tasks(work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_item_tasks_get_work_item_tasks(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->service_order_item_tasks_get_work_item_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

