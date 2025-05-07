# qualer_sdk.AssetMaintenancePlansApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_maintenance_plans_get_maintenance_plan**](AssetMaintenancePlansApi.md#asset_maintenance_plans_get_maintenance_plan) | **GET** /api/assets/{assetId}/plans/{maintenancePlanId} | 
[**asset_maintenance_plans_get_maintenance_plans**](AssetMaintenancePlansApi.md#asset_maintenance_plans_get_maintenance_plans) | **GET** /api/assets/{assetId}/plans | 
[**asset_maintenance_plans_reset_initial_service_date**](AssetMaintenancePlansApi.md#asset_maintenance_plans_reset_initial_service_date) | **PUT** /api/assets/{assetId}/plans/{maintenancePlanId} | 


# **asset_maintenance_plans_get_maintenance_plan**
> QualerApiModelsAssetToAssetMaintenancePlanModel asset_maintenance_plans_get_maintenance_plan(asset_id, maintenance_plan_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetMaintenancePlansApi()
asset_id = 56 # int | 
maintenance_plan_id = 56 # int | 

try:
    api_response = api_instance.asset_maintenance_plans_get_maintenance_plan(asset_id, maintenance_plan_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetMaintenancePlansApi->asset_maintenance_plans_get_maintenance_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **maintenance_plan_id** | **int**|  | 

### Return type

[**QualerApiModelsAssetToAssetMaintenancePlanModel**](QualerApiModelsAssetToAssetMaintenancePlanModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_maintenance_plans_get_maintenance_plans**
> QualerApiModelsAssetToAssetMaintenancePlanModel asset_maintenance_plans_get_maintenance_plans(asset_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetMaintenancePlansApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.asset_maintenance_plans_get_maintenance_plans(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetMaintenancePlansApi->asset_maintenance_plans_get_maintenance_plans: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**QualerApiModelsAssetToAssetMaintenancePlanModel**](QualerApiModelsAssetToAssetMaintenancePlanModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_maintenance_plans_reset_initial_service_date**
> object asset_maintenance_plans_reset_initial_service_date(asset_id, maintenance_plan_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetMaintenancePlansApi()
asset_id = 56 # int | 
maintenance_plan_id = 56 # int | 
model = qualer_sdk.QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat() # QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat | 

try:
    api_response = api_instance.asset_maintenance_plans_reset_initial_service_date(asset_id, maintenance_plan_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetMaintenancePlansApi->asset_maintenance_plans_reset_initial_service_date: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **maintenance_plan_id** | **int**|  | 
 **model** | [**QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat**](QualerApiModelsAssetFromUpdateAssetMaintenanceServiceDat.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

