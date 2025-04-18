# swagger_client.ClientEmployeesApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_employees_create_employee**](ClientEmployeesApi.md#client_employees_create_employee) | **POST** /api/service/clients/employees | 
[**client_employees_get_employee**](ClientEmployeesApi.md#client_employees_get_employee) | **GET** /api/service/clients/employees/{EmployeeId} | 
[**client_employees_get_employees**](ClientEmployeesApi.md#client_employees_get_employees) | **GET** /api/service/clients/{clientCompanyId}/employees | 
[**client_employees_send_employee_email**](ClientEmployeesApi.md#client_employees_send_employee_email) | **PUT** /api/service/clients/employees/{employeeId}/sendemail | 

# **client_employees_create_employee**
> object client_employees_create_employee(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientEmployeesApi()
body = swagger_client.QualerApiModelsClientsFromSponsoredEmployeeModel() # QualerApiModelsClientsFromSponsoredEmployeeModel | 

try:
    api_response = api_instance.client_employees_create_employee(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->client_employees_create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsClientsFromSponsoredEmployeeModel**](QualerApiModelsClientsFromSponsoredEmployeeModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_employees_get_employee**
> QualerApiModelsClientsToEmployeeResponseModel client_employees_get_employee(employee_id, model_employee_id=model_employee_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientEmployeesApi()
employee_id = 'employee_id_example' # str | 
model_employee_id = 56 # int |  (optional)

try:
    api_response = api_instance.client_employees_get_employee(employee_id, model_employee_id=model_employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->client_employees_get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **str**|  | 
 **model_employee_id** | **int**|  | [optional] 

### Return type

[**QualerApiModelsClientsToEmployeeResponseModel**](QualerApiModelsClientsToEmployeeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_employees_get_employees**
> list[QualerApiModelsClientsToEmployeeResponseModel] client_employees_get_employees(client_company_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientEmployeesApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.client_employees_get_employees(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->client_employees_get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**list[QualerApiModelsClientsToEmployeeResponseModel]**](QualerApiModelsClientsToEmployeeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_employees_send_employee_email**
> object client_employees_send_employee_email(body, employee_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientEmployeesApi()
body = swagger_client.QualerApiModelsClientsFromSendEmployeeEmailModel() # QualerApiModelsClientsFromSendEmployeeEmailModel | 
employee_id = 56 # int | 

try:
    api_response = api_instance.client_employees_send_employee_email(body, employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->client_employees_send_employee_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsClientsFromSendEmployeeEmailModel**](QualerApiModelsClientsFromSendEmployeeEmailModel.md)|  | 
 **employee_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

