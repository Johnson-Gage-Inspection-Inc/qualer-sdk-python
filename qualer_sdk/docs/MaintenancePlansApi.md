# qualer_sdk.MaintenancePlansApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**maintenance_plans_get_maintenance_plan_assets**](MaintenancePlansApi.md#maintenance_plans_get_maintenance_plan_assets) | **GET** /api/plans/{maintenancePlanId}/assets | 
[**maintenance_plans_get_maintenance_plans**](MaintenancePlansApi.md#maintenance_plans_get_maintenance_plans) | **GET** /api/plans | 


# **maintenance_plans_get_maintenance_plan_assets**
> list[QualerApiModelsAssetToAssetForecastApiResponseModel] maintenance_plans_get_maintenance_plan_assets(maintenance_plan_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.MaintenancePlansApi()
maintenance_plan_id = 56 # int | 

try:
    api_response = api_instance.maintenance_plans_get_maintenance_plan_assets(maintenance_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenancePlansApi->maintenance_plans_get_maintenance_plan_assets: %s\n" % e)
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

# **maintenance_plans_get_maintenance_plans**
> list[QualerApiModelsMaintenancePlansToMaintenancePlanResponse] maintenance_plans_get_maintenance_plans()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.MaintenancePlansApi()

try:
    api_response = api_instance.maintenance_plans_get_maintenance_plans()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MaintenancePlansApi->maintenance_plans_get_maintenance_plans: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsMaintenancePlansToMaintenancePlanResponse]**](QualerApiModelsMaintenancePlansToMaintenancePlanResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

