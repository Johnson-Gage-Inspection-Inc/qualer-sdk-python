# qualer_sdk.AssetServiceRecordsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_asset_service_record**](AssetServiceRecordsApi.md#add_asset_service_record) | **POST** /api/assets/{assetId}/assetservicerecords | 
[**document_list**](AssetServiceRecordsApi.md#document_list) | **GET** /api/assetservicerecords/{AssetServiceRecordId}/documents/files | 
[**download_document**](AssetServiceRecordsApi.md#download_document) | **GET** /api/assetservicerecords/{AssetServiceRecordId}/documents/{FileName} | 
[**download_documents**](AssetServiceRecordsApi.md#download_documents) | **GET** /api/assetservicerecords/{assetServiceRecordId}/documents | 
[**get_asset_service_record**](AssetServiceRecordsApi.md#get_asset_service_record) | **GET** /api/assetservicerecords/{AssetServiceRecordId} | 
[**get_asset_service_records**](AssetServiceRecordsApi.md#get_asset_service_records) | **GET** /api/assetservicerecords | 
[**get_asset_service_records_by_asset**](AssetServiceRecordsApi.md#get_asset_service_records_by_asset) | **GET** /api/assets/{assetId}/assetservicerecords | 
[**update_asset_service_record**](AssetServiceRecordsApi.md#update_asset_service_record) | **PUT** /api/assetservicerecords/{assetServiceRecordId} | 
[**upload_documents**](AssetServiceRecordsApi.md#upload_documents) | **POST** /api/assetservicerecords/{assetServiceRecordId}/documents | 


# **add_asset_service_record**
> object add_asset_service_record(asset_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_id = 56 # int | 
model = qualer_sdk.AssetServiceRecordsFromAddAssetServiceRecordModel() # AssetServiceRecordsFromAddAssetServiceRecordModel | 

try:
    api_response = api_instance.add_asset_service_record(asset_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->add_asset_service_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **model** | [**AssetServiceRecordsFromAddAssetServiceRecordModel**](AssetServiceRecordsFromAddAssetServiceRecordModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **document_list**
> list[str] document_list(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_service_record_id = 'asset_service_record_id_example' # str | 
model_asset_service_record_id = 56 # int |  (optional)

try:
    api_response = api_instance.document_list(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->document_list: %s\n" % e)
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

# **download_document**
> object download_document(asset_service_record_id, file_name, model_asset_service_record_id=model_asset_service_record_id, model_file_name=model_file_name)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_service_record_id = 'asset_service_record_id_example' # str | 
file_name = 'file_name_example' # str | 
model_asset_service_record_id = 56 # int |  (optional)
model_file_name = 'model_file_name_example' # str |  (optional)

try:
    api_response = api_instance.download_document(asset_service_record_id, file_name, model_asset_service_record_id=model_asset_service_record_id, model_file_name=model_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->download_document: %s\n" % e)
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

# **download_documents**
> object download_documents(asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_service_record_id = 56 # int | 

try:
    api_response = api_instance.download_documents(asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->download_documents: %s\n" % e)
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

# **get_asset_service_record**
> AssetServiceRecordsToAssetServiceRecordResponseModel get_asset_service_record(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_service_record_id = 'asset_service_record_id_example' # str | 
model_asset_service_record_id = 56 # int |  (optional)

try:
    api_response = api_instance.get_asset_service_record(asset_service_record_id, model_asset_service_record_id=model_asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->get_asset_service_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **str**|  | 
 **model_asset_service_record_id** | **int**|  | [optional] 

### Return type

[**AssetServiceRecordsToAssetServiceRecordResponseModel**](AssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_records**
> AssetServiceRecordsToAssetServiceRecordResponseModel get_asset_service_records(model_asset_id=model_asset_id, model_serial_number=model_serial_number, model_from=model_from, model_to=model_to)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
model_asset_id = 56 # int |  (optional)
model_serial_number = 'model_serial_number_example' # str |  (optional)
model_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
model_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_asset_service_records(model_asset_id=model_asset_id, model_serial_number=model_serial_number, model_from=model_from, model_to=model_to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->get_asset_service_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_asset_id** | **int**|  | [optional] 
 **model_serial_number** | **str**|  | [optional] 
 **model_from** | **datetime**|  | [optional] 
 **model_to** | **datetime**|  | [optional] 

### Return type

[**AssetServiceRecordsToAssetServiceRecordResponseModel**](AssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_records_by_asset**
> list[AssetServiceRecordsToAssetServiceRecordResponseModel] get_asset_service_records_by_asset(asset_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_id = 56 # int | 

try:
    api_response = api_instance.get_asset_service_records_by_asset(asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->get_asset_service_records_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 

### Return type

[**list[AssetServiceRecordsToAssetServiceRecordResponseModel]**](AssetServiceRecordsToAssetServiceRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_service_record**
> object update_asset_service_record(asset_service_record_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_service_record_id = 56 # int | 
model = qualer_sdk.AssetServiceRecordsFromUpdateAssetServiceRecordModel() # AssetServiceRecordsFromUpdateAssetServiceRecordModel | 

try:
    api_response = api_instance.update_asset_service_record(asset_service_record_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->update_asset_service_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_service_record_id** | **int**|  | 
 **model** | [**AssetServiceRecordsFromUpdateAssetServiceRecordModel**](AssetServiceRecordsFromUpdateAssetServiceRecordModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_documents**
> object upload_documents(asset_service_record_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetServiceRecordsApi()
asset_service_record_id = 56 # int | 

try:
    api_response = api_instance.upload_documents(asset_service_record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetServiceRecordsApi->upload_documents: %s\n" % e)
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

