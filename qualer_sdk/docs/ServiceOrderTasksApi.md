# swagger_client.ServiceOrderTasksApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_tasks_create_work_order_task**](ServiceOrderTasksApi.md#service_order_tasks_create_work_order_task) | **POST** /api/service/workorders/{serviceOrderId}/tasks | 
[**service_order_tasks_delete_work_order_task**](ServiceOrderTasksApi.md#service_order_tasks_delete_work_order_task) | **DELETE** /api/service/workorders/{serviceOrderId}/Tasks/{serviceOrderTaskId} | 
[**service_order_tasks_get_work_order_tasks**](ServiceOrderTasksApi.md#service_order_tasks_get_work_order_tasks) | **GET** /api/service/workorders/{serviceOrderId}/tasks | 
[**service_order_tasks_update_work_order_task**](ServiceOrderTasksApi.md#service_order_tasks_update_work_order_task) | **PUT** /api/service/workorders/{serviceOrderId}/tasks | 


# **service_order_tasks_create_work_order_task**
> object service_order_tasks_create_work_order_task(service_order_id, model)



- If StartTime and FinishTime are defined TimeSpent will be ignored and recalculated based on their difference  - If StartTime and FinishTime are not defined they will be recalculated      - if StartTime - in will be recalculated FinishTime - TimeSpent      - if FinishTime - in will be recalculated StartTime + TimeSpent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderTasksApi()
service_order_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel() # QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel | 

try:
    api_response = api_instance.service_order_tasks_create_work_order_task(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderTasksApi->service_order_tasks_create_work_order_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel**](QualerApiModelsServiceOrdersFromServiceOrderTaskCreateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_tasks_delete_work_order_task**
> object service_order_tasks_delete_work_order_task(service_order_id, service_order_task_id)





### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderTasksApi()
service_order_id = 56 # int | 
service_order_task_id = 56 # int | 

try:
    api_response = api_instance.service_order_tasks_delete_work_order_task(service_order_id, service_order_task_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderTasksApi->service_order_tasks_delete_work_order_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **service_order_task_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_tasks_get_work_order_tasks**
> list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse] service_order_tasks_get_work_order_tasks(service_order_id)



TimeSpent  Integer part (before dot) is hours  Fractional part (after dot) is minutes  For example:      if time spent is 10 minutes -&gt; 10 / 60 = 0.1666666666666667      if time spent is 65 minutes -&gt; (65 - 60) + (5 / 60) = 1.0833333333333333

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderTasksApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_tasks_get_work_order_tasks(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderTasksApi->service_order_tasks_get_work_order_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToServiceOrderTaskResponse]**](QualerApiModelsServiceOrdersToServiceOrderTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_tasks_update_work_order_task**
> object service_order_tasks_update_work_order_task(service_order_id, model)



- If StartTime and FinishTime are defined TimeSpent will be ignored and recalculated based on their difference  - If StartTime and FinishTime are not defined they will be recalculated      - if StartTime - in will be recalculated FinishTime - TimeSpent      - if FinishTime - in will be recalculated StartTime + TimeSpent

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderTasksApi()
service_order_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel() # QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel | 

try:
    api_response = api_instance.service_order_tasks_update_work_order_task(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderTasksApi->service_order_tasks_update_work_order_task: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel**](QualerApiModelsServiceOrdersFromServiceOrderTaskUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

