# swagger_client.EmployeesApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**employees_add_employee_department**](EmployeesApi.md#employees_add_employee_department) | **POST** /api/employees/{employeeId}/department | 
[**employees_create_employee**](EmployeesApi.md#employees_create_employee) | **POST** /api/employees | Create Employee
[**employees_delete_employee_department**](EmployeesApi.md#employees_delete_employee_department) | **DELETE** /api/employees/{employeeId}/department/{departmentId} | 
[**employees_get_employee**](EmployeesApi.md#employees_get_employee) | **GET** /api/employees/{employeeId} | 
[**employees_get_employees**](EmployeesApi.md#employees_get_employees) | **GET** /api/employees | 
[**employees_update_employee**](EmployeesApi.md#employees_update_employee) | **PUT** /api/employees/{employeeId} | Update Employee


# **employees_add_employee_department**
> object employees_add_employee_department(employee_id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeesApi()
employee_id = 56 # int | 
model = swagger_client.QualerApiModelsEmployeesFromEmployeeDepartmentModel() # QualerApiModelsEmployeesFromEmployeeDepartmentModel | 

try:
    # 
    api_response = api_instance.employees_add_employee_department(employee_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->employees_add_employee_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **model** | [**QualerApiModelsEmployeesFromEmployeeDepartmentModel**](QualerApiModelsEmployeesFromEmployeeDepartmentModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_create_employee**
> QualerApiModelsEmployeesToCreatedEmployeeResponse employees_create_employee(model)

Create Employee

CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeesApi()
model = swagger_client.QualerApiModelsEmployeesFromCreateEmployeeModel() # QualerApiModelsEmployeesFromCreateEmployeeModel | 

try:
    # Create Employee
    api_response = api_instance.employees_create_employee(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->employees_create_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsEmployeesFromCreateEmployeeModel**](QualerApiModelsEmployeesFromCreateEmployeeModel.md)|  | 

### Return type

[**QualerApiModelsEmployeesToCreatedEmployeeResponse**](QualerApiModelsEmployeesToCreatedEmployeeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_delete_employee_department**
> object employees_delete_employee_department(employee_id, department_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeesApi()
employee_id = 56 # int | 
department_id = 56 # int | 

try:
    # 
    api_response = api_instance.employees_delete_employee_department(employee_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->employees_delete_employee_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **department_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_get_employee**
> QualerApiModelsClientsToEmployeeResponseModel employees_get_employee(employee_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeesApi()
employee_id = 56 # int | 

try:
    api_response = api_instance.employees_get_employee(employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->employees_get_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 

### Return type

[**QualerApiModelsClientsToEmployeeResponseModel**](QualerApiModelsClientsToEmployeeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_get_employees**
> list[QualerApiModelsClientsToEmployeeResponseModel] employees_get_employees(model_search_string=model_search_string)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeesApi()
model_search_string = 'model_search_string_example' # str |  (optional)

try:
    api_response = api_instance.employees_get_employees(model_search_string=model_search_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->employees_get_employees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_search_string** | **str**|  | [optional] 

### Return type

[**list[QualerApiModelsClientsToEmployeeResponseModel]**](QualerApiModelsClientsToEmployeeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **employees_update_employee**
> object employees_update_employee(employee_id, model)

Update Employee

CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.EmployeesApi()
employee_id = 56 # int | 
model = swagger_client.QualerApiModelsEmployeesFromUpdateEmployeeModel() # QualerApiModelsEmployeesFromUpdateEmployeeModel | 

try:
    # Update Employee
    api_response = api_instance.employees_update_employee(employee_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->employees_update_employee: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **model** | [**QualerApiModelsEmployeesFromUpdateEmployeeModel**](QualerApiModelsEmployeesFromUpdateEmployeeModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

