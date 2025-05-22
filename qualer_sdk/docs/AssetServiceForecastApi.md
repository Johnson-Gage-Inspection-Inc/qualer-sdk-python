# qualer_sdk.AssetServiceForecastApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_forecast_list**](AssetServiceForecastApi.md#get_asset_forecast_list) | **GET** /api/assetserviceforecast | 
[**get_client_asset_forecast_list**](AssetServiceForecastApi.md#get_client_asset_forecast_list) | **GET** /api/assetserviceforecast/client/{clientCompanyId} | 


# **get_asset_forecast_list**
> list[QualerApiModelsAssetToAssetServiceForecastModel] get_asset_forecast_list()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceForecastApi()

try:
    api_response = api_instance.get_asset_forecast_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceForecastApi->get_asset_forecast_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsAssetToAssetServiceForecastModel]**](QualerApiModelsAssetToAssetServiceForecastModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_asset_forecast_list**
> list[QualerApiModelsAssetToAssetServiceForecastModel] get_client_asset_forecast_list(client_company_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceForecastApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.get_client_asset_forecast_list(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceForecastApi->get_client_asset_forecast_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetServiceForecastModel]**](QualerApiModelsAssetToAssetServiceForecastModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

