# qualer_sdk.ServiceOrderItemTasksApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_work_item_task**](ServiceOrderItemTasksApi.md#create_work_item_task) | **POST** /api/service/workitems/{workItemId}/tasks | 
[**delete_work_item_task**](ServiceOrderItemTasksApi.md#delete_work_item_task) | **DELETE** /api/service/workitems/{workItemId}/tasks/{taskId} | 
[**get_work_item_task**](ServiceOrderItemTasksApi.md#get_work_item_task) | **GET** /api/service/workitems/{workItemId}/tasks/{taskId} | 
[**get_work_item_tasks**](ServiceOrderItemTasksApi.md#get_work_item_tasks) | **GET** /api/service/workitems/{workItemId}/tasks | 


# **create_work_item_task**
> object create_work_item_task(work_item_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 
model = qualer_sdk.QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel() # QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel | 

try:
    api_response = api_instance.create_work_item_task(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->create_work_item_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel**](QualerApiModelsServiceOrderItemTasksFromServiceOrderItemTaskCreateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_item_task**
> object delete_work_item_task(work_item_id, task_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 
task_id = 56 # int | 

try:
    api_response = api_instance.delete_work_item_task(work_item_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->delete_work_item_task: %s\n" % e)
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

# **get_work_item_task**
> object get_work_item_task(work_item_id, task_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 
task_id = 56 # int | 

try:
    api_response = api_instance.get_work_item_task(work_item_id, task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->get_work_item_task: %s\n" % e)
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

# **get_work_item_tasks**
> object get_work_item_tasks(work_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemTasksApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.get_work_item_tasks(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemTasksApi->get_work_item_tasks: %s\n" % e)
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

