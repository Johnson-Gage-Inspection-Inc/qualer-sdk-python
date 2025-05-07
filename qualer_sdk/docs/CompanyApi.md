# qualer_sdk.CompanyApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**company_add_department**](CompanyApi.md#company_add_department) | **POST** /api/company/departments | 
[**company_delete_department**](CompanyApi.md#company_delete_department) | **DELETE** /api/company/departments/{departmentId} | 
[**company_departments**](CompanyApi.md#company_departments) | **GET** /api/company/departments | 
[**company_lookups**](CompanyApi.md#company_lookups) | **GET** /api/company/lookups | 
[**company_site_rooms**](CompanyApi.md#company_site_rooms) | **GET** /api/company/sites/{id}/rooms | 
[**company_sites**](CompanyApi.md#company_sites) | **GET** /api/company/sites | 
[**company_update_department**](CompanyApi.md#company_update_department) | **PUT** /api/company/departments/{departmentId} | 


# **company_add_department**
> object company_add_department(model)



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
    api_response = api_instance.company_add_department(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_add_department: %s\n" % e)
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

# **company_delete_department**
> object company_delete_department(department_id)



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
    api_response = api_instance.company_delete_department(department_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_delete_department: %s\n" % e)
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

# **company_departments**
> list[QualerApiModelsCompanyToDepartmentsResponseModel] company_departments()



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
    api_response = api_instance.company_departments()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_departments: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsCompanyToDepartmentsResponseModel]**](QualerApiModelsCompanyToDepartmentsResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_lookups**
> list[str] company_lookups(lookup_type)



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
    api_response = api_instance.company_lookups(lookup_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_lookups: %s\n" % e)
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

# **company_site_rooms**
> list[QualerApiModelsCompanyToEnvironmentResponseModel] company_site_rooms(id)



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
    api_response = api_instance.company_site_rooms(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_site_rooms: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Site id  GET /api/company/sites | 

### Return type

[**list[QualerApiModelsCompanyToEnvironmentResponseModel]**](QualerApiModelsCompanyToEnvironmentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_sites**
> list[QualerApiModelsCompanyToSitesResponseModel] company_sites()



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
    api_response = api_instance.company_sites()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_sites: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsCompanyToSitesResponseModel]**](QualerApiModelsCompanyToSitesResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **company_update_department**
> object company_update_department(department_id, model)



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
    api_response = api_instance.company_update_department(department_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CompanyApi->company_update_department: %s\n" % e)
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

