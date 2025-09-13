# qualer_sdk.ServiceOrdersApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**change_order_status**](ServiceOrdersApi.md#change_order_status) | **PUT** /api/service/workorders/{serviceOrderId}/status | Change Work Order Status
[**create_async**](ServiceOrdersApi.md#create_async) | **POST** /api/service/workorders | Create service order.
[**create_order_by_schedule**](ServiceOrdersApi.md#create_order_by_schedule) | **POST** /api/service/workorders/byplan/{serviceScheduleId} | 
[**get_assignments**](ServiceOrdersApi.md#get_assignments) | **GET** /api/service/workorders/{serviceOrderId}/assignments | 
[**get_charges**](ServiceOrdersApi.md#get_charges) | **GET** /api/service/workorders/{serviceOrderId}/charges | 
[**get_order_status**](ServiceOrdersApi.md#get_order_status) | **GET** /api/service/workorders/{serviceOrderId}/status | Gets current status and next status according to the workflow
[**get_work_order**](ServiceOrdersApi.md#get_work_order) | **GET** /api/service/workorders/{serviceOrderId} | 
[**get_work_orders**](ServiceOrdersApi.md#get_work_orders) | **GET** /api/service/workorders | Retrieve work orders by filters
[**get_work_orders_0**](ServiceOrdersApi.md#get_work_orders_0) | **GET** /api/employee/{employeeId}/workorders | 
[**order_cancel**](ServiceOrdersApi.md#order_cancel) | **PUT** /api/service/workorders/{serviceOrderId}/cancel | Cancel work order
[**put_charges**](ServiceOrdersApi.md#put_charges) | **PUT** /api/service/workorders/{serviceOrderId}/charges | Charge Names: LateFee, ServiceDiscount, PrepaidCredit, TradeInCredit, TravelCharge, TaxAmount, ShippingFee


# **change_order_status**
> object change_order_status(service_order_id, model)

Change Work Order Status

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 
model = qualer_sdk.ServiceOrdersFromChangeServiceOrderStatusModel() # ServiceOrdersFromChangeServiceOrderStatusModel | 

try:
    # Change Work Order Status
    api_response = api_instance.change_order_status(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->change_order_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**ServiceOrdersFromChangeServiceOrderStatusModel**](ServiceOrdersFromChangeServiceOrderStatusModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_async**
> object create_async(model)

Create service order.



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
model = qualer_sdk.ServiceOrdersFromCreateOrderModel() # ServiceOrdersFromCreateOrderModel | Vendor update model

try:
    # Create service order.
    api_response = api_instance.create_async(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->create_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**ServiceOrdersFromCreateOrderModel**](ServiceOrdersFromCreateOrderModel.md)| Vendor update model | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_order_by_schedule**
> object create_order_by_schedule(service_schedule_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_schedule_id = 56 # int | 

try:
    api_response = api_instance.create_order_by_schedule(service_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->create_order_by_schedule: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_schedule_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assignments**
> list[ServiceOrdersToOrderAssignmentResponseModel] get_assignments(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_assignments(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->get_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[ServiceOrdersToOrderAssignmentResponseModel]**](ServiceOrdersToOrderAssignmentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_charges**
> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel get_charges(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_charges(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->get_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel**](QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_status**
> object get_order_status(service_order_id)

Gets current status and next status according to the workflow

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    # Gets current status and next status according to the workflow
    api_response = api_instance.get_order_status(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->get_order_status: %s\n" % e)
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

# **get_work_order**
> ServiceOrdersToClientOrderResponseModel get_work_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_work_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->get_work_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**ServiceOrdersToClientOrderResponseModel**](ServiceOrdersToClientOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_orders**
> list[ServiceOrdersToClientOrderResponseModel] get_work_orders(status=status, company_id=company_id, _from=_from, to=to, modified_after=modified_after, work_order_number=work_order_number, assigned_employees=assigned_employees)

Retrieve work orders by filters

Sample request:                GET /api/service/workorders                GET /api/service/workorders?status=submitted                GET /api/service/workorders?&amp;status=onsite,submitted&amp;companyId=10&amp;from=2010-11-15T10:11:12&amp;to=2011-11-15T10:11:12&amp;modifiedAfter=2010-12-15T10:11:12&amp;workOrderNumber=00567

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
status = 'status_example' # str | Comma separated list of statuses.               Order statuses: WaitingForApproval, Submitted, Processing, QualityControl, Cancelled, WaitingForClientSignOff, Completed, Denied, Delayed, Scheduling, Closed, WaitingForVendorSignOff, DelayedApproval.               Payment statuses: NotInvoiced, Invoiced, PartiallyPaid, PaidInFull, NoCharge, Overpaid.               Shipment statuses: Delivered, Shipped, PartialShipment, NotShipped, PickUp, OnSite. (optional)
company_id = 56 # int | Filter by Client Company ID (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Orders where LastUpdatedOn greater than From parameter (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Orders where LastUpdatedOn less than To parameter (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Orders where LastUpdatedOn greater than ModifiedAfter parameter (optional)
work_order_number = 'work_order_number_example' # str | Filter by WorkOrderNumber (optional)
assigned_employees = 'assigned_employees_example' # str | Comma separated list of assigned employees (using full name, alias or login email of the employee) (optional)

try:
    # Retrieve work orders by filters
    api_response = api_instance.get_work_orders(status=status, company_id=company_id, _from=_from, to=to, modified_after=modified_after, work_order_number=work_order_number, assigned_employees=assigned_employees)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->get_work_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **status** | **str**| Comma separated list of statuses.               Order statuses: WaitingForApproval, Submitted, Processing, QualityControl, Cancelled, WaitingForClientSignOff, Completed, Denied, Delayed, Scheduling, Closed, WaitingForVendorSignOff, DelayedApproval.               Payment statuses: NotInvoiced, Invoiced, PartiallyPaid, PaidInFull, NoCharge, Overpaid.               Shipment statuses: Delivered, Shipped, PartialShipment, NotShipped, PickUp, OnSite. | [optional] 
 **company_id** | **int**| Filter by Client Company ID | [optional] 
 **_from** | **datetime**| Retrieve Work Orders where LastUpdatedOn greater than From parameter | [optional] 
 **to** | **datetime**| Retrieve Work Orders where LastUpdatedOn less than To parameter | [optional] 
 **modified_after** | **datetime**| Retrieve Work Orders where LastUpdatedOn greater than ModifiedAfter parameter | [optional] 
 **work_order_number** | **str**| Filter by WorkOrderNumber | [optional] 
 **assigned_employees** | **str**| Comma separated list of assigned employees (using full name, alias or login email of the employee) | [optional] 

### Return type

[**list[ServiceOrdersToClientOrderResponseModel]**](ServiceOrdersToClientOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_work_orders_0**
> list[ServiceOrdersToProviderServiceOrderResponseModel] get_work_orders_0(employee_id, is_internal=is_internal)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
employee_id = 56 # int | 
is_internal = true # bool |  (optional)

try:
    api_response = api_instance.get_work_orders_0(employee_id, is_internal=is_internal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->get_work_orders_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **is_internal** | **bool**|  | [optional] 

### Return type

[**list[ServiceOrdersToProviderServiceOrderResponseModel]**](ServiceOrdersToProviderServiceOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **order_cancel**
> object order_cancel(service_order_id, reason_text=reason_text)

Cancel work order

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 
reason_text = 'reason_text_example' # str | cancel description (optional)

try:
    # Cancel work order
    api_response = api_instance.order_cancel(service_order_id, reason_text=reason_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->order_cancel: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **reason_text** | **str**| cancel description | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_charges**
> object put_charges(service_order_id, model)

Charge Names: LateFee, ServiceDiscount, PrepaidCredit, TradeInCredit, TravelCharge, TaxAmount, ShippingFee

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrdersApi()
service_order_id = 56 # int | 
model = qualer_sdk.ServiceOrdersFromChargeUpdateModel() # ServiceOrdersFromChargeUpdateModel | 

try:
    # Charge Names: LateFee, ServiceDiscount, PrepaidCredit, TradeInCredit, TravelCharge, TaxAmount, ShippingFee
    api_response = api_instance.put_charges(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->put_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**ServiceOrdersFromChargeUpdateModel**](ServiceOrdersFromChargeUpdateModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

