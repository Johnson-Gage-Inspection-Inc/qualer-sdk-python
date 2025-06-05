# qualer_sdk.ServiceOrderMetadataApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ServiceOrderMetadataApi.md#create) | **POST** /api/service/workorders/{serviceOrderId}/metadata | Create metadata
[**delete**](ServiceOrderMetadataApi.md#delete) | **DELETE** /api/service/workorders/{serviceOrderId}/metadata/{serviceOrderMetadataId} | Delete metadata
[**get**](ServiceOrderMetadataApi.md#get) | **GET** /api/service/workorders/{serviceOrderId}/metadata | Get list of metadata
[**update**](ServiceOrderMetadataApi.md#update) | **PUT** /api/service/workorders/{serviceOrderId}/metadata | Update metadata


# **create**
> object create(service_order_id, model)

Create metadata

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderMetadataApi()
service_order_id = 56 # int | 
model = qualer_sdk.QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel() # QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel | 

try:
    # Create metadata
    api_response = api_instance.create(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel**](QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete**
> object delete(service_order_id, service_order_metadata_id)

Delete metadata

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderMetadataApi()
service_order_id = 56 # int | 
service_order_metadata_id = 56 # int | 

try:
    # Delete metadata
    api_response = api_instance.delete(service_order_id, service_order_metadata_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **service_order_metadata_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> object get(service_order_id)

Get list of metadata

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderMetadataApi()
service_order_id = 56 # int | 

try:
    # Get list of metadata
    api_response = api_instance.get(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(service_order_id, model)

Update metadata

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderMetadataApi()
service_order_id = 56 # int | 
model = qualer_sdk.QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel() # QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel | 

try:
    # Update metadata
    api_response = api_instance.update(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel**](QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

