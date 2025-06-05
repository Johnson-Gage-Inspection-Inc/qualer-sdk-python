# qualer_sdk.ReportDatasetsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**channel_uniformity_by_order**](ReportDatasetsApi.md#channel_uniformity_by_order) | **GET** /api/data/orders/{serviceOrderId}/ChannelUniformity | 
[**get_all_measurements**](ReportDatasetsApi.md#get_all_measurements) | **GET** /api/data/Measurements/{serviceOrderItemId} | 
[**get_all_measurements_by_order**](ReportDatasetsApi.md#get_all_measurements_by_order) | **GET** /api/data/orders/{serviceOrderId}/Measurements | 
[**get_as_found_measurements**](ReportDatasetsApi.md#get_as_found_measurements) | **GET** /api/data/MeasurementsAsFound/{serviceOrderItemId} | 
[**get_as_found_measurements_by_order**](ReportDatasetsApi.md#get_as_found_measurements_by_order) | **GET** /api/data/orders/{serviceOrderId}/MeasurementsAsFound | 
[**get_as_left_measurements**](ReportDatasetsApi.md#get_as_left_measurements) | **GET** /api/data/MeasurementsAsLeft/{serviceOrderItemId} | 
[**get_as_left_measurements_by_order**](ReportDatasetsApi.md#get_as_left_measurements_by_order) | **GET** /api/data/orders/{serviceOrderId}/MeasurementsAsLeft | 
[**get_asset_attributes**](ReportDatasetsApi.md#get_asset_attributes) | **GET** /api/data/AssetAttributes/{serviceOrderItemId} | 
[**get_asset_service_records**](ReportDatasetsApi.md#get_asset_service_records) | **GET** /api/data/AssetServiceRecords/{serviceOrderItemId} | 
[**get_channel_results**](ReportDatasetsApi.md#get_channel_results) | **GET** /api/data/ChannelResults/{serviceOrderItemId} | 
[**get_channel_results_by_order**](ReportDatasetsApi.md#get_channel_results_by_order) | **GET** /api/data/orders/{serviceOrderId}/ChannelResults | 
[**get_channel_uniformity**](ReportDatasetsApi.md#get_channel_uniformity) | **GET** /api/data/ChannelUniformity/{serviceOrderItemId} | 
[**get_client_attributes**](ReportDatasetsApi.md#get_client_attributes) | **GET** /api/data/ClientAttributes/{serviceOrderId} | 
[**get_company_certifications**](ReportDatasetsApi.md#get_company_certifications) | **GET** /api/data/CompanyCertifications | 
[**get_external_data_reports**](ReportDatasetsApi.md#get_external_data_reports) | **GET** /api/data/{serviceOrderId}/ExternalDataReports | 
[**get_measurement_charts**](ReportDatasetsApi.md#get_measurement_charts) | **GET** /api/data/MeasurementChart/{serviceOrderItemId} | 
[**get_measurement_fields**](ReportDatasetsApi.md#get_measurement_fields) | **GET** /api/data/MeasurementFields/{serviceOrderItemId} | 
[**get_measurement_fields_by_order**](ReportDatasetsApi.md#get_measurement_fields_by_order) | **GET** /api/data/orders/{serviceOrderId}/MeasurementFields | 
[**get_order_item_documents**](ReportDatasetsApi.md#get_order_item_documents) | **GET** /api/data/OrderItemDocuments/{serviceOrderItemId} | 
[**get_order_item_images**](ReportDatasetsApi.md#get_order_item_images) | **GET** /api/data/OrderItemImages/{serviceOrderItemId} | 
[**get_reference_standards**](ReportDatasetsApi.md#get_reference_standards) | **GET** /api/data/ReferenceStandards/{serviceOrderItemId} | 
[**get_reference_standards_by_order**](ReportDatasetsApi.md#get_reference_standards_by_order) | **GET** /api/data/orders/{serviceOrderId}/ReferenceStandards | 
[**get_service_order_assignees**](ReportDatasetsApi.md#get_service_order_assignees) | **GET** /api/data/ServiceOrderAssignees/{serviceOrderId} | 
[**get_service_order_charges**](ReportDatasetsApi.md#get_service_order_charges) | **GET** /api/data/ServiceOrderCharges/{serviceOrderId} | 
[**get_service_order_item_components**](ReportDatasetsApi.md#get_service_order_item_components) | **GET** /api/data/ServiceOrderItemComponents/{serviceOrderItemId} | 
[**get_service_order_item_components_by_order**](ReportDatasetsApi.md#get_service_order_item_components_by_order) | **GET** /api/data/orders/{serviceOrderId}/ServiceOrderItemComponents | 
[**get_service_order_item_fields_by_order**](ReportDatasetsApi.md#get_service_order_item_fields_by_order) | **GET** /api/data/ServiceOrderItemFieldsByOrder/{serviceOrderId} | 
[**get_service_order_item_options**](ReportDatasetsApi.md#get_service_order_item_options) | **GET** /api/data/ServiceOrderItemOptions/{serviceOrderItemId} | 
[**get_service_order_item_status_history_async**](ReportDatasetsApi.md#get_service_order_item_status_history_async) | **GET** /api/data/ServiceOrderItemStatusHistory/{serviceOrderItemId} | 
[**get_service_order_item_tasks_by_order**](ReportDatasetsApi.md#get_service_order_item_tasks_by_order) | **GET** /api/data/ServiceOrderItemTasksByOrder/{serviceOrderId} | 
[**get_service_order_item_tasks_by_order_items**](ReportDatasetsApi.md#get_service_order_item_tasks_by_order_items) | **GET** /api/data/ServiceOrderItemTasksByOrderItem/{serviceOrderItemId} | 
[**get_service_order_items**](ReportDatasetsApi.md#get_service_order_items) | **GET** /api/data/ServiceOrderItems/{serviceOrderItemId} | 
[**get_service_order_items_by_order**](ReportDatasetsApi.md#get_service_order_items_by_order) | **GET** /api/data/orders/{serviceOrderId}/ServiceOrderItems | 
[**get_service_order_tasks**](ReportDatasetsApi.md#get_service_order_tasks) | **GET** /api/data/ServiceOrderTasks/{serviceOrderId} | 
[**get_service_orders**](ReportDatasetsApi.md#get_service_orders) | **GET** /api/data/ServiceOrders/{serviceOrderId} | 
[**get_tool_attributes**](ReportDatasetsApi.md#get_tool_attributes) | **GET** /api/data/ToolAttributes/{serviceOrderItemId} | 
[**get_tool_range_attributes**](ReportDatasetsApi.md#get_tool_range_attributes) | **GET** /api/data/ToolRangeAttributes/{serviceOrderItemId} | 


# **channel_uniformity_by_order**
> list[QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse] channel_uniformity_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.channel_uniformity_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->channel_uniformity_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse]**](QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_measurements**
> list[QualerApiModelsReportDatasetsToMeasurementAllResponse] get_all_measurements(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_all_measurements(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_all_measurements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementAllResponse]**](QualerApiModelsReportDatasetsToMeasurementAllResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all_measurements_by_order**
> list[QualerApiModelsReportDatasetsToMeasurementAllResponse] get_all_measurements_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_all_measurements_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_all_measurements_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementAllResponse]**](QualerApiModelsReportDatasetsToMeasurementAllResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_as_found_measurements**
> list[QualerApiModelsReportDatasetsToMeasurementResponse] get_as_found_measurements(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_as_found_measurements(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_as_found_measurements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementResponse]**](QualerApiModelsReportDatasetsToMeasurementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_as_found_measurements_by_order**
> list[QualerApiModelsReportDatasetsToMeasurementResponse] get_as_found_measurements_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_as_found_measurements_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_as_found_measurements_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementResponse]**](QualerApiModelsReportDatasetsToMeasurementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_as_left_measurements**
> list[QualerApiModelsReportDatasetsToMeasurementResponse] get_as_left_measurements(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_as_left_measurements(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_as_left_measurements: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementResponse]**](QualerApiModelsReportDatasetsToMeasurementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_as_left_measurements_by_order**
> list[QualerApiModelsReportDatasetsToMeasurementResponse] get_as_left_measurements_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_as_left_measurements_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_as_left_measurements_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementResponse]**](QualerApiModelsReportDatasetsToMeasurementResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_attributes**
> list[QualerApiModelsReportDatasetsToAssetAttributeResponse] get_asset_attributes(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_asset_attributes(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_asset_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToAssetAttributeResponse]**](QualerApiModelsReportDatasetsToAssetAttributeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_asset_service_records**
> QualerApiModelsReportDatasetsToAssetSummaryResponse get_asset_service_records(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_asset_service_records(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_asset_service_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**QualerApiModelsReportDatasetsToAssetSummaryResponse**](QualerApiModelsReportDatasetsToAssetSummaryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_results**
> list[QualerApiModelsReportDatasetsToMeasurementChannelResultResponse] get_channel_results(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_channel_results(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_channel_results: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementChannelResultResponse]**](QualerApiModelsReportDatasetsToMeasurementChannelResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_results_by_order**
> list[QualerApiModelsReportDatasetsToMeasurementChannelResultResponse] get_channel_results_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_channel_results_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_channel_results_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementChannelResultResponse]**](QualerApiModelsReportDatasetsToMeasurementChannelResultResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_channel_uniformity**
> list[QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse] get_channel_uniformity(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_channel_uniformity(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_channel_uniformity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse]**](QualerApiModelsReportDatasetsToMeasurementChannelUniformityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_client_attributes**
> QualerApiModelsReportDatasetsToClientAttributeResponse get_client_attributes(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_client_attributes(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_client_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**QualerApiModelsReportDatasetsToClientAttributeResponse**](QualerApiModelsReportDatasetsToClientAttributeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_certifications**
> list[QualerApiModelsReportDatasetsToCompanyCertificationResponse] get_company_certifications()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()

try:
    api_response = api_instance.get_company_certifications()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_company_certifications: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsReportDatasetsToCompanyCertificationResponse]**](QualerApiModelsReportDatasetsToCompanyCertificationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_external_data_reports**
> list[QualerApiModelsReportDatasetsToExternalDataReportResponse] get_external_data_reports(service_order_id, service_order_item_ids)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 
service_order_item_ids = [56] # list[int] | 

try:
    api_response = api_instance.get_external_data_reports(service_order_id, service_order_item_ids)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_external_data_reports: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 
 **service_order_item_ids** | [**list[int]**](int.md)|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToExternalDataReportResponse]**](QualerApiModelsReportDatasetsToExternalDataReportResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurement_charts**
> list[QualerApiModelsReportDatasetsToMeasurementChartResponse] get_measurement_charts(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_measurement_charts(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_measurement_charts: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementChartResponse]**](QualerApiModelsReportDatasetsToMeasurementChartResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurement_fields**
> list[QualerApiModelsReportDatasetsToMeasurementFieldResponse] get_measurement_fields(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_measurement_fields(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_measurement_fields: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementFieldResponse]**](QualerApiModelsReportDatasetsToMeasurementFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurement_fields_by_order**
> list[QualerApiModelsReportDatasetsToMeasurementFieldResponse] get_measurement_fields_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_measurement_fields_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_measurement_fields_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToMeasurementFieldResponse]**](QualerApiModelsReportDatasetsToMeasurementFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_item_documents**
> list[QualerApiModelsReportDatasetsToOrderItemImageResponse] get_order_item_documents(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_order_item_documents(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_order_item_documents: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToOrderItemImageResponse]**](QualerApiModelsReportDatasetsToOrderItemImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_order_item_images**
> list[QualerApiModelsReportDatasetsToOrderItemImageResponse] get_order_item_images(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_order_item_images(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_order_item_images: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToOrderItemImageResponse]**](QualerApiModelsReportDatasetsToOrderItemImageResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_standards**
> list[QualerApiModelsReportDatasetsToReferenceStandardResponse] get_reference_standards(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_reference_standards(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_reference_standards: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToReferenceStandardResponse]**](QualerApiModelsReportDatasetsToReferenceStandardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_reference_standards_by_order**
> list[QualerApiModelsReportDatasetsToReferenceStandardResponse] get_reference_standards_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_reference_standards_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_reference_standards_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToReferenceStandardResponse]**](QualerApiModelsReportDatasetsToReferenceStandardResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_assignees**
> list[QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse] get_service_order_assignees(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_assignees(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_assignees: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse]**](QualerApiModelsReportDatasetsToServiceOrderAssigneeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_charges**
> list[QualerApiModelsReportDatasetsToServiceOrderChargeResponse] get_service_order_charges(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_charges(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_charges: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderChargeResponse]**](QualerApiModelsReportDatasetsToServiceOrderChargeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_components**
> list[QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse] get_service_order_item_components(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_components(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_components: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_components_by_order**
> list[QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse] get_service_order_item_components_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_components_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_components_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemComponentResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_fields_by_order**
> list[QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse] get_service_order_item_fields_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_fields_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_fields_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_options**
> list[QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse] get_service_order_item_options(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_options(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_options: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemOptionResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_status_history_async**
> list[QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse] get_service_order_item_status_history_async(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_status_history_async(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_status_history_async: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemStatusHistoryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_tasks_by_order**
> list[QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse] get_service_order_item_tasks_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_tasks_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_tasks_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_item_tasks_by_order_items**
> list[QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse] get_service_order_item_tasks_by_order_items(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_item_tasks_by_order_items(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_item_tasks_by_order_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_items**
> list[QualerApiModelsReportDatasetsToServiceOrderItemResponse] get_service_order_items(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_items(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_items: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_items_by_order**
> list[QualerApiModelsReportDatasetsToServiceOrderItemResponse] get_service_order_items_by_order(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_items_by_order(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_items_by_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderItemResponse]**](QualerApiModelsReportDatasetsToServiceOrderItemResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_order_tasks**
> list[QualerApiModelsReportDatasetsToServiceOrderTaskResponse] get_service_order_tasks(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_order_tasks(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_order_tasks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToServiceOrderTaskResponse]**](QualerApiModelsReportDatasetsToServiceOrderTaskResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_orders**
> QualerApiModelsReportDatasetsToServiceOrderResponse get_service_orders(service_order_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_id = 56 # int | 

try:
    api_response = api_instance.get_service_orders(service_order_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_service_orders: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_id** | **int**|  | 

### Return type

[**QualerApiModelsReportDatasetsToServiceOrderResponse**](QualerApiModelsReportDatasetsToServiceOrderResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tool_attributes**
> list[QualerApiModelsReportDatasetsToToolAttributeResponse] get_tool_attributes(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_tool_attributes(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_tool_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToToolAttributeResponse]**](QualerApiModelsReportDatasetsToToolAttributeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tool_range_attributes**
> list[QualerApiModelsReportDatasetsToToolRangeAttributeResponse] get_tool_range_attributes(service_order_item_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ReportDatasetsApi()
service_order_item_id = 56 # int | 

try:
    api_response = api_instance.get_tool_range_attributes(service_order_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportDatasetsApi->get_tool_range_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_order_item_id** | **int**|  | 

### Return type

[**list[QualerApiModelsReportDatasetsToToolRangeAttributeResponse]**](QualerApiModelsReportDatasetsToToolRangeAttributeResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

