# swagger_client.CommonApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**common_culture_list**](CommonApi.md#common_culture_list) | **GET** /api/common/culturelist | 
[**common_culture_ui_list**](CommonApi.md#common_culture_ui_list) | **GET** /api/common/cultureuilist | 
[**common_get_company_settings**](CommonApi.md#common_get_company_settings) | **GET** /api/common/settings | 


# **common_culture_list**
> QualerApiModelsCommonToCultureListResponseModel common_culture_list()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()

try:
    api_response = api_instance.common_culture_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->common_culture_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QualerApiModelsCommonToCultureListResponseModel**](QualerApiModelsCommonToCultureListResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_culture_ui_list**
> QualerApiModelsCommonToCultureListResponseModel common_culture_ui_list()



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()

try:
    api_response = api_instance.common_culture_ui_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->common_culture_ui_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**QualerApiModelsCommonToCultureListResponseModel**](QualerApiModelsCommonToCultureListResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **common_get_company_settings**
> QualerApiModelsCommonToSettingResponseModel common_get_company_settings(setting_key)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommonApi()
setting_key = 'setting_key_example' # str | 

try:
    api_response = api_instance.common_get_company_settings(setting_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommonApi->common_get_company_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **setting_key** | **str**|  | 

### Return type

[**QualerApiModelsCommonToSettingResponseModel**](QualerApiModelsCommonToSettingResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

