# qualer_sdk.ClientEmployeesApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_employee**](ClientEmployeesApi.md#create_employee) | **POST** /api/service/clients/employees | 
[**get_employee**](ClientEmployeesApi.md#get_employee) | **GET** /api/service/clients/employees/{EmployeeId} | 
[**get_employees**](ClientEmployeesApi.md#get_employees) | **GET** /api/service/clients/{clientCompanyId}/employees | 
[**send_employee_email**](ClientEmployeesApi.md#send_employee_email) | **PUT** /api/service/clients/employees/{employeeId}/sendemail | 


# **create_employee**
> object create_employee(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
model = qualer_sdk.ClientsFromSponsoredEmployeeModel() # ClientsFromSponsoredEmployeeModel | 

try:
    api_response = api_instance.create_employee(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ClientsFromSponsoredEmployeeModel**](ClientsFromSponsoredEmployeeModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employee**
> ClientsToEmployeeResponseModel get_employee(employee_id, model_employee_id=model_employee_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
employee_id = 'employee_id_example' # str | 
model_employee_id = 56 # int |  (optional)

try:
    api_response = api_instance.get_employee(employee_id, model_employee_id=model_employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 
 **model_employee_id** | **int**|  | [optional] 

### Return type

[**ClientsToEmployeeResponseModel**](ClientsToEmployeeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_employees**
> list[ClientsToEmployeeResponseModel] get_employees(client_company_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.get_employees(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**list[ClientsToEmployeeResponseModel]**](ClientsToEmployeeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_employee_email**
> object send_employee_email(employee_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
employee_id = 56 # int | 
model = qualer_sdk.ClientsFromSendEmployeeEmailModel() # ClientsFromSendEmployeeEmailModel | 

try:
    api_response = api_instance.send_employee_email(employee_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->send_employee_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **model** | [**ClientsFromSendEmployeeEmailModel**](ClientsFromSendEmployeeEmailModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

