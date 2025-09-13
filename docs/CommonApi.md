# qualer_sdk.CommonApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**culture_list**](CommonApi.md#culture_list) | **GET** /api/common/culturelist | 
[**culture_ui_list**](CommonApi.md#culture_ui_list) | **GET** /api/common/cultureuilist | 
[**get_company_settings**](CommonApi.md#get_company_settings) | **GET** /api/common/settings | 


# **culture_list**
> CommonToCultureListResponseModel culture_list()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CommonApi()

try:
    api_response = api_instance.culture_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->culture_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommonToCultureListResponseModel**](CommonToCultureListResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **culture_ui_list**
> CommonToCultureListResponseModel culture_ui_list()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CommonApi()

try:
    api_response = api_instance.culture_ui_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->culture_ui_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CommonToCultureListResponseModel**](CommonToCultureListResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_company_settings**
> CommonToSettingResponseModel get_company_settings(setting_key)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.CommonApi()
setting_key = 'setting_key_example' # str | 

try:
    api_response = api_instance.get_company_settings(setting_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->get_company_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_key** | **str**|  | 

### Return type

[**CommonToSettingResponseModel**](CommonToSettingResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

