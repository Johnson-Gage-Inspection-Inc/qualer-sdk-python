# swagger_client.AccountApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_companies**](AccountApi.md#account_companies) | **POST** /api/user/companies | 
[**account_get_employee_message**](AccountApi.md#account_get_employee_message) | **GET** /api/user/messages/{messageId} | 
[**account_get_employee_messages**](AccountApi.md#account_get_employee_messages) | **GET** /api/user/messages | 
[**account_login**](AccountApi.md#account_login) | **POST** /api/login | Login
[**account_logout**](AccountApi.md#account_logout) | **POST** /api/logout | Logout
[**account_post_employee_location**](AccountApi.md#account_post_employee_location) | **POST** /api/user/location | Post Employee Location


# **account_companies**
> object account_companies(model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
model = swagger_client.QualerWebMvcAreasApiModelsAccountToLoginModel() # QualerWebMvcAreasApiModelsAccountToLoginModel | 

try:
    api_response = api_instance.account_companies(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_companies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerWebMvcAreasApiModelsAccountToLoginModel**](QualerWebMvcAreasApiModelsAccountToLoginModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_employee_message**
> QualerApiModelsAccountToEmployeeEventMessageResponseModel account_get_employee_message(message_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
message_id = 56 # int | 

try:
    api_response = api_instance.account_get_employee_message(message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_employee_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message_id** | **int**|  | 

### Return type

[**QualerApiModelsAccountToEmployeeEventMessageResponseModel**](QualerApiModelsAccountToEmployeeEventMessageResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_get_employee_messages**
> list[QualerApiModelsAccountToEmployeeEventResponseModel] account_get_employee_messages(model_period=model_period, model_site_id=model_site_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
model_period = 56 # int |  (optional)
model_site_id = 56 # int |  (optional)

try:
    api_response = api_instance.account_get_employee_messages(model_period=model_period, model_site_id=model_site_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_get_employee_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_period** | **int**|  | [optional] 
 **model_site_id** | **int**|  | [optional] 

### Return type

[**list[QualerApiModelsAccountToEmployeeEventResponseModel]**](QualerApiModelsAccountToEmployeeEventResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_login**
> QualerApiModelsAccountFromLoginResponseModel account_login(model)

Login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
model = swagger_client.QualerWebMvcAreasApiModelsAccountToLoginModel() # QualerWebMvcAreasApiModelsAccountToLoginModel | 

try:
    # Login
    api_response = api_instance.account_login(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_login: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerWebMvcAreasApiModelsAccountToLoginModel**](QualerWebMvcAreasApiModelsAccountToLoginModel.md)|  | 

### Return type

[**QualerApiModelsAccountFromLoginResponseModel**](QualerApiModelsAccountFromLoginResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_logout**
> object account_logout(model)

Logout

LogoutAction:<br />  Logout - remove the passed token from the list of active sessions (default value)<br />  LogoutAll - remove this token and all other tokens created for the same user from the list of active sessions<br />  LogoutAllOther - remove all tokens created for the same user from the list of session except for the one that is passed in<br />  Rotate - change the current token to a different GUID and return the new GUID

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
model = swagger_client.QualerApiModelsAccountToLogoutModel() # QualerApiModelsAccountToLogoutModel | 

try:
    # Logout
    api_response = api_instance.account_logout(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_logout: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsAccountToLogoutModel**](QualerApiModelsAccountToLogoutModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **account_post_employee_location**
> object account_post_employee_location(model)

Post Employee Location

Sample request:                POST api/user/location                Latitude - The latitude in degrees.<br />  Longitude - The longitude in degrees.<br />  Accuracy - The radius of uncertainty for the location, measured in meters.<br />  Altitude - The altitude in meters above the WGS 84 reference ellipsoid.<br />  AltitudeAccuracy - The accuracy of the altitude value, in meters.<br />  Heading - Horizontal direction of travel of this device, measured in degrees starting at due north and continuing clockwise around the compass. Thus, north is 0 degrees, east is 90 degrees, south is 180 degrees, and so on.<br />  Speed - The instantaneous speed of the device in meters per second.<br />  Timestamp - The time at which this position information was obtained, in seconds.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountApi()
model = swagger_client.QualerApiModelsEmployeesFromEmployeeLocationModel() # QualerApiModelsEmployeesFromEmployeeLocationModel | 

try:
    # Post Employee Location
    api_response = api_instance.account_post_employee_location(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountApi->account_post_employee_location: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsEmployeesFromEmployeeLocationModel**](QualerApiModelsEmployeesFromEmployeeLocationModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

