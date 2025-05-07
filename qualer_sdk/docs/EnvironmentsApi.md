# qualer_sdk.EnvironmentsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**environments_get**](EnvironmentsApi.md#environments_get) | **GET** /api/Environments/{id} | 
[**environments_post**](EnvironmentsApi.md#environments_post) | **POST** /api/Environments/{id} | 


# **environments_get**
> list[QualerApiModelsEnvironmentToEnvironmentModel] environments_get(id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EnvironmentsApi()
id = 'id_example' # str | 

try:
    api_response = api_instance.environments_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->environments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**list[QualerApiModelsEnvironmentToEnvironmentModel]**](QualerApiModelsEnvironmentToEnvironmentModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **environments_post**
> object environments_post(model, id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EnvironmentsApi()
model = qualer_sdk.QualerApiModelsEnvironmentFromEnvironmentModel() # QualerApiModelsEnvironmentFromEnvironmentModel | 
id = 'id_example' # str | 

try:
    api_response = api_instance.environments_post(model, id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnvironmentsApi->environments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsEnvironmentFromEnvironmentModel**](QualerApiModelsEnvironmentFromEnvironmentModel.md)|  | 
 **id** | [**str**](.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

