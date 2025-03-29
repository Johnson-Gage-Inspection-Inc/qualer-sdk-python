# swagger_client.AssetServiceRecordsApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_service_records_add_asset_service_record**](AssetServiceRecordsApi.md#asset_service_records_add_asset_service_record) | **POST** /api/assets/{assetId}/assetservicerecords | 
[**asset_service_records_document_list**](AssetServiceRecordsApi.md#asset_service_records_document_list) | **GET** /api/assetservicerecords/{AssetServiceRecordId}/documents/files | 
[**asset_service_records_download_document**](AssetServiceRecordsApi.md#asset_service_records_download_document) | **GET** /api/assetservicerecords/{AssetServiceRecordId}/documents/{FileName} | 
[**asset_service_records_download_documents**](AssetServiceRecordsApi.md#asset_service_records_download_documents) | **GET** /api/assetservicerecords/{assetServiceRecordId}/documents | 
[**asset_service_records_get_asset_service_record**](AssetServiceRecordsApi.md#asset_service_records_get_asset_service_record) | **GET** /api/assetservicerecords/{AssetServiceRecordId} | 
[**asset_service_records_get_asset_service_records**](AssetServiceRecordsApi.md#asset_service_records_get_asset_service_records) | **GET** /api/assetservicerecords | 
[**asset_service_records_get_asset_service_records_by_asset**](AssetServiceRecordsApi.md#asset_service_records_get_asset_service_records_by_asset) | **GET** /api/assets/{assetId}/assetservicerecords | 
[**asset_service_records_update_asset_service_record**](AssetServiceRecordsApi.md#asset_service_records_update_asset_service_record) | **PUT** /api/assetservicerecords/{assetServiceRecordId} | 
[**asset_service_records_upload_documents**](AssetServiceRecordsApi.md#asset_service_records_upload_documents) | **POST** /api/assetservicerecords/{assetServiceRecordId}/documents | 

# **asset_service_records_add_asset_service_record**
> object asset_service_records_add_asset_service_record(body, asset_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
body = swagger_client.QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel() # QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel | 
asset_id = 56 # int | 

try:
    api_response = api_instance.asset_service_records_add_asset_service_record(body, asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_add_asset_service_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel**](QualerApiModelsAssetServiceRecordsFromAddAssetServiceRecordModel.md)|  | 
 **asset_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_document_list**
> list[str] asset_service_records_document_list(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
asset_service_record_id = 'asset_service_record_id_example' # str | 
model_asset_service_record_id = 56 # int |  (optional)

try:
    api_response = api_instance.asset_service_records_document_list(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_document_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **str**|  | 
 **model_asset_service_record_id** | **int**|  | [optional] 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_download_document**
> object asset_service_records_download_document(asset_service_record_id, file_name, model_asset_service_record_id=model_asset_service_record_id, model_file_name=model_file_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
asset_service_record_id = 'asset_service_record_id_example' # str | 
file_name = 'file_name_example' # str | 
model_asset_service_record_id = 56 # int |  (optional)
model_file_name = 'model_file_name_example' # str |  (optional)

try:
    api_response = api_instance.asset_service_records_download_document(asset_service_record_id, file_name, model_asset_service_record_id=model_asset_service_record_id, model_file_name=model_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_download_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **str**|  | 
 **file_name** | **str**|  | 
 **model_asset_service_record_id** | **int**|  | [optional] 
 **model_file_name** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_download_documents**
> object asset_service_records_download_documents(asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
asset_service_record_id = 56 # int | 

try:
    api_response = api_instance.asset_service_records_download_documents(asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_download_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_get_asset_service_record**
> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel asset_service_records_get_asset_service_record(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
asset_service_record_id = 'asset_service_record_id_example' # str | 
model_asset_service_record_id = 56 # int |  (optional)

try:
    api_response = api_instance.asset_service_records_get_asset_service_record(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_get_asset_service_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **str**|  | 
 **model_asset_service_record_id** | **int**|  | [optional] 

### Return type

[**QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel**](QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_get_asset_service_records**
> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel asset_service_records_get_asset_service_records(model_asset_id=model_asset_id, model_serial_number=model_serial_number, model_from=model_from, model_to=model_to)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
model_asset_id = 56 # int |  (optional)
model_serial_number = 'model_serial_number_example' # str |  (optional)
model_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
model_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.asset_service_records_get_asset_service_records(model_asset_id=model_asset_id, model_serial_number=model_serial_number, model_from=model_from, model_to=model_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_get_asset_service_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_asset_id** | **int**|  | [optional] 
 **model_serial_number** | **str**|  | [optional] 
 **model_from** | **datetime**|  | [optional] 
 **model_to** | **datetime**|  | [optional] 

### Return type

[**QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel**](QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_get_asset_service_records_by_asset**
> QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel asset_service_records_get_asset_service_records_by_asset(asset_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.asset_service_records_get_asset_service_records_by_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_get_asset_service_records_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel**](QualerApiModelsAssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_update_asset_service_record**
> object asset_service_records_update_asset_service_record(body, asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
body = swagger_client.QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel() # QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel | 
asset_service_record_id = 56 # int | 

try:
    api_response = api_instance.asset_service_records_update_asset_service_record(body, asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_update_asset_service_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel**](QualerApiModelsAssetServiceRecordsFromUpdateAssetServiceRecordModel.md)|  | 
 **asset_service_record_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_service_records_upload_documents**
> object asset_service_records_upload_documents(asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetServiceRecordsApi()
asset_service_record_id = 56 # int | 

try:
    api_response = api_instance.asset_service_records_upload_documents(asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->asset_service_records_upload_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

