# swagger_client.ServiceOrdersApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_orders_change_order_status**](ServiceOrdersApi.md#service_orders_change_order_status) | **PUT** /api/service/workorders/{serviceOrderId}/status | Change Work Order Status
[**service_orders_create_async**](ServiceOrdersApi.md#service_orders_create_async) | **POST** /api/service/workorders | Create service order.
[**service_orders_create_order_by_schedule**](ServiceOrdersApi.md#service_orders_create_order_by_schedule) | **POST** /api/service/workorders/byplan/{serviceScheduleId} | 
[**service_orders_get_assignments**](ServiceOrdersApi.md#service_orders_get_assignments) | **GET** /api/service/workorders/{serviceOrderId}/assignments | 
[**service_orders_get_charges**](ServiceOrdersApi.md#service_orders_get_charges) | **GET** /api/service/workorders/{serviceOrderId}/charges | 
[**service_orders_get_order_status**](ServiceOrdersApi.md#service_orders_get_order_status) | **GET** /api/service/workorders/{serviceOrderId}/status | Gets current status and next status according to the workflow
[**service_orders_get_work_order**](ServiceOrdersApi.md#service_orders_get_work_order) | **GET** /api/service/workorders/{serviceOrderId} | 
[**service_orders_get_work_orders**](ServiceOrdersApi.md#service_orders_get_work_orders) | **GET** /api/service/workorders | Retrieve work orders by filters
[**service_orders_get_work_orders_0**](ServiceOrdersApi.md#service_orders_get_work_orders_0) | **GET** /api/employee/{employeeId}/workorders | 
[**service_orders_order_cancel**](ServiceOrdersApi.md#service_orders_order_cancel) | **PUT** /api/service/workorders/{serviceOrderId}/cancel | Cancel work order
[**service_orders_put_charges**](ServiceOrdersApi.md#service_orders_put_charges) | **PUT** /api/service/workorders/{serviceOrderId}/charges | Charge Names: LateFee, ServiceDiscount, PrepaidCredit, TradeInCredit, TravelCharge, TaxAmount, ShippingFee

# **service_orders_change_order_status**
> object service_orders_change_order_status(body, service_order_id)

Change Work Order Status

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
body = swagger_client.QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel() # QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel | 
service_order_id = 56 # int | 

try:
    # Change Work Order Status
    api_response = api_instance.service_orders_change_order_status(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_change_order_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel**](QualerApiModelsServiceOrdersFromChangeServiceOrderStatusModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orders_create_async**
> object service_orders_create_async(body)

Create service order.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
body = swagger_client.QualerApiModelsServiceOrdersFromCreateOrderModel() # QualerApiModelsServiceOrdersFromCreateOrderModel | Vendor update model

try:
    # Create service order.
    api_response = api_instance.service_orders_create_async(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_create_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromCreateOrderModel**](QualerApiModelsServiceOrdersFromCreateOrderModel.md)| Vendor update model | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orders_create_order_by_schedule**
> object service_orders_create_order_by_schedule(service_schedule_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
service_schedule_id = 56 # int | 

try:
    api_response = api_instance.service_orders_create_order_by_schedule(service_schedule_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_create_order_by_schedule: %s\n" % e)
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

# **service_orders_get_assignments**
> list[QualerApiModelsServiceOrdersToOrderAssignmentResponseModel] service_orders_get_assignments(service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_orders_get_assignments(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_get_assignments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToOrderAssignmentResponseModel]**](QualerApiModelsServiceOrdersToOrderAssignmentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orders_get_charges**
> QualerWebMvcAreasApiModelsServiceOrdersToChargeResponseModel service_orders_get_charges(service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_orders_get_charges(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_get_charges: %s\n" % e)
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

# **service_orders_get_order_status**
> object service_orders_get_order_status(service_order_id)

Gets current status and next status according to the workflow

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    # Gets current status and next status according to the workflow
    api_response = api_instance.service_orders_get_order_status(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_get_order_status: %s\n" % e)
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

# **service_orders_get_work_order**
> QualerApiModelsServiceOrdersToClientOrderResponseModel service_orders_get_work_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_orders_get_work_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_get_work_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**QualerApiModelsServiceOrdersToClientOrderResponseModel**](QualerApiModelsServiceOrdersToClientOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orders_get_work_orders**
> list[QualerApiModelsServiceOrdersToClientOrderResponseModel] service_orders_get_work_orders(status=status, company_id=company_id, _from=_from, to=to, modified_after=modified_after, work_order_number=work_order_number, assigned_employees=assigned_employees)

Retrieve work orders by filters

Sample request:                GET /api/service/workorders                GET /api/service/workorders?status=submitted                GET /api/service/workorders?&amp;status=onsite,submitted&amp;companyId=10&amp;from=2010-11-15T10:11:12&amp;to=2011-11-15T10:11:12&amp;modifiedAfter=2010-12-15T10:11:12&amp;workOrderNumber=00567

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
status = 'status_example' # str | Comma separated list of statuses.               Order statuses: WaitingForApproval, Submitted, Processing, QualityControl, Cancelled, WaitingForClientSignOff, Completed, Denied, Delayed, Scheduling, Closed, WaitingForVendorSignOff, DelayedApproval.               Payment statuses: NotInvoiced, Invoiced, PartiallyPaid, PaidInFull, NoCharge, Overpaid.               Shipment statuses: Delivered, Shipped, PartialShipment, NotShipped, PickUp, OnSite. (optional)
company_id = 56 # int | Filter by Client Company ID (optional)
_from = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Orders where LastUpdatedOn greater than From parameter (optional)
to = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Orders where LastUpdatedOn less than To parameter (optional)
modified_after = '2013-10-20T19:20:30+01:00' # datetime | Retrieve Work Orders where LastUpdatedOn greater than ModifiedAfter parameter (optional)
work_order_number = 'work_order_number_example' # str | Filter by WorkOrderNumber (optional)
assigned_employees = 'assigned_employees_example' # str | Comma separated list of assigned employees (using full name, alias or login email of the employee) (optional)

try:
    # Retrieve work orders by filters
    api_response = api_instance.service_orders_get_work_orders(status=status, company_id=company_id, _from=_from, to=to, modified_after=modified_after, work_order_number=work_order_number, assigned_employees=assigned_employees)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_get_work_orders: %s\n" % e)
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

[**list[QualerApiModelsServiceOrdersToClientOrderResponseModel]**](QualerApiModelsServiceOrdersToClientOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orders_get_work_orders_0**
> list[QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel] service_orders_get_work_orders_0(employee_id, is_internal=is_internal)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
employee_id = 56 # int | 
is_internal = true # bool |  (optional)

try:
    api_response = api_instance.service_orders_get_work_orders_0(employee_id, is_internal=is_internal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_get_work_orders_0: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **employee_id** | **int**|  | 
 **is_internal** | **bool**|  | [optional] 

### Return type

[**list[QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel]**](QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_orders_order_cancel**
> object service_orders_order_cancel(service_order_id, reason_text=reason_text)

Cancel work order

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
service_order_id = 56 # int | 
reason_text = 'reason_text_example' # str | cancel description (optional)

try:
    # Cancel work order
    api_response = api_instance.service_orders_order_cancel(service_order_id, reason_text=reason_text)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_order_cancel: %s\n" % e)
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

# **service_orders_put_charges**
> object service_orders_put_charges(body, service_order_id)

Charge Names: LateFee, ServiceDiscount, PrepaidCredit, TradeInCredit, TravelCharge, TaxAmount, ShippingFee

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrdersApi()
body = swagger_client.QualerApiModelsServiceOrdersFromChargeUpdateModel() # QualerApiModelsServiceOrdersFromChargeUpdateModel | 
service_order_id = 56 # int | 

try:
    # Charge Names: LateFee, ServiceDiscount, PrepaidCredit, TradeInCredit, TravelCharge, TaxAmount, ShippingFee
    api_response = api_instance.service_orders_put_charges(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrdersApi->service_orders_put_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromChargeUpdateModel**](QualerApiModelsServiceOrdersFromChargeUpdateModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

