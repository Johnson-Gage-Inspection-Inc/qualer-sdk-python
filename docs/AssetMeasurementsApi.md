# qualer_sdk.AssetMeasurementsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_measurements_by_asset**](AssetMeasurementsApi.md#get_measurements_by_asset) | **GET** /api/assets/{assetId}/measurements | 


# **get_measurements_by_asset**
> list[MeasurementsToMeasurementRecordResponseModel] get_measurements_by_asset(asset_id, _from=_from, to=to)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetMeasurementsApi()
asset_id = 56 # int | 
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_measurements_by_asset(asset_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetMeasurementsApi->get_measurements_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 

### Return type

[**list[MeasurementsToMeasurementRecordResponseModel]**](MeasurementsToMeasurementRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

