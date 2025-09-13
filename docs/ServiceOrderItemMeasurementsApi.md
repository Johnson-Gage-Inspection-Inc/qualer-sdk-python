# qualer_sdk.ServiceOrderItemMeasurementsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_auxiliary_tools**](ServiceOrderItemMeasurementsApi.md#add_auxiliary_tools) | **POST** /api/service/workitems/{workItemId}/AuxiliaryTools | 
[**create_measurement_form**](ServiceOrderItemMeasurementsApi.md#create_measurement_form) | **POST** /api/service/workitems/{workItemId}/measurements | Create Measurement Form.
[**get_measurement_form**](ServiceOrderItemMeasurementsApi.md#get_measurement_form) | **GET** /api/service/workitems/{workItemId}/form | Get Measurement Form.
[**get_measurements_by_asset**](ServiceOrderItemMeasurementsApi.md#get_measurements_by_asset) | **GET** /api/service/assets/{assetId}/measurements | 
[**update_measurement_form**](ServiceOrderItemMeasurementsApi.md#update_measurement_form) | **POST** /api/service/workitems/{workItemId}/form | Update Measurement Form.


# **add_auxiliary_tools**
> object add_auxiliary_tools(work_item_id, models)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemMeasurementsApi()
work_item_id = 56 # int | 
models = [qualer_sdk.MeasurementsFromCreateMeasurementToolModel()] # list[MeasurementsFromCreateMeasurementToolModel] | 

try:
    api_response = api_instance.add_auxiliary_tools(work_item_id, models)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->add_auxiliary_tools: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**|  | 
 **models** | [**list[MeasurementsFromCreateMeasurementToolModel]**](MeasurementsFromCreateMeasurementToolModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_measurement_form**
> object create_measurement_form(work_item_id, model)

Create Measurement Form.

BatchType: AsLeft, AsFound.                BatchResult: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment, Done, Pending.                CustomFields.Result: NotServiced, Fail, Pass.                ToleranceType: Percentage, Range, Offset, PercentagePlus, Ppm, PpmPlus, Function.                ToleranceMode: Symmetric, Asymmetric, Range.                ToleranceUnit: Percentage, UnitOfMeasure, Ppm.                PrecisionType: Percentage, UnitOfMeasure.                ChannelsType: Combined, IndividualAcross, IndividualDown, OneOf.                Measurement.Result: NotServiced, Fail, FailAmbiguous, FailSignificant, Pass, PassAmbiguous, PassAdjustment, Done, Pending.                FactorId: AmbientTemperature, AirHumidity, BarometricPressure, EvaporationRate, AirBuoyancy, ZFactor, Altitude, WindSpeed, SolarRadiation, LightIntensity, NoiseLevel, PhLevel, WaterConductivity3, WaterTemperature.

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemMeasurementsApi()
work_item_id = 56 # int | Work Item ID of Measurement Form
model = qualer_sdk.MeasurementsFromCreateMeasurementFormModel() # MeasurementsFromCreateMeasurementFormModel | Measurement Form parameters

try:
    # Create Measurement Form.
    api_response = api_instance.create_measurement_form(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->create_measurement_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**| Work Item ID of Measurement Form | 
 **model** | [**MeasurementsFromCreateMeasurementFormModel**](MeasurementsFromCreateMeasurementFormModel.md)| Measurement Form parameters | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurement_form**
> MeasurementsToUpdateMeasurementFormResponseModel get_measurement_form(work_item_id)

Get Measurement Form.

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemMeasurementsApi()
work_item_id = 56 # int | Work Item ID of Measurement Form

try:
    # Get Measurement Form.
    api_response = api_instance.get_measurement_form(work_item_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->get_measurement_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**| Work Item ID of Measurement Form | 

### Return type

[**MeasurementsToUpdateMeasurementFormResponseModel**](MeasurementsToUpdateMeasurementFormResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_measurements_by_asset**
> list[MeasurementsToMeasurementRecordResponseModel] get_measurements_by_asset(asset_id, _from=_from, to=to)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemMeasurementsApi()
asset_id = 56 # int | 
_from = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
to = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_measurements_by_asset(asset_id, _from=_from, to=to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->get_measurements_by_asset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **asset_id** | **int**|  | 
 **_from** | **datetime**|  | [optional] 
 **to** | **datetime**|  | [optional] 

### Return type

[**list[MeasurementsToMeasurementRecordResponseModel]**](MeasurementsToMeasurementRecordResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_measurement_form**
> object update_measurement_form(work_item_id, model)

Update Measurement Form.

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ServiceOrderItemMeasurementsApi()
work_item_id = 56 # int | Work Item ID of Measurement Form
model = qualer_sdk.MeasurementsFromUpdateMeasurementFormModel() # MeasurementsFromUpdateMeasurementFormModel | Measurement Form parameters

try:
    # Update Measurement Form.
    api_response = api_instance.update_measurement_form(work_item_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServiceOrderItemMeasurementsApi->update_measurement_form: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **work_item_id** | **int**| Work Item ID of Measurement Form | 
 **model** | [**MeasurementsFromUpdateMeasurementFormModel**](MeasurementsFromUpdateMeasurementFormModel.md)| Measurement Form parameters | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

