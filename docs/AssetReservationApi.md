# qualer_sdk.AssetReservationApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**close**](AssetReservationApi.md#close) | **PUT** /api/assetsreservations/close | 
[**get**](AssetReservationApi.md#get) | **GET** /api/assetsreservations | 
[**upsert**](AssetReservationApi.md#upsert) | **PUT** /api/assetsreservations | 


# **close**
> object close(model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetReservationApi()
model_asset_id = 56 # int |  (optional)
model_area_id = 56 # int |  (optional)
model_product_id = 56 # int |  (optional)
model_serial_number = 'model_serial_number_example' # str |  (optional)
model_asset_tag = 'model_asset_tag_example' # str |  (optional)
model_reservation_id = 56 # int |  (optional)

try:
    api_response = api_instance.close(model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetReservationApi->close: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_asset_id** | **int**|  | [optional] 
 **model_area_id** | **int**|  | [optional] 
 **model_product_id** | **int**|  | [optional] 
 **model_serial_number** | **str**|  | [optional] 
 **model_asset_tag** | **str**|  | [optional] 
 **model_reservation_id** | **int**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> list[AssetReservationToAssetReservationResponse] get(model_from=model_from, model_to=model_to, model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetReservationApi()
model_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
model_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
model_asset_id = 56 # int |  (optional)
model_area_id = 56 # int |  (optional)
model_product_id = 56 # int |  (optional)
model_serial_number = 'model_serial_number_example' # str |  (optional)
model_asset_tag = 'model_asset_tag_example' # str |  (optional)
model_reservation_id = 56 # int |  (optional)

try:
    api_response = api_instance.get(model_from=model_from, model_to=model_to, model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetReservationApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_from** | **datetime**|  | [optional] 
 **model_to** | **datetime**|  | [optional] 
 **model_asset_id** | **int**|  | [optional] 
 **model_area_id** | **int**|  | [optional] 
 **model_product_id** | **int**|  | [optional] 
 **model_serial_number** | **str**|  | [optional] 
 **model_asset_tag** | **str**|  | [optional] 
 **model_reservation_id** | **int**|  | [optional] 

### Return type

[**list[AssetReservationToAssetReservationResponse]**](AssetReservationToAssetReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upsert**
> AssetReservationToUpsertAssetReservationResponse upsert(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.AssetReservationApi()
model = qualer_sdk.AssetReservationFromUpsertAssetReservationModel() # AssetReservationFromUpsertAssetReservationModel | 

try:
    api_response = api_instance.upsert(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetReservationApi->upsert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**AssetReservationFromUpsertAssetReservationModel**](AssetReservationFromUpsertAssetReservationModel.md)|  | 

### Return type

[**AssetReservationToUpsertAssetReservationResponse**](AssetReservationToUpsertAssetReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

