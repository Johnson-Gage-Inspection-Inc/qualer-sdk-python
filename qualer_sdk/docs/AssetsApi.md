# swagger_client.AssetsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**assets_clear_collected_assets**](AssetsApi.md#assets_clear_collected_assets) | **PUT** /api/assets/collection/remove | ClearCollectedAssets(int[] assetIds)
[**assets_collect_assets**](AssetsApi.md#assets_collect_assets) | **PUT** /api/assets/collection/add | CollectAssets(int[] assetIds)
[**assets_get_all_assets**](AssetsApi.md#assets_get_all_assets) | **GET** /api/assets | 
[**assets_get_asset**](AssetsApi.md#assets_get_asset) | **GET** /api/assets/{id} | 
[**assets_get_asset_by_asset_pool**](AssetsApi.md#assets_get_asset_by_asset_pool) | **GET** /api/assets/byassetpool/{assetPoolId} | 
[**assets_get_asset_by_asset_tag**](AssetsApi.md#assets_get_asset_by_asset_tag) | **GET** /api/assets/byassettag/{assetTag} | 
[**assets_get_asset_by_attribute**](AssetsApi.md#assets_get_asset_by_attribute) | **GET** /api/assets/byattribute | 
[**assets_get_asset_by_barcode**](AssetsApi.md#assets_get_asset_by_barcode) | **GET** /api/assets/bybarcode/{barcode} | 
[**assets_get_asset_by_serial_number**](AssetsApi.md#assets_get_asset_by_serial_number) | **GET** /api/assets/byserialnumber/{serialNumber} | 
[**assets_get_asset_images**](AssetsApi.md#assets_get_asset_images) | **GET** /api/assets/{id}/images | GetAssetImages
[**assets_get_asset_manager_counters**](AssetsApi.md#assets_get_asset_manager_counters) | **GET** /api/assets/counters | GetAssetManagerCounters
[**assets_get_asset_manager_list**](AssetsApi.md#assets_get_asset_manager_list) | **GET** /api/assets/byfilter | GetAssetManagerList
[**assets_get_assets_by_equipment_id**](AssetsApi.md#assets_get_assets_by_equipment_id) | **GET** /api/assets/byequipmentid/{equipmentId} | 
[**assets_post_asset_images**](AssetsApi.md#assets_post_asset_images) | **POST** /api/assets/{id}/images | PostAssetImages
[**assets_update_asset_class**](AssetsApi.md#assets_update_asset_class) | **PUT** /api/assets/{id}/class | 
[**assets_update_asset_department**](AssetsApi.md#assets_update_asset_department) | **PUT** /api/assets/{id}/department | 
[**assets_update_asset_room**](AssetsApi.md#assets_update_asset_room) | **PUT** /api/assets/{id}/room | 
[**assets_update_room**](AssetsApi.md#assets_update_room) | **PUT** /api/assets/room | 


# **assets_clear_collected_assets**
> object assets_clear_collected_assets(asset_ids)

ClearCollectedAssets(int[] assetIds)

[123,234,567] removes assets with selected Ids                [] removes all assets from QuickCollection

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_ids = [swagger_client.list[int]()] # list[int] | 

try:
    # ClearCollectedAssets(int[] assetIds)
    api_response = api_instance.assets_clear_collected_assets(asset_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_clear_collected_assets: %s\n" % e)
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

# **assets_collect_assets**
> object assets_collect_assets(asset_ids)

CollectAssets(int[] assetIds)

[123,234,567]

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_ids = [swagger_client.list[int]()] # list[int] | 

try:
    # CollectAssets(int[] assetIds)
    api_response = api_instance.assets_collect_assets(asset_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_collect_assets: %s\n" % e)
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

# **assets_get_all_assets**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_all_assets()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()

try:
    api_response = api_instance.assets_get_all_assets()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_all_assets: %s\n" % e)
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

# **assets_get_asset**
> QualerApiModelsAssetToAssetResponseModel assets_get_asset(id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 56 # int | 

try:
    api_response = api_instance.assets_get_asset(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset: %s\n" % e)
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

# **assets_get_asset_by_asset_pool**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_asset_by_asset_pool(asset_pool_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_pool_id = 56 # int | 

try:
    api_response = api_instance.assets_get_asset_by_asset_pool(asset_pool_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_by_asset_pool: %s\n" % e)
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

# **assets_get_asset_by_asset_tag**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_asset_by_asset_tag(asset_tag)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
asset_tag = 'asset_tag_example' # str | 

try:
    api_response = api_instance.assets_get_asset_by_asset_tag(asset_tag)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_by_asset_tag: %s\n" % e)
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

# **assets_get_asset_by_attribute**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_asset_by_attribute(model_name=model_name, model_value=model_value)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
model_name = 'model_name_example' # str |  (optional)
model_value = 'model_value_example' # str |  (optional)

try:
    api_response = api_instance.assets_get_asset_by_attribute(model_name=model_name, model_value=model_value)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_by_attribute: %s\n" % e)
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

# **assets_get_asset_by_barcode**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_asset_by_barcode(barcode)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
barcode = 'barcode_example' # str | 

try:
    api_response = api_instance.assets_get_asset_by_barcode(barcode)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_by_barcode: %s\n" % e)
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

# **assets_get_asset_by_serial_number**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_asset_by_serial_number(serial_number)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
serial_number = 'serial_number_example' # str | 

try:
    api_response = api_instance.assets_get_asset_by_serial_number(serial_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_by_serial_number: %s\n" % e)
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

# **assets_get_asset_images**
> list[str] assets_get_asset_images(id)

GetAssetImages

returns list of asset image urls

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 56 # int | 

try:
    # GetAssetImages
    api_response = api_instance.assets_get_asset_images(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_images: %s\n" % e)
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

# **assets_get_asset_manager_counters**
> QualerApiModelsAssetToAssetsCountResponseModel assets_get_asset_manager_counters(model_search_string=model_search_string)

GetAssetManagerCounters

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
model_search_string = 'model_search_string_example' # str |  (optional)

try:
    # GetAssetManagerCounters
    api_response = api_instance.assets_get_asset_manager_counters(model_search_string=model_search_string)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_manager_counters: %s\n" % e)
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

# **assets_get_asset_manager_list**
> list[QualerApiModelsAssetToAssetManageResponseModel] assets_get_asset_manager_list(model_filter_type=model_filter_type, model_search_string=model_search_string, model_page=model_page, model_page_size=model_page_size)

GetAssetManagerList

filterType: Unset, DueForService, RecentlyServiced, NotServiced, RecentlyPurchased,      WarrantyExpiring, DueForReplacement, OutOfService,      PastDue, ServicePending, CollectedAssets,  WithoutSchedule, WithoutVendor,      WithoutProduct, Added, Modified, Deleted,      NoAgreement, ExpiredAgreement, AgreementUpForRenewal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
model_filter_type = 'model_filter_type_example' # str |  (optional)
model_search_string = 'model_search_string_example' # str |  (optional)
model_page = 56 # int |  (optional)
model_page_size = 56 # int |  (optional)

try:
    # GetAssetManagerList
    api_response = api_instance.assets_get_asset_manager_list(model_filter_type=model_filter_type, model_search_string=model_search_string, model_page=model_page, model_page_size=model_page_size)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_asset_manager_list: %s\n" % e)
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

# **assets_get_assets_by_equipment_id**
> list[QualerApiModelsAssetToAssetResponseModel] assets_get_assets_by_equipment_id(equipment_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
equipment_id = 'equipment_id_example' # str | 

try:
    api_response = api_instance.assets_get_assets_by_equipment_id(equipment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_get_assets_by_equipment_id: %s\n" % e)
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

# **assets_post_asset_images**
> object assets_post_asset_images(id)

PostAssetImages

returns list of asset image urls

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 56 # int | 

try:
    # PostAssetImages
    api_response = api_instance.assets_post_asset_images(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_post_asset_images: %s\n" % e)
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

# **assets_update_asset_class**
> object assets_update_asset_class(id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 56 # int | 
model = swagger_client.QualerApiModelsAssetFromUpdateAssetClassModel() # QualerApiModelsAssetFromUpdateAssetClassModel | 

try:
    api_response = api_instance.assets_update_asset_class(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_update_asset_class: %s\n" % e)
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

# **assets_update_asset_department**
> object assets_update_asset_department(id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 56 # int | 
model = swagger_client.QualerApiModelsAssetFromUpdateAssetDepartmentModel() # QualerApiModelsAssetFromUpdateAssetDepartmentModel | 

try:
    api_response = api_instance.assets_update_asset_department(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_update_asset_department: %s\n" % e)
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

# **assets_update_asset_room**
> object assets_update_asset_room(id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
id = 56 # int | 
model = swagger_client.QualerApiModelsAssetFromUpdateAssetRoomModel() # QualerApiModelsAssetFromUpdateAssetRoomModel | 

try:
    api_response = api_instance.assets_update_asset_room(id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_update_asset_room: %s\n" % e)
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

# **assets_update_room**
> object assets_update_room(model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetsApi()
model = swagger_client.QualerApiModelsAssetFromUpdateRoomModel() # QualerApiModelsAssetFromUpdateRoomModel | 

try:
    api_response = api_instance.assets_update_room(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetsApi->assets_update_room: %s\n" % e)
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

