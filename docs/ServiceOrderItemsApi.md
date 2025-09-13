# qualer_sdk.ServiceOrderItemsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_work_items**](ServiceOrderItemsApi.md#add_work_items) | **PUT** /api/service/workorders/{serviceOrderId}/workitems | Add work items
[**delete_work_item_image**](ServiceOrderItemsApi.md#delete_work_item_image) | **DELETE** /api/service/workitems/{workItemId}/images/{imageName} | 
[**get_work_item**](ServiceOrderItemsApi.md#get_work_item) | **GET** /api/service/workitems/{workItemId} | 
[**get_work_item_charges**](ServiceOrderItemsApi.md#get_work_item_charges) | **GET** /api/service/workitems/{workItemId}/charges | 
[**get_work_item_image**](ServiceOrderItemsApi.md#get_work_item_image) | **GET** /api/service/workitems/{workItemId}/images/{imageName} | 
[**get_work_item_images**](ServiceOrderItemsApi.md#get_work_item_images) | **GET** /api/service/workitems/{workItemId}/images | 
[**get_work_items**](ServiceOrderItemsApi.md#get_work_items) | **GET** /api/service/workorders/{serviceOrderId}/workitems | 
[**get_work_items_0**](ServiceOrderItemsApi.md#get_work_items_0) | **GET** /api/service/workitems | Retrieve work items
[**put_charges**](ServiceOrderItemsApi.md#put_charges) | **PUT** /api/service/workitems/{workItemId}/charges | Apply Service Order Item Charges
[**set_work_item**](ServiceOrderItemsApi.md#set_work_item) | **PUT** /api/service/workitems/{workItemId} | Update work item
[**upload_work_item_images**](ServiceOrderItemsApi.md#upload_work_item_images) | **POST** /api/service/workitems/{workItemId}/images | 


# **add_work_items**
> ServiceOrdersToAssetAddResultResponseModel add_work_items(service_order_id, model)

Add work items

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
service_order_id = 56 # int | 
model = qualer_sdk.ServiceOrdersFromAddWorkItemsModel() # ServiceOrdersFromAddWorkItemsModel | 

try:
    # Add work items
    api_response = api_instance.add_work_items(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->add_work_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**ServiceOrdersFromAddWorkItemsModel**](ServiceOrdersFromAddWorkItemsModel.md)|  | 

### Return type

[**ServiceOrdersToAssetAddResultResponseModel**](ServiceOrdersToAssetAddResultResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_work_item_image**
> object delete_work_item_image(work_item_id, image_name)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 
image_name = 'image_name_example' # str | 

try:
    api_response = api_instance.delete_work_item_image(work_item_id, image_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->delete_work_item_image: %s\n" % e)
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

# **get_work_item**
> ServiceOrdersToClientOrderItemResponseModel get_work_item(work_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.get_work_item(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->get_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 

### Return type

[**ServiceOrdersToClientOrderItemResponseModel**](ServiceOrdersToClientOrderItemResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_item_charges**
> object get_work_item_charges(work_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.get_work_item_charges(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->get_work_item_charges: %s\n" % e)
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

# **get_work_item_image**
> object get_work_item_image(work_item_id, image_name)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 
image_name = 'image_name_example' # str | 

try:
    api_response = api_instance.get_work_item_image(work_item_id, image_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->get_work_item_image: %s\n" % e)
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

# **get_work_item_images**
> list[str] get_work_item_images(work_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.get_work_item_images(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->get_work_item_images: %s\n" % e)
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

# **get_work_items**
> list[ServiceOrdersToClientOrderItemResponseModel] get_work_items(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_work_items(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->get_work_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[ServiceOrdersToClientOrderItemResponseModel]**](ServiceOrdersToClientOrderItemResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_items_0**
> list[ServiceOrdersToClientOrderItemResponseModel] get_work_items_0(status=status, company_id=company_id, _from=_from, to=to, work_item_number=work_item_number, asset_search=asset_search)

Retrieve work items

Sample request:                GET /api/service/workitems                GET /api/service/workitems?status=pending                GET /api/service/workitems?&amp;status=pending,delayed&amp;companyId=10&amp;from=2010-11-15T10:11:12&amp;to=2011-11-15T10:11:12&amp;workItemNumber=0629-000032-02

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
status = 'status_example' # str | Comma separated list of work item statuses: Pending, Completed, Delayed, InProgress, Withdrawn (optional)
company_id = 56 # int | Filter by Client Company ID (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Items where CreatedOnUtc greater than From parameter (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Items where CreatedOnUtc less than To parameter (optional)
work_item_number = 'work_item_number_example' # str | Filter by CustomOrderNumber or CertificateNumber (optional)
asset_search = 'asset_search_example' # str | Filter by asset Search keywords: SerialNumber, EquipmentId, AssetTag, AssetUser, LegacyId, AssetName, AssetDescription, ManufacturerPartNumber (optional)

try:
    # Retrieve work items
    api_response = api_instance.get_work_items_0(status=status, company_id=company_id, _from=_from, to=to, work_item_number=work_item_number, asset_search=asset_search)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->get_work_items_0: %s\n" % e)
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

[**list[ServiceOrdersToClientOrderItemResponseModel]**](ServiceOrdersToClientOrderItemResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_charges**
> object put_charges(work_item_id, model)

Apply Service Order Item Charges

Allowed Names:      OverrideServiceTotal,      OverridePartsTotal,      OverrideRepairsTotal

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 
model = qualer_sdk.ServiceOrdersFromItemChargeUpdateModel() # ServiceOrdersFromItemChargeUpdateModel | 

try:
    # Apply Service Order Item Charges
    api_response = api_instance.put_charges(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->put_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **model** | [**ServiceOrdersFromItemChargeUpdateModel**](ServiceOrdersFromItemChargeUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_work_item**
> object set_work_item(work_item_id, model)

Update work item

WorkStatus:  Pending = 0  InProgress = 1  Completed = 2  Delayed = 3  Withdrawn = 4  Locked = 5<br />  AsFoundCheck/AsLeftCheck (ChecklistResultStatus):  NotServiced = 0,  Fail = 1,  Pass = 2<br />  ResultStatus/AsFoundResult/AsLeftResult (ServiceResultStatus):  NotAvailable = 0,  Fail = 1,  FailAmbiguous = 10,  FailSignificant = 11,  Pass = 2,  PassAmbiguous = 20,  PassAdjustment = 21,  Done = 22,

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 
model = qualer_sdk.ServiceOrdersFromOrderItemUpdateModel() # ServiceOrdersFromOrderItemUpdateModel | 

try:
    # Update work item
    api_response = api_instance.set_work_item(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->set_work_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **model** | [**ServiceOrdersFromOrderItemUpdateModel**](ServiceOrdersFromOrderItemUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **upload_work_item_images**
> object upload_work_item_images(work_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemsApi()
work_item_id = 56 # int | 

try:
    api_response = api_instance.upload_work_item_images(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemsApi->upload_work_item_images: %s\n" % e)
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

