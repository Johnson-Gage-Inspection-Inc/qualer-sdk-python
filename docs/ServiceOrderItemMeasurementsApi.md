# swagger_client.ServiceOrderItemMeasurementsApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**service_order_item_measurements_add_auxiliary_tools**](ServiceOrderItemMeasurementsApi.md#service_order_item_measurements_add_auxiliary_tools) | **POST** /api/service/workitems/{workItemId}/AuxiliaryTools | 
[**service_order_item_measurements_create_measurement_form**](ServiceOrderItemMeasurementsApi.md#service_order_item_measurements_create_measurement_form) | **POST** /api/service/workitems/{workItemId}/measurements | Create Measurement Form.
[**service_order_item_measurements_get_measurement_form**](ServiceOrderItemMeasurementsApi.md#service_order_item_measurements_get_measurement_form) | **GET** /api/service/workitems/{workItemId}/form | Get Measurement Form.
[**service_order_item_measurements_get_measurements_by_asset**](ServiceOrderItemMeasurementsApi.md#service_order_item_measurements_get_measurements_by_asset) | **GET** /api/service/assets/{assetId}/measurements | 
[**service_order_item_measurements_update_measurement_form**](ServiceOrderItemMeasurementsApi.md#service_order_item_measurements_update_measurement_form) | **POST** /api/service/workitems/{workItemId}/form | Update Measurement Form.

# **service_order_item_measurements_add_auxiliary_tools**
> object service_order_item_measurements_add_auxiliary_tools(body, work_item_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemMeasurementsApi()
body = [swagger_client.QualerApiModelsMeasurementsFromCreateMeasurementToolModel()] # list[QualerApiModelsMeasurementsFromCreateMeasurementToolModel] | 
work_item_id = 56 # int | 

try:
    api_response = api_instance.service_order_item_measurements_add_auxiliary_tools(body, work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->service_order_item_measurements_add_auxiliary_tools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**list[QualerApiModelsMeasurementsFromCreateMeasurementToolModel]**](QualerApiModelsMeasurementsFromCreateMeasurementToolModel.md)|  | 
 **work_item_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_measurements_create_measurement_form**
> object service_order_item_measurements_create_measurement_form(body, work_item_id)

Create Measurement Form.

BatchType: AsLeft, AsFound.                BatchResult: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment, Done, Pending.                CustomFields.Result: NotServiced, Fail, Pass.                ToleranceType: Percentage, Range, Offset, PercentagePlus, Ppm, PpmPlus, Function.                ToleranceMode: Symmetric, Asymmetric, Range.                ToleranceUnit: Percentage, UnitOfMeasure, Ppm.                PrecisionType: Percentage, UnitOfMeasure.                ChannelsType: Combined, IndividualAcross, IndividualDown, OneOf.                Measurement.Result: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment, Done, Pending.                FactorId: AmbientTemperature, AirHumidity, BarometricPressure, EvaporationRate, AirBuoyancy, ZFactor, Altitude, WindSpeed, SolarRadiation, LightIntensity, NoiseLevel, PhLevel, WaterConductivity3, WaterTemperature.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemMeasurementsApi()
body = swagger_client.QualerApiModelsMeasurementsFromCreateMeasurementFormModel() # QualerApiModelsMeasurementsFromCreateMeasurementFormModel | Measurement Form parameters
work_item_id = 56 # int | Work Item ID of Measurement Form

try:
    # Create Measurement Form.
    api_response = api_instance.service_order_item_measurements_create_measurement_form(body, work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->service_order_item_measurements_create_measurement_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsMeasurementsFromCreateMeasurementFormModel**](QualerApiModelsMeasurementsFromCreateMeasurementFormModel.md)| Measurement Form parameters | 
 **work_item_id** | **int**| Work Item ID of Measurement Form | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_measurements_get_measurement_form**
> QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel service_order_item_measurements_get_measurement_form(work_item_id)

Get Measurement Form.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemMeasurementsApi()
work_item_id = 56 # int | Work Item ID of Measurement Form

try:
    # Get Measurement Form.
    api_response = api_instance.service_order_item_measurements_get_measurement_form(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->service_order_item_measurements_get_measurement_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**| Work Item ID of Measurement Form | 

### Return type

[**QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel**](QualerApiModelsMeasurementsToUpdateMeasurementFormResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_measurements_get_measurements_by_asset**
> list[QualerApiModelsMeasurementsToMeasurementRecordResponseModel] service_order_item_measurements_get_measurements_by_asset(asset_id, _from=_from, to=to)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemMeasurementsApi()
asset_id = 56 # int | 
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.service_order_item_measurements_get_measurements_by_asset(asset_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->service_order_item_measurements_get_measurements_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 

### Return type

[**list[QualerApiModelsMeasurementsToMeasurementRecordResponseModel]**](QualerApiModelsMeasurementsToMeasurementRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **service_order_item_measurements_update_measurement_form**
> object service_order_item_measurements_update_measurement_form(body, work_item_id)

Update Measurement Form.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServiceOrderItemMeasurementsApi()
body = swagger_client.QualerApiModelsMeasurementsFromUpdateMeasurementFormModel() # QualerApiModelsMeasurementsFromUpdateMeasurementFormModel | Measurement Form parameters
work_item_id = 56 # int | Work Item ID of Measurement Form

try:
    # Update Measurement Form.
    api_response = api_instance.service_order_item_measurements_update_measurement_form(body, work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->service_order_item_measurements_update_measurement_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsMeasurementsFromUpdateMeasurementFormModel**](QualerApiModelsMeasurementsFromUpdateMeasurementFormModel.md)| Measurement Form parameters | 
 **work_item_id** | **int**| Work Item ID of Measurement Form | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

