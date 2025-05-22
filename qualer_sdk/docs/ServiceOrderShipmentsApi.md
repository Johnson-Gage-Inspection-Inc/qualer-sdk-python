# qualer_sdk.ServiceOrderShipmentsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**append_shipment_tracking_number**](ServiceOrderShipmentsApi.md#append_shipment_tracking_number) | **PUT** /api/service/workorders/{serviceOrderId}/shipments/trackingnumber | 
[**update_shipment_status**](ServiceOrderShipmentsApi.md#update_shipment_status) | **PUT** /api/service/workorders/{serviceOrderId}/shipments/status | 


# **append_shipment_tracking_number**
> object append_shipment_tracking_number(service_order_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderShipmentsApi()
service_order_id = 56 # int | 
model = qualer_sdk.QualerApiModelsServiceOrdersFromAppendTrackingNumberModel() # QualerApiModelsServiceOrdersFromAppendTrackingNumberModel | 

try:
    api_response = api_instance.append_shipment_tracking_number(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderShipmentsApi->append_shipment_tracking_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromAppendTrackingNumberModel**](QualerApiModelsServiceOrdersFromAppendTrackingNumberModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_shipment_status**
> object update_shipment_status(service_order_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderShipmentsApi()
service_order_id = 56 # int | 
model = qualer_sdk.QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel() # QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel | 

try:
    api_response = api_instance.update_shipment_status(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderShipmentsApi->update_shipment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel**](QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

