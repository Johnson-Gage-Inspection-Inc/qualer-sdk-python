# qualer_sdk.ServiceOrderItemDocumentsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document_list**](ServiceOrderItemDocumentsApi.md#get_document_list) | **GET** /api/service/workitems/documents/list | Retrieve work order documents
[**get_documents**](ServiceOrderItemDocumentsApi.md#get_documents) | **GET** /api/service/workitems/{serviceOrderItemId}/documents | Retrieve work order documents
[**get_documents_list**](ServiceOrderItemDocumentsApi.md#get_documents_list) | **GET** /api/service/workitems/{serviceOrderItemId}/documents/list | 
[**upload_documents**](ServiceOrderItemDocumentsApi.md#upload_documents) | **POST** /api/service/workitems/{serviceOrderItemId}/documents | 


# **get_document_list**
> list[ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse] get_document_list(_from, to, report_type=report_type, service_order_item_id=service_order_item_id)

Retrieve work order documents

Sample request:                GET /api/service/workitems/documents/list                GET /api/service/workitems/documents/list?status=reportType                GET /api/service/workitems/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderItemId=1                reportType:<br />  Unset = 0,<br />  AssetSummary = 1,<br />  AssetLabel = 11,<br />  AssetDetail = 2,<br />  AssetCertificate = 21,<br />  OrderSummary / ServiceOrderSummary = 3,<br />  OrderInvoice / ServiceOrderInvoice = 31,<br />  OrderEstimate / ServiceOrderEstimate = 32,<br />  Dashboard = 4,<br />  OrderDetail / ServiceOrderDetail = 5,<br />  OrderCertificate / ServiceOrderCertificate = 5<br />

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemDocumentsApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Retrieve documents where CreatedOnUtc greater than From parameter
to = '2013-10-20T19:20:30+01:00' # datetime | Retrieve documents where CreatedOnUtc less than To parameter
report_type = 'report_type_example' # str | Retrieve documents given types (Optional) (optional)
service_order_item_id = 56 # int | Retrieve documents by given service order item id (Optional) (optional)

try:
    # Retrieve work order documents
    api_response = api_instance.get_document_list(_from, to, report_type=report_type, service_order_item_id=service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemDocumentsApi->get_document_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Retrieve documents where CreatedOnUtc greater than From parameter | 
 **to** | **datetime**| Retrieve documents where CreatedOnUtc less than To parameter | 
 **report_type** | **str**| Retrieve documents given types (Optional) | [optional] 
 **service_order_item_id** | **int**| Retrieve documents by given service order item id (Optional) | [optional] 

### Return type

[**list[ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse]**](ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> object get_documents(service_order_item_id, model_file_name=model_file_name)

Retrieve work order documents

Sample request:                GET api/service/workitems/1000/documents

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemDocumentsApi()
service_order_item_id = 56 # int | Retrieve documents where CreatedOnUtc greater than From parameter
model_file_name = 'model_file_name_example' # str |  (optional)

try:
    # Retrieve work order documents
    api_response = api_instance.get_documents(service_order_item_id, model_file_name=model_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemDocumentsApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**| Retrieve documents where CreatedOnUtc greater than From parameter | 
 **model_file_name** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents_list**
> list[ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse] get_documents_list(service_order_item_id, model_report_type=model_report_type)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemDocumentsApi()
service_order_item_id = 56 # int | 
model_report_type = 'model_report_type_example' # str |  (optional)

try:
    api_response = api_instance.get_documents_list(service_order_item_id, model_report_type=model_report_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemDocumentsApi->get_documents_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 
 **model_report_type** | **str**|  | [optional] 

### Return type

[**list[ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse]**](ServiceOrderDocumentsToCompanyOrderItemControlledDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_documents**
> object upload_documents(service_order_item_id, model_report_type=model_report_type, model_is_private=model_is_private)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemDocumentsApi()
service_order_item_id = 56 # int | 
model_report_type = 'model_report_type_example' # str |  (optional)
model_is_private = true # bool |  (optional)

try:
    api_response = api_instance.upload_documents(service_order_item_id, model_report_type=model_report_type, model_is_private=model_is_private)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemDocumentsApi->upload_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 
 **model_report_type** | **str**|  | [optional] 
 **model_is_private** | **bool**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

