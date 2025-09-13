# qualer_sdk.CompanyApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_department**](CompanyApi.md#add_department) | **POST** /api/company/departments | 
[**delete_department**](CompanyApi.md#delete_department) | **DELETE** /api/company/departments/{departmentId} | 
[**departments**](CompanyApi.md#departments) | **GET** /api/company/departments | 
[**lookups**](CompanyApi.md#lookups) | **GET** /api/company/lookups | 
[**site_rooms**](CompanyApi.md#site_rooms) | **GET** /api/company/sites/{id}/rooms | 
[**sites**](CompanyApi.md#sites) | **GET** /api/company/sites | 
[**update_department**](CompanyApi.md#update_department) | **PUT** /api/company/departments/{departmentId} | 


# **add_department**
> object add_department(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()
model = qualer_sdk.QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel() # QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel | 

try:
    # 
    api_response = api_instance.add_department(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->add_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel**](QualerWebMvcAreasApiModelsCompanyFromAddDepartmentModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_department**
> object delete_department(department_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()
department_id = 56 # int | 

try:
    # 
    api_response = api_instance.delete_department(department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->delete_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **departments**
> list[CompanyToDepartmentsResponseModel] departments()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()

try:
    api_response = api_instance.departments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->departments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CompanyToDepartmentsResponseModel]**](CompanyToDepartmentsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **lookups**
> list[str] lookups(lookup_type)



lookupName:  AssetClass = 1  AssetCriticality = 2  AssetCondition = 3  InventoryCategory = 4  InventoryUnit = 5  OrderItemInProgressWorkStatus = 6  OrderItemDelayWorkStatus = 7  OrderItemWithdrawnWorkStatus = 8  OrderItemCompletedWorkStatus = 9  OrderDelayedStatus = 10  ClientInvoicing = 11  ClientStanding = 12  ClientCategory = 13  CancelOrderReasons = 14  OrderItemLockedWorkStatus = 15

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()
lookup_type = 'lookup_type_example' # str | 

try:
    api_response = api_instance.lookups(lookup_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->lookups: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **lookup_type** | **str**|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **site_rooms**
> list[CompanyToEnvironmentResponseModel] site_rooms(id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()
id = 56 # int | Site id  GET /api/company/sites

try:
    # 
    api_response = api_instance.site_rooms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->site_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site id  GET /api/company/sites | 

### Return type

[**list[CompanyToEnvironmentResponseModel]**](CompanyToEnvironmentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sites**
> list[CompanyToSitesResponseModel] sites()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()

try:
    api_response = api_instance.sites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[CompanyToSitesResponseModel]**](CompanyToSitesResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_department**
> object update_department(department_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CompanyApi()
department_id = 56 # int | 
model = qualer_sdk.QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel() # QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel | 

try:
    # 
    api_response = api_instance.update_department(department_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->update_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **department_id** | **int**|  | 
 **model** | [**QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel**](QualerWebMvcAreasApiModelsCompanyFromUpdateDepartmentModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

