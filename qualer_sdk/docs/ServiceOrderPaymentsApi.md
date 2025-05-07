# swagger_client.ServiceOrderPaymentsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_payments_change_work_order_payment_status**](ServiceOrderPaymentsApi.md#service_order_payments_change_work_order_payment_status) | **PUT** /api/service/workorders/{serviceOrderId}/payments/status | 
[**service_order_payments_create_work_order_payment**](ServiceOrderPaymentsApi.md#service_order_payments_create_work_order_payment) | **POST** /api/service/workorders/{serviceOrderId}/payments | 
[**service_order_payments_get_all_work_order_payments**](ServiceOrderPaymentsApi.md#service_order_payments_get_all_work_order_payments) | **GET** /api/service/workorders/{serviceOrderId}/payments | 
[**service_order_payments_get_work_order_payment**](ServiceOrderPaymentsApi.md#service_order_payments_get_work_order_payment) | **GET** /api/service/workorders/payments/{serviceOrderPaymentId} | 


# **service_order_payments_change_work_order_payment_status**
> object service_order_payments_change_work_order_payment_status(service_order_id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPaymentsApi()
service_order_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel() # QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel | 

try:
    api_response = api_instance.service_order_payments_change_work_order_payment_status(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPaymentsApi->service_order_payments_change_work_order_payment_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel**](QualerApiModelsServiceOrdersFromUpdatePaymentStatusModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_payments_create_work_order_payment**
> QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse service_order_payments_create_work_order_payment(service_order_id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPaymentsApi()
service_order_id = 56 # int | 
model = swagger_client.QualerApiModelsServiceOrdersFromAddPaymentModel() # QualerApiModelsServiceOrdersFromAddPaymentModel | 

try:
    api_response = api_instance.service_order_payments_create_work_order_payment(service_order_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPaymentsApi->service_order_payments_create_work_order_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **model** | [**QualerApiModelsServiceOrdersFromAddPaymentModel**](QualerApiModelsServiceOrdersFromAddPaymentModel.md)|  | 

### Return type

[**QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse**](QualerApiModelsServiceOrdersToCreatedWorkOrderPaymentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_payments_get_all_work_order_payments**
> list[QualerApiModelsServiceOrdersToPaymentResponseModel] service_order_payments_get_all_work_order_payments(service_order_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPaymentsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.service_order_payments_get_all_work_order_payments(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPaymentsApi->service_order_payments_get_all_work_order_payments: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsServiceOrdersToPaymentResponseModel]**](QualerApiModelsServiceOrdersToPaymentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_payments_get_work_order_payment**
> QualerApiModelsServiceOrdersToPaymentResponseModel service_order_payments_get_work_order_payment(service_order_payment_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderPaymentsApi()
service_order_payment_id = 56 # int | 

try:
    api_response = api_instance.service_order_payments_get_work_order_payment(service_order_payment_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderPaymentsApi->service_order_payments_get_work_order_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_payment_id** | **int**|  | 

### Return type

[**QualerApiModelsServiceOrdersToPaymentResponseModel**](QualerApiModelsServiceOrdersToPaymentResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

