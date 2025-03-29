# swagger_client.AssetServiceForecastApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_service_forecast_get_asset_forecast_list**](AssetServiceForecastApi.md#asset_service_forecast_get_asset_forecast_list) | **GET** /api/assetserviceforecast | 
[**asset_service_forecast_get_client_asset_forecast_list**](AssetServiceForecastApi.md#asset_service_forecast_get_client_asset_forecast_list) | **GET** /api/assetserviceforecast/client/{clientCompanyId} | 

# **asset_service_forecast_get_asset_forecast_list**
> list[QualerApiModelsAssetToAssetServiceForecastModel] asset_service_forecast_get_asset_forecast_list()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceForecastApi()

try:
    api_response = api_instance.asset_service_forecast_get_asset_forecast_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceForecastApi->asset_service_forecast_get_asset_forecast_list: %s\n" % e)
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

# **asset_service_forecast_get_client_asset_forecast_list**
> list[QualerApiModelsAssetToAssetServiceForecastModel] asset_service_forecast_get_client_asset_forecast_list(client_company_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceForecastApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.asset_service_forecast_get_client_asset_forecast_list(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceForecastApi->asset_service_forecast_get_client_asset_forecast_list: %s\n" % e)
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

