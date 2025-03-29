# swagger_client.ClientAssetServiceRecordsApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_asset_service_records_get_asset_service_records_by_asset**](ClientAssetServiceRecordsApi.md#client_asset_service_records_get_asset_service_records_by_asset) | **GET** /api/service/clients/assets/{assetId}/assetservicerecords | 

# **client_asset_service_records_get_asset_service_records_by_asset**
> list[QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel] client_asset_service_records_get_asset_service_records_by_asset(asset_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientAssetServiceRecordsApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.client_asset_service_records_get_asset_service_records_by_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetServiceRecordsApi->client_asset_service_records_get_asset_service_records_by_asset: %s\n" % e)
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

