# swagger_client.ServiceOrderItemsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_items_add_work_items**](ServiceOrderItemsApi.md#service_order_items_add_work_items) | **PUT** /api/service/workorders/{serviceOrderId}/workitems | Add work items
[**service_order_items_delete_work_item_image**](ServiceOrderItemsApi.md#service_order_items_delete_work_item_image) | **DELETE** /api/service/workitems/{workItemId}/images/{imageName} | 
[**service_order_items_get_work_item**](ServiceOrderItemsApi.md#service_order_items_get_work_item) | **GET** /api/service/workitems/{workItemId} | 
[**service_order_items_get_work_item_charges**](ServiceOrderItemsApi.md#service_order_items_get_work_item_charges) | **GET** /api/service/workitems/{workItemId}/charges | 
[**service_order_items_get_work_item_image**](ServiceOrderItemsApi.md#service_order_items_get_work_item_image) | **GET** /api/service/workitems/{workItemId}/images/{imageName} | 
[**service_order_items_get_work_item_images**](ServiceOrderItemsApi.md#service_order_items_get_work_item_images) | **GET** /api/service/workitems/{workItemId}/images | 
[**service_order_items_get_work_items**](ServiceOrderItemsApi.md#service_order_items_get_work_items) | **GET** /api/service/workorders/{serviceOrderId}/workitems | 
[**service_order_items_get_work_items_0**](ServiceOrderItemsApi.md#service_order_items_get_work_items_0) | **GET** /api/service/workitems | Retrieve work items
[**service_order_items_put_charges**](ServiceOrderItemsApi.md#service_order_items_put_charges) | **PUT** /api/service/workitems/{workItemId}/charges | Apply Service Order Item Charges
[**service_order_items_set_work_item**](ServiceOrderItemsApi.md#service_order_items_set_work_item) | **PUT** /api/service/workitems/{workItemId} | Update work item
[**service_order_items_upload_work_item_images**](ServiceOrderItemsApi.md#service_order_items_upload_work_item_images) | **POST** /api/service/workitems/{workItemId}/images | 


# **service_order_items_add_work_items**
> QualerApiModelsServiceOrdersToAssetAddResultResponseModel service_order_items_add_work_items(service_order_id, model)

Add work items

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
service_order_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromAddWorkItemsModel() # QualerApiModelsServiceOrdersFromAddWorkItemsModel | 

try:
    # Add work items
    api_response = api_instance.service_order_items_add_work_items(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_add_work_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromAddWorkItemsModel**](QualerApiModelsServiceOrdersFromAddWorkItemsModel.md)|  | 

### Return type

[**QualerApiModelsServiceOrdersToAssetAddResultResponseModel**](QualerApiModelsServiceOrdersToAssetAddResultResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_delete_work_item_image**
> object service_order_items_delete_work_item_image(work_item_id, image_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 
image_name = 'image_name_example' # str | 

try:
    api_response = api_instance.service_order_items_delete_work_item_image(work_item_id, image_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_delete_work_item_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **image_name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_get_work_item**
> QualerApiModelsServiceOrdersToClientOrderItemResponseModel service_order_items_get_work_item(work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_items_get_work_item(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_get_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

[**QualerApiModelsServiceOrdersToClientOrderItemResponseModel**](QualerApiModelsServiceOrdersToClientOrderItemResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_get_work_item_charges**
> object service_order_items_get_work_item_charges(work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_items_get_work_item_charges(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_get_work_item_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_get_work_item_image**
> object service_order_items_get_work_item_image(work_item_id, image_name)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 
image_name = 'image_name_example' # str | 

try:
    api_response = api_instance.service_order_items_get_work_item_image(work_item_id, image_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_get_work_item_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **image_name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_get_work_item_images**
> list[str] service_order_items_get_work_item_images(work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_items_get_work_item_images(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_get_work_item_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

**list[str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_get_work_items**
> list[QualerApiModelsServiceOrdersToClientOrderItemResponseModel] service_order_items_get_work_items(service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_items_get_work_items(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_get_work_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]**](QualerApiModelsServiceOrdersToClientOrderItemResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_get_work_items_0**
> list[QualerApiModelsServiceOrdersToClientOrderItemResponseModel] service_order_items_get_work_items_0(status=status, company_id=company_id, _from=_from, to=to, work_item_number=work_item_number, asset_search=asset_search)

Retrieve work items

Sample request:                GET /api/service/workitems                GET /api/service/workitems?status=pending                GET /api/service/workitems?&amp;status=pending,delayed&amp;companyId=10&amp;from=2010-11-15T10:11:12&amp;to=2011-11-15T10:11:12&amp;workItemNumber=0629-000032-02

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
status = 'status_example' # str | Comma separated list of work item statuses: Pending, Completed, Delayed, InProgress, Withdrawn (optional)
company_id = 56 # int | Filter by Client Company ID (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Items where CreatedOnUtc greater than From parameter (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Items where CreatedOnUtc less than To parameter (optional)
work_item_number = 'work_item_number_example' # str | Filter by CustomOrderNumber or CertificateNumber (optional)
asset_search = 'asset_search_example' # str | Filter by asset Search keywords: SerialNumber, EquipmentId, AssetTag, AssetUser, LegacyId, AssetName, AssetDescription, ManufacturerPartNumber (optional)

try:
    # Retrieve work items
    api_response = api_instance.service_order_items_get_work_items_0(status=status, company_id=company_id, _from=_from, to=to, work_item_number=work_item_number, asset_search=asset_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_get_work_items_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Comma separated list of work item statuses: Pending, Completed, Delayed, InProgress, Withdrawn | [optional] 
 **company_id** | **int**| Filter by Client Company ID | [optional] 
 **_from** | **datetime**| Retrieve Work Items where CreatedOnUtc greater than From parameter | [optional] 
 **to** | **datetime**| Retrieve Work Items where CreatedOnUtc less than To parameter | [optional] 
 **work_item_number** | **str**| Filter by CustomOrderNumber or CertificateNumber | [optional] 
 **asset_search** | **str**| Filter by asset Search keywords: SerialNumber, EquipmentId, AssetTag, AssetUser, LegacyId, AssetName, AssetDescription, ManufacturerPartNumber | [optional] 

### Return type

[**list[QualerApiModelsServiceOrdersToClientOrderItemResponseModel]**](QualerApiModelsServiceOrdersToClientOrderItemResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_put_charges**
> object service_order_items_put_charges(work_item_id, model)

Apply Service Order Item Charges

Allowed Names:      OverrideServiceTotal,      OverridePartsTotal,      OverrideRepairsTotal

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromItemChargeUpdateModel() # QualerApiModelsServiceOrdersFromItemChargeUpdateModel | 

try:
    # Apply Service Order Item Charges
    api_response = api_instance.service_order_items_put_charges(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_put_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromItemChargeUpdateModel**](QualerApiModelsServiceOrdersFromItemChargeUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_set_work_item**
> object service_order_items_set_work_item(work_item_id, model)

Update work item

WorkStatus:  Pending = 0  InProgress = 1  Completed = 2  Delayed = 3  Withdrawn = 4  Locked = 5<br />  AsFoundCheck/AsLeftCheck (ChecklistResultStatus):  NotServiced = 0,  Fail = 1,  Pass = 2<br />  ResultStatus/AsFoundResult/AsLeftResult (ServiceResultStatus):  NotAvailable = 0,  Fail = 1,  FailAmbiguous = 10,  FailSignificant = 11,  Pass = 2,  PassAmbiguous = 20,  PassAdjustment = 21,  Done = 22,

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromOrderItemUpdateModel() # QualerApiModelsServiceOrdersFromOrderItemUpdateModel | 

try:
    # Update work item
    api_response = api_instance.service_order_items_set_work_item(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_set_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromOrderItemUpdateModel**](QualerApiModelsServiceOrdersFromOrderItemUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_items_upload_work_item_images**
> object service_order_items_upload_work_item_images(work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_items_upload_work_item_images(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->service_order_items_upload_work_item_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

