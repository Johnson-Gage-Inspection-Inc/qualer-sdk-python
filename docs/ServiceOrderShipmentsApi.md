# swagger_client.ServiceOrderShipmentsApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_shipments_append_shipment_tracking_number**](ServiceOrderShipmentsApi.md#service_order_shipments_append_shipment_tracking_number) | **PUT** /api/service/workorders/{serviceOrderId}/shipments/trackingnumber | 
[**service_order_shipments_update_shipment_status**](ServiceOrderShipmentsApi.md#service_order_shipments_update_shipment_status) | **PUT** /api/service/workorders/{serviceOrderId}/shipments/status | 

# **service_order_shipments_append_shipment_tracking_number**
> object service_order_shipments_append_shipment_tracking_number(body, service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderShipmentsApi()
body = swagger_client.QualerApiModelsServiceOrdersFromAppendTrackingNumberModel() # QualerApiModelsServiceOrdersFromAppendTrackingNumberModel | 
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_shipments_append_shipment_tracking_number(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderShipmentsApi->service_order_shipments_append_shipment_tracking_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromAppendTrackingNumberModel**](QualerApiModelsServiceOrdersFromAppendTrackingNumberModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_shipments_update_shipment_status**
> object service_order_shipments_update_shipment_status(body, service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderShipmentsApi()
body = swagger_client.QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel() # QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel | 
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_shipments_update_shipment_status(body, service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderShipmentsApi->service_order_shipments_update_shipment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel**](QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel.md)|  | 
 **service_order_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

