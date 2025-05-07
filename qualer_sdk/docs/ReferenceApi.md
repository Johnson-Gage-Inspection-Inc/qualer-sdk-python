# swagger_client.ReferenceApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**reference_get_measurement_quantities**](ReferenceApi.md#reference_get_measurement_quantities) | **GET** /api/reference/MeasurementQuantities | 
[**reference_get_units_of_measure**](ReferenceApi.md#reference_get_units_of_measure) | **GET** /api/reference/UnitsOfMeasure | 


# **reference_get_measurement_quantities**
> list[QualerApiModelsReferenceToMeasurementQuantityResponse] reference_get_measurement_quantities()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    api_response = api_instance.reference_get_measurement_quantities()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_get_measurement_quantities: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsReferenceToMeasurementQuantityResponse]**](QualerApiModelsReferenceToMeasurementQuantityResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **reference_get_units_of_measure**
> list[QualerApiModelsReferenceToUnitOfMeasureResponse] reference_get_units_of_measure()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReferenceApi()

try:
    api_response = api_instance.reference_get_units_of_measure()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReferenceApi->reference_get_units_of_measure: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsReferenceToUnitOfMeasureResponse]**](QualerApiModelsReferenceToUnitOfMeasureResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

