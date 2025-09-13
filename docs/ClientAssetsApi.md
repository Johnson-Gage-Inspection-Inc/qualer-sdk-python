# qualer_sdk.ClientAssetsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_asset**](ClientAssetsApi.md#create_asset) | **POST** /api/service/clients/assets | 
[**get_all_assets**](ClientAssetsApi.md#get_all_assets) | **GET** /api/service/clients/assets | 
[**get_asset**](ClientAssetsApi.md#get_asset) | **GET** /api/service/clients/assets/{AssetId} | 
[**get_asset_counters**](ClientAssetsApi.md#get_asset_counters) | **GET** /api/service/clients/{clientCompanyId}/counters | 
[**get_asset_manager_list**](ClientAssetsApi.md#get_asset_manager_list) | **GET** /api/service/clients/{clientCompanyId}/assets/byfilter | GetAssetManagerList
[**get_assets**](ClientAssetsApi.md#get_assets) | **GET** /api/service/clients/{clientCompanyId}/assets | 


# **create_asset**
> object create_asset(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetsApi()
model = qualer_sdk.ClientsFromAssetModel() # ClientsFromAssetModel | 

try:
    api_response = api_instance.create_asset(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetsApi->create_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ClientsFromAssetModel**](ClientsFromAssetModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_assets**
> list[AssetToAssetResponseModel] get_all_assets(query_equipment_id=query_equipment_id, query_serial_number=query_serial_number, query_asset_tag=query_asset_tag, query_barcode=query_barcode, query_legacy_id=query_legacy_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetsApi()
query_equipment_id = 'query_equipment_id_example' # str |  (optional)
query_serial_number = 'query_serial_number_example' # str |  (optional)
query_asset_tag = 'query_asset_tag_example' # str |  (optional)
query_barcode = 'query_barcode_example' # str |  (optional)
query_legacy_id = 'query_legacy_id_example' # str |  (optional)

try:
    api_response = api_instance.get_all_assets(query_equipment_id=query_equipment_id, query_serial_number=query_serial_number, query_asset_tag=query_asset_tag, query_barcode=query_barcode, query_legacy_id=query_legacy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetsApi->get_all_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query_equipment_id** | **str**|  | [optional] 
 **query_serial_number** | **str**|  | [optional] 
 **query_asset_tag** | **str**|  | [optional] 
 **query_barcode** | **str**|  | [optional] 
 **query_legacy_id** | **str**|  | [optional] 

### Return type

[**list[AssetToAssetResponseModel]**](AssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> AssetToAssetResponseModel get_asset(asset_id, model_asset_id=model_asset_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetsApi()
asset_id = 'asset_id_example' # str | 
model_asset_id = 56 # int |  (optional)

try:
    api_response = api_instance.get_asset(asset_id, model_asset_id=model_asset_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetsApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **str**|  | 
 **model_asset_id** | **int**|  | [optional] 

### Return type

[**AssetToAssetResponseModel**](AssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_counters**
> AssetToClientAssetCountersResponseModel get_asset_counters(client_company_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetsApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.get_asset_counters(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetsApi->get_asset_counters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**AssetToClientAssetCountersResponseModel**](AssetToClientAssetCountersResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_manager_list**
> list[AssetToClientAssetManagerResponseModel] get_asset_manager_list(client_company_id, query_filter_type=query_filter_type, query_search_string=query_search_string, query_page=query_page, query_page_size=query_page_size)

GetAssetManagerList

assetFilterType: ClientUnset, ClientAssetsCollected, ClientPastDue, ClientDueForService, ClientOutOfService, ClientWithoutSchedule                ClientDueForService - depends on Employee Filter Preference  POST api/user/filters

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetsApi()
client_company_id = 56 # int | 
query_filter_type = 'query_filter_type_example' # str |  (optional)
query_search_string = 'query_search_string_example' # str |  (optional)
query_page = 56 # int |  (optional)
query_page_size = 56 # int |  (optional)

try:
    # GetAssetManagerList
    api_response = api_instance.get_asset_manager_list(client_company_id, query_filter_type=query_filter_type, query_search_string=query_search_string, query_page=query_page, query_page_size=query_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetsApi->get_asset_manager_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 
 **query_filter_type** | **str**|  | [optional] 
 **query_search_string** | **str**|  | [optional] 
 **query_page** | **int**|  | [optional] 
 **query_page_size** | **int**|  | [optional] 

### Return type

[**list[AssetToClientAssetManagerResponseModel]**](AssetToClientAssetManagerResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets**
> list[AssetToAssetResponseModel] get_assets(client_company_id, query_equipment_id=query_equipment_id, query_serial_number=query_serial_number, query_asset_tag=query_asset_tag, query_barcode=query_barcode, query_legacy_id=query_legacy_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientAssetsApi()
client_company_id = 56 # int | 
query_equipment_id = 'query_equipment_id_example' # str |  (optional)
query_serial_number = 'query_serial_number_example' # str |  (optional)
query_asset_tag = 'query_asset_tag_example' # str |  (optional)
query_barcode = 'query_barcode_example' # str |  (optional)
query_legacy_id = 'query_legacy_id_example' # str |  (optional)

try:
    api_response = api_instance.get_assets(client_company_id, query_equipment_id=query_equipment_id, query_serial_number=query_serial_number, query_asset_tag=query_asset_tag, query_barcode=query_barcode, query_legacy_id=query_legacy_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAssetsApi->get_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 
 **query_equipment_id** | **str**|  | [optional] 
 **query_serial_number** | **str**|  | [optional] 
 **query_asset_tag** | **str**|  | [optional] 
 **query_barcode** | **str**|  | [optional] 
 **query_legacy_id** | **str**|  | [optional] 

### Return type

[**list[AssetToAssetResponseModel]**](AssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

