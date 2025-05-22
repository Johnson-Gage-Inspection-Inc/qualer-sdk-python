# qualer_sdk.ClientMaintenancePlansApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_maintenance_plan_assets**](ClientMaintenancePlansApi.md#get_maintenance_plan_assets) | **GET** /api/service/clients/plans/{maintenancePlanId}/assets | 
[**get_maintenance_plans**](ClientMaintenancePlansApi.md#get_maintenance_plans) | **GET** /api/service/clients/{clientCompanyId}/plans | 


# **get_maintenance_plan_assets**
> list[QualerApiModelsAssetToAssetForecastApiResponseModel] get_maintenance_plan_assets(maintenance_plan_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientMaintenancePlansApi()
maintenance_plan_id = 56 # int | 

try:
    api_response = api_instance.get_maintenance_plan_assets(maintenance_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientMaintenancePlansApi->get_maintenance_plan_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **maintenance_plan_id** | **int**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetForecastApiResponseModel]**](QualerApiModelsAssetToAssetForecastApiResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_maintenance_plans**
> list[QualerApiModelsMaintenancePlansToMaintenancePlanResponse] get_maintenance_plans(client_company_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientMaintenancePlansApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.get_maintenance_plans(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientMaintenancePlansApi->get_maintenance_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**list[QualerApiModelsMaintenancePlansToMaintenancePlanResponse]**](QualerApiModelsMaintenancePlansToMaintenancePlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

