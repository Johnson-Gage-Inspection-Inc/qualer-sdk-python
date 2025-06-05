# qualer_sdk.EmployeesApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_employee_department**](EmployeesApi.md#add_employee_department) | **POST** /api/employees/{employeeId}/department | 
[**create_employee**](EmployeesApi.md#create_employee) | **POST** /api/employees | Create Employee
[**delete_employee_department**](EmployeesApi.md#delete_employee_department) | **DELETE** /api/employees/{employeeId}/department/{departmentId} | 
[**get_employee**](EmployeesApi.md#get_employee) | **GET** /api/employees/{employeeId} | 
[**get_employees**](EmployeesApi.md#get_employees) | **GET** /api/employees | 
[**update_employee**](EmployeesApi.md#update_employee) | **PUT** /api/employees/{employeeId} | Update Employee


# **add_employee_department**
> object add_employee_department(employee_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeesApi()
employee_id = 56 # int | 
model = qualer_sdk.QualerApiModelsEmployeesFromEmployeeDepartmentModel() # QualerApiModelsEmployeesFromEmployeeDepartmentModel | 

try:
    # 
    api_response = api_instance.add_employee_department(employee_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->add_employee_department: %s\n" % e)
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

# **create_employee**
> QualerApiModelsEmployeesToCreatedEmployeeResponse create_employee(model)

Create Employee

CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeesApi()
model = qualer_sdk.QualerApiModelsEmployeesFromCreateEmployeeModel() # QualerApiModelsEmployeesFromCreateEmployeeModel | 

try:
    # Create Employee
    api_response = api_instance.create_employee(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->create_employee: %s\n" % e)
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

# **delete_employee_department**
> object delete_employee_department(employee_id, department_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeesApi()
employee_id = 56 # int | 
department_id = 56 # int | 

try:
    # 
    api_response = api_instance.delete_employee_department(employee_id, department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->delete_employee_department: %s\n" % e)
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

# **get_employee**
> QualerApiModelsClientsToEmployeeResponseModel get_employee(employee_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeesApi()
employee_id = 56 # int | 

try:
    api_response = api_instance.get_employee(employee_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->get_employee: %s\n" % e)
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

# **get_employees**
> list[QualerApiModelsClientsToEmployeeResponseModel] get_employees(model_search_string=model_search_string)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeesApi()
model_search_string = 'model_search_string_example' # str |  (optional)

try:
    api_response = api_instance.get_employees(model_search_string=model_search_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->get_employees: %s\n" % e)
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

# **update_employee**
> object update_employee(employee_id, model)

Update Employee

CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeesApi()
employee_id = 56 # int | 
model = qualer_sdk.QualerApiModelsEmployeesFromUpdateEmployeeModel() # QualerApiModelsEmployeesFromUpdateEmployeeModel | 

try:
    # Update Employee
    api_response = api_instance.update_employee(employee_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeesApi->update_employee: %s\n" % e)
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

