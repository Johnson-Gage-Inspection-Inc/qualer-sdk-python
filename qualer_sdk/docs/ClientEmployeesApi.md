# qualer_sdk.ClientEmployeesApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_employees_create_employee**](ClientEmployeesApi.md#client_employees_create_employee) | **POST** /api/service/clients/employees | 
[**client_employees_get_employee**](ClientEmployeesApi.md#client_employees_get_employee) | **GET** /api/service/clients/employees/{EmployeeId} | 
[**client_employees_get_employees**](ClientEmployeesApi.md#client_employees_get_employees) | **GET** /api/service/clients/{clientCompanyId}/employees | 
[**client_employees_send_employee_email**](ClientEmployeesApi.md#client_employees_send_employee_email) | **PUT** /api/service/clients/employees/{employeeId}/sendemail | 


# **client_employees_create_employee**
> object client_employees_create_employee(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
model = qualer_sdk.QualerApiModelsClientsFromSponsoredEmployeeModel() # QualerApiModelsClientsFromSponsoredEmployeeModel | 

try:
    api_response = api_instance.client_employees_create_employee(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->client_employees_create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsClientsFromSponsoredEmployeeModel**](QualerApiModelsClientsFromSponsoredEmployeeModel.md)|  | 

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
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
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
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientEmployeesApi()
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
> object client_employees_send_employee_email(employee_id, model)



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
model = qualer_sdk.QualerApiModelsClientsFromSendEmployeeEmailModel() # QualerApiModelsClientsFromSendEmployeeEmailModel | 

try:
    api_response = api_instance.client_employees_send_employee_email(employee_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientEmployeesApi->client_employees_send_employee_email: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **model** | [**QualerApiModelsClientsFromSendEmployeeEmailModel**](QualerApiModelsClientsFromSendEmployeeEmailModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

