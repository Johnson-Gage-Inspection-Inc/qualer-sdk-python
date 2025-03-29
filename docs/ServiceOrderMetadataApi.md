# swagger_client.ServiceOrderMetadataApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_metadata_create**](ServiceOrderMetadataApi.md#service_order_metadata_create) | **POST** /api/service/workorders/{serviceOrderId}/metadata | Create metadata
[**service_order_metadata_delete**](ServiceOrderMetadataApi.md#service_order_metadata_delete) | **DELETE** /api/service/workorders/{serviceOrderId}/metadata/{serviceOrderMetadataId} | Delete metadata
[**service_order_metadata_get**](ServiceOrderMetadataApi.md#service_order_metadata_get) | **GET** /api/service/workorders/{serviceOrderId}/metadata | Get list of metadata
[**service_order_metadata_update**](ServiceOrderMetadataApi.md#service_order_metadata_update) | **PUT** /api/service/workorders/{serviceOrderId}/metadata | Update metadata

# **service_order_metadata_create**
> object service_order_metadata_create(body, service_order_id)

Create metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderMetadataApi()
body = swagger_client.QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel() # QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel | 
service_order_id = 56 # int | 

try:
    # Create metadata
    api_response = api_instance.service_order_metadata_create(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->service_order_metadata_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel**](QualerApiModelsServiceOrdersFromServiceOrderMetadataCreateModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_metadata_delete**
> object service_order_metadata_delete(service_order_id, service_order_metadata_id)

Delete metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderMetadataApi()
service_order_id = 56 # int | 
service_order_metadata_id = 56 # int | 

try:
    # Delete metadata
    api_response = api_instance.service_order_metadata_delete(service_order_id, service_order_metadata_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->service_order_metadata_delete: %s\n" % e)
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

# **service_order_metadata_get**
> object service_order_metadata_get(service_order_id)

Get list of metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderMetadataApi()
service_order_id = 56 # int | 

try:
    # Get list of metadata
    api_response = api_instance.service_order_metadata_get(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->service_order_metadata_get: %s\n" % e)
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

# **service_order_metadata_update**
> object service_order_metadata_update(body, service_order_id)

Update metadata

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderMetadataApi()
body = swagger_client.QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel() # QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel | 
service_order_id = 56 # int | 

try:
    # Update metadata
    api_response = api_instance.service_order_metadata_update(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderMetadataApi->service_order_metadata_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel**](QualerApiModelsServiceOrdersFromServiceOrderMetadataUpdateModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

