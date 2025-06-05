# qualer_sdk.AssetsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clear_collected_assets**](AssetsApi.md#clear_collected_assets) | **PUT** /api/assets/collection/remove | ClearCollectedAssets(int[] assetIds)
[**collect_assets**](AssetsApi.md#collect_assets) | **PUT** /api/assets/collection/add | CollectAssets(int[] assetIds)
[**get_all_assets**](AssetsApi.md#get_all_assets) | **GET** /api/assets | 
[**get_asset**](AssetsApi.md#get_asset) | **GET** /api/assets/{id} | 
[**get_asset_by_asset_pool**](AssetsApi.md#get_asset_by_asset_pool) | **GET** /api/assets/byassetpool/{assetPoolId} | 
[**get_asset_by_asset_tag**](AssetsApi.md#get_asset_by_asset_tag) | **GET** /api/assets/byassettag/{assetTag} | 
[**get_asset_by_attribute**](AssetsApi.md#get_asset_by_attribute) | **GET** /api/assets/byattribute | 
[**get_asset_by_barcode**](AssetsApi.md#get_asset_by_barcode) | **GET** /api/assets/bybarcode/{barcode} | 
[**get_asset_by_serial_number**](AssetsApi.md#get_asset_by_serial_number) | **GET** /api/assets/byserialnumber/{serialNumber} | 
[**get_asset_images**](AssetsApi.md#get_asset_images) | **GET** /api/assets/{id}/images | GetAssetImages
[**get_asset_manager_counters**](AssetsApi.md#get_asset_manager_counters) | **GET** /api/assets/counters | GetAssetManagerCounters
[**get_asset_manager_list**](AssetsApi.md#get_asset_manager_list) | **GET** /api/assets/byfilter | GetAssetManagerList
[**get_assets_by_equipment_id**](AssetsApi.md#get_assets_by_equipment_id) | **GET** /api/assets/byequipmentid/{equipmentId} | 
[**post_asset_images**](AssetsApi.md#post_asset_images) | **POST** /api/assets/{id}/images | PostAssetImages
[**update_asset_class**](AssetsApi.md#update_asset_class) | **PUT** /api/assets/{id}/class | 
[**update_asset_department**](AssetsApi.md#update_asset_department) | **PUT** /api/assets/{id}/department | 
[**update_asset_room**](AssetsApi.md#update_asset_room) | **PUT** /api/assets/{id}/room | 
[**update_room**](AssetsApi.md#update_room) | **PUT** /api/assets/room | 


# **clear_collected_assets**
> object clear_collected_assets(asset_ids)

ClearCollectedAssets(int[] assetIds)

[123,234,567] removes assets with selected Ids                [] removes all assets from QuickCollection

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
asset_ids = [qualer_sdk.list[int]()] # list[int] | 

try:
    # ClearCollectedAssets(int[] assetIds)
    api_response = api_instance.clear_collected_assets(asset_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->clear_collected_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **list[int]**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collect_assets**
> object collect_assets(asset_ids)

CollectAssets(int[] assetIds)

[123,234,567]

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
asset_ids = [qualer_sdk.list[int]()] # list[int] | 

try:
    # CollectAssets(int[] assetIds)
    api_response = api_instance.collect_assets(asset_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->collect_assets: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_ids** | **list[int]**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_assets**
> list[QualerApiModelsAssetToAssetResponseModel] get_all_assets()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()

try:
    api_response = api_instance.get_all_assets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_all_assets: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset**
> QualerApiModelsAssetToAssetResponseModel get_asset(id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
id = 56 # int | 

try:
    api_response = api_instance.get_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**QualerApiModelsAssetToAssetResponseModel**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_asset_pool**
> list[QualerApiModelsAssetToAssetResponseModel] get_asset_by_asset_pool(asset_pool_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
asset_pool_id = 56 # int | 

try:
    api_response = api_instance.get_asset_by_asset_pool(asset_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_by_asset_pool: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_pool_id** | **int**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_asset_tag**
> list[QualerApiModelsAssetToAssetResponseModel] get_asset_by_asset_tag(asset_tag)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
asset_tag = 'asset_tag_example' # str | 

try:
    api_response = api_instance.get_asset_by_asset_tag(asset_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_by_asset_tag: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_tag** | **str**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_attribute**
> list[QualerApiModelsAssetToAssetResponseModel] get_asset_by_attribute(model_name=model_name, model_value=model_value)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
model_name = 'model_name_example' # str |  (optional)
model_value = 'model_value_example' # str |  (optional)

try:
    api_response = api_instance.get_asset_by_attribute(model_name=model_name, model_value=model_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_by_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_name** | **str**|  | [optional] 
 **model_value** | **str**|  | [optional] 

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_barcode**
> list[QualerApiModelsAssetToAssetResponseModel] get_asset_by_barcode(barcode)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
barcode = 'barcode_example' # str | 

try:
    api_response = api_instance.get_asset_by_barcode(barcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_by_barcode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **barcode** | **str**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_by_serial_number**
> list[QualerApiModelsAssetToAssetResponseModel] get_asset_by_serial_number(serial_number)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
serial_number = 'serial_number_example' # str | 

try:
    api_response = api_instance.get_asset_by_serial_number(serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_by_serial_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **serial_number** | **str**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_images**
> list[str] get_asset_images(id)

GetAssetImages

returns list of asset image urls

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
id = 56 # int | 

try:
    # GetAssetImages
    api_response = api_instance.get_asset_images(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_manager_counters**
> QualerApiModelsAssetToAssetsCountResponseModel get_asset_manager_counters(model_search_string=model_search_string)

GetAssetManagerCounters

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
model_search_string = 'model_search_string_example' # str |  (optional)

try:
    # GetAssetManagerCounters
    api_response = api_instance.get_asset_manager_counters(model_search_string=model_search_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_manager_counters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_search_string** | **str**|  | [optional] 

### Return type

[**QualerApiModelsAssetToAssetsCountResponseModel**](QualerApiModelsAssetToAssetsCountResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_manager_list**
> list[QualerApiModelsAssetToAssetManageResponseModel] get_asset_manager_list(model_filter_type=model_filter_type, model_search_string=model_search_string, model_page=model_page, model_page_size=model_page_size)

GetAssetManagerList

filterType: Unset, DueForService, RecentlyServiced, NotServiced, RecentlyPurchased,      WarrantyExpiring, DueForReplacement, OutOfService,      PastDue, ServicePending, CollectedAssets,  WithoutSchedule, WithoutVendor,      WithoutProduct, Added, Modified, Deleted,      NoAgreement, ExpiredAgreement, AgreementUpForRenewal

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
model_filter_type = 'model_filter_type_example' # str |  (optional)
model_search_string = 'model_search_string_example' # str |  (optional)
model_page = 56 # int |  (optional)
model_page_size = 56 # int |  (optional)

try:
    # GetAssetManagerList
    api_response = api_instance.get_asset_manager_list(model_filter_type=model_filter_type, model_search_string=model_search_string, model_page=model_page, model_page_size=model_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_asset_manager_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_filter_type** | **str**|  | [optional] 
 **model_search_string** | **str**|  | [optional] 
 **model_page** | **int**|  | [optional] 
 **model_page_size** | **int**|  | [optional] 

### Return type

[**list[QualerApiModelsAssetToAssetManageResponseModel]**](QualerApiModelsAssetToAssetManageResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assets_by_equipment_id**
> list[QualerApiModelsAssetToAssetResponseModel] get_assets_by_equipment_id(equipment_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
equipment_id = 'equipment_id_example' # str | 

try:
    api_response = api_instance.get_assets_by_equipment_id(equipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->get_assets_by_equipment_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **equipment_id** | **str**|  | 

### Return type

[**list[QualerApiModelsAssetToAssetResponseModel]**](QualerApiModelsAssetToAssetResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **post_asset_images**
> object post_asset_images(id)

PostAssetImages

returns list of asset image urls

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
id = 56 # int | 

try:
    # PostAssetImages
    api_response = api_instance.post_asset_images(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->post_asset_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_class**
> object update_asset_class(id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
id = 56 # int | 
model = qualer_sdk.QualerApiModelsAssetFromUpdateAssetClassModel() # QualerApiModelsAssetFromUpdateAssetClassModel | 

try:
    api_response = api_instance.update_asset_class(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->update_asset_class: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model** | [**QualerApiModelsAssetFromUpdateAssetClassModel**](QualerApiModelsAssetFromUpdateAssetClassModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_department**
> object update_asset_department(id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
id = 56 # int | 
model = qualer_sdk.QualerApiModelsAssetFromUpdateAssetDepartmentModel() # QualerApiModelsAssetFromUpdateAssetDepartmentModel | 

try:
    api_response = api_instance.update_asset_department(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->update_asset_department: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model** | [**QualerApiModelsAssetFromUpdateAssetDepartmentModel**](QualerApiModelsAssetFromUpdateAssetDepartmentModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_asset_room**
> object update_asset_room(id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
id = 56 # int | 
model = qualer_sdk.QualerApiModelsAssetFromUpdateAssetRoomModel() # QualerApiModelsAssetFromUpdateAssetRoomModel | 

try:
    api_response = api_instance.update_asset_room(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->update_asset_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **model** | [**QualerApiModelsAssetFromUpdateAssetRoomModel**](QualerApiModelsAssetFromUpdateAssetRoomModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_room**
> object update_room(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetsApi()
model = qualer_sdk.QualerApiModelsAssetFromUpdateRoomModel() # QualerApiModelsAssetFromUpdateRoomModel | 

try:
    api_response = api_instance.update_room(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->update_room: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsAssetFromUpdateRoomModel**](QualerApiModelsAssetFromUpdateRoomModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

