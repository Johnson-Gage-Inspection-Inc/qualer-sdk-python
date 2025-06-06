# qualer_sdk.ClientAssetServiceRecordsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_asset_service_records_by_asset**](ClientAssetServiceRecordsApi.md#get_asset_service_records_by_asset) | **GET** /api/service/clients/assets/{assetId}/assetservicerecords | 


# **get_asset_service_records_by_asset**
> list[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel] get_asset_service_records_by_asset(asset_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetServiceRecordsApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.get_asset_service_records_by_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetServiceRecordsApi->get_asset_service_records_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**list[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel]**](QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

