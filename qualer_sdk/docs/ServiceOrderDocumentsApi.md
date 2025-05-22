# qualer_sdk.ServiceOrderDocumentsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_document**](ServiceOrderDocumentsApi.md#get_document) | **GET** /api/service/workorders/documents/{guid} | Retrieve work order document by Unique Id
[**get_document_0**](ServiceOrderDocumentsApi.md#get_document_0) | **GET** /api/wd/{guid} | Retrieve work order document by Unique Id
[**get_document_list**](ServiceOrderDocumentsApi.md#get_document_list) | **GET** /api/service/workorders/documents/list | Retrieve work order documents
[**get_documents**](ServiceOrderDocumentsApi.md#get_documents) | **GET** /api/service/workorders/{serviceOrderId}/documents | Retrieve work order documents
[**get_documents_list**](ServiceOrderDocumentsApi.md#get_documents_list) | **GET** /api/service/workorders/{serviceOrderId}/documents/list | 
[**upload_documents**](ServiceOrderDocumentsApi.md#upload_documents) | **POST** /api/service/workorders/{serviceOrderId}/documents | 


# **get_document**
> object get_document(guid)

Retrieve work order document by Unique Id

Sample request:                GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9                GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderDocumentsApi()
guid = 'guid_example' # str | Document unique id

try:
    # Retrieve work order document by Unique Id
    api_response = api_instance.get_document(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderDocumentsApi->get_document: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| Document unique id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_0**
> object get_document_0(guid)

Retrieve work order document by Unique Id

Sample request:                GET api/service/workorders/documents/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9                GET api/wd/FE6B21DC-8061-46FF-AAB8-12C2030FE4B9

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderDocumentsApi()
guid = 'guid_example' # str | Document unique id

try:
    # Retrieve work order document by Unique Id
    api_response = api_instance.get_document_0(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderDocumentsApi->get_document_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | [**str**](.md)| Document unique id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_document_list**
> list[QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse] get_document_list(_from, to, report_type=report_type, service_order_id=service_order_id)

Retrieve work order documents

Sample request:                GET /api/service/workorders/documents/list                GET /api/service/workorders/documents/list?status=reportType                GET /api/service/workorders/documents/list?from=2020-12-01T10:11:12&amp;to=2021-01-01T10:11:12&amp;reportType=OrderInvoice&amp;ServiceOrderId=1                reportType:<br />  Unset = 0,<br />  AssetSummary = 1,<br />  AssetLabel = 11,<br />  AssetDetail = 2,<br />  AssetCertificate = 21,<br />  OrderSummary / ServiceOrderSummary = 3,<br />  OrderInvoice / ServiceOrderInvoice = 31,<br />  OrderEstimate / ServiceOrderEstimate = 32,<br />  Dashboard = 4,<br />  OrderDetail / ServiceOrderDetail = 5,<br />  OrderCertificate / ServiceOrderCertificate = 5<br />

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderDocumentsApi()
_from = '2013-10-20T19:20:30+01:00' # datetime | Retrieve documents where CreatedOnUtc greater than From parameter
to = '2013-10-20T19:20:30+01:00' # datetime | Retrieve documents where CreatedOnUtc less than To parameter
report_type = 'report_type_example' # str | Retrieve documents given types (Optional) (optional)
service_order_id = 56 # int | Retrieve documents by given service order id (Optional) (optional)

try:
    # Retrieve work order documents
    api_response = api_instance.get_document_list(_from, to, report_type=report_type, service_order_id=service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderDocumentsApi->get_document_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **datetime**| Retrieve documents where CreatedOnUtc greater than From parameter | 
 **to** | **datetime**| Retrieve documents where CreatedOnUtc less than To parameter | 
 **report_type** | **str**| Retrieve documents given types (Optional) | [optional] 
 **service_order_id** | **int**| Retrieve documents by given service order id (Optional) | [optional] 

### Return type

[**list[QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse]**](QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_documents**
> object get_documents(service_order_id, model_file_name=model_file_name)

Retrieve work order documents

Sample request:                GET api/service/workorders/1000/documents

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderDocumentsApi()
service_order_id = 56 # int | 
model_file_name = 'model_file_name_example' # str |  (optional)

try:
    # Retrieve work order documents
    api_response = api_instance.get_documents(service_order_id, model_file_name=model_file_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderDocumentsApi->get_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
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
> list[QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse] get_documents_list(service_order_id, model_report_type=model_report_type)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderDocumentsApi()
service_order_id = 56 # int | 
model_report_type = 'model_report_type_example' # str |  (optional)

try:
    api_response = api_instance.get_documents_list(service_order_id, model_report_type=model_report_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderDocumentsApi->get_documents_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model_report_type** | **str**|  | [optional] 

### Return type

[**list[QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse]**](QualerApiModelsServiceOrderDocumentsToCompanyOrderControlledDocumentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_documents**
> object upload_documents(service_order_id, model_report_type=model_report_type, model_is_private=model_is_private)



reportType:<br />  assetsummary, assetlabel, assetdetail, assetcertificate,<br />  ordersummary / serviceordersummary,<br />  orderinvoice / serviceorderinvoice,<br />  orderestimate / serviceorderestimate,<br />  orderdetail / serviceorderdetail,<br />  ordercertificate / serviceordercertificate,<br />  general

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderDocumentsApi()
service_order_id = 56 # int | 
model_report_type = 'model_report_type_example' # str |  (optional)
model_is_private = true # bool |  (optional)

try:
    # 
    api_response = api_instance.upload_documents(service_order_id, model_report_type=model_report_type, model_is_private=model_is_private)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderDocumentsApi->upload_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
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

