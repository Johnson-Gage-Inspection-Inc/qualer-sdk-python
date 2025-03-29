# swagger_client.AssetReservationApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**asset_reservation_close**](AssetReservationApi.md#asset_reservation_close) | **PUT** /api/assetsreservations/close | 
[**asset_reservation_get**](AssetReservationApi.md#asset_reservation_get) | **GET** /api/assetsreservations | 
[**asset_reservation_upsert**](AssetReservationApi.md#asset_reservation_upsert) | **PUT** /api/assetsreservations | 

# **asset_reservation_close**
> object asset_reservation_close(model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetReservationApi()
model_asset_id = 56 # int |  (optional)
model_area_id = 56 # int |  (optional)
model_product_id = 56 # int |  (optional)
model_serial_number = 'model_serial_number_example' # str |  (optional)
model_asset_tag = 'model_asset_tag_example' # str |  (optional)
model_reservation_id = 56 # int |  (optional)

try:
    api_response = api_instance.asset_reservation_close(model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetReservationApi->asset_reservation_close: %s\n" % e)
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

# **asset_reservation_get**
> list[QualerApiModelsAssetReservationToAssetReservationResponse] asset_reservation_get(model_from=model_from, model_to=model_to, model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetReservationApi()
model_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
model_to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
model_asset_id = 56 # int |  (optional)
model_area_id = 56 # int |  (optional)
model_product_id = 56 # int |  (optional)
model_serial_number = 'model_serial_number_example' # str |  (optional)
model_asset_tag = 'model_asset_tag_example' # str |  (optional)
model_reservation_id = 56 # int |  (optional)

try:
    api_response = api_instance.asset_reservation_get(model_from=model_from, model_to=model_to, model_asset_id=model_asset_id, model_area_id=model_area_id, model_product_id=model_product_id, model_serial_number=model_serial_number, model_asset_tag=model_asset_tag, model_reservation_id=model_reservation_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetReservationApi->asset_reservation_get: %s\n" % e)
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

[**list[QualerApiModelsAssetReservationToAssetReservationResponse]**](QualerApiModelsAssetReservationToAssetReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **asset_reservation_upsert**
> QualerApiModelsAssetReservationToUpsertAssetReservationResponse asset_reservation_upsert(body)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AssetReservationApi()
body = swagger_client.QualerApiModelsAssetReservationFromUpsertAssetReservationModel() # QualerApiModelsAssetReservationFromUpsertAssetReservationModel | 

try:
    api_response = api_instance.asset_reservation_upsert(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssetReservationApi->asset_reservation_upsert: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsAssetReservationFromUpsertAssetReservationModel**](QualerApiModelsAssetReservationFromUpsertAssetReservationModel.md)|  | 

### Return type

[**QualerApiModelsAssetReservationToUpsertAssetReservationResponse**](QualerApiModelsAssetReservationToUpsertAssetReservationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

