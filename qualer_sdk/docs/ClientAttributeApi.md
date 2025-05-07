# swagger_client.ClientAttributeApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_attribute_get_client_attributes**](ClientAttributeApi.md#client_attribute_get_client_attributes) | **GET** /api/service/clients/{clientCompanyId}/attributes | 
[**client_attribute_upsert_client_attribute**](ClientAttributeApi.md#client_attribute_upsert_client_attribute) | **POST** /api/service/clients/{clientCompanyId}/attributes | 


# **client_attribute_get_client_attributes**
> object client_attribute_get_client_attributes(client_company_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientAttributeApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.client_attribute_get_client_attributes(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAttributeApi->client_attribute_get_client_attributes: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_attribute_upsert_client_attribute**
> object client_attribute_upsert_client_attribute(client_company_id, model)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientAttributeApi()
client_company_id = 56 # int | 
model = swagger_client.QualerApiModelsClientAttributesFromClientAttributeModel() # QualerApiModelsClientAttributesFromClientAttributeModel | 

try:
    api_response = api_instance.client_attribute_upsert_client_attribute(client_company_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientAttributeApi->client_attribute_upsert_client_attribute: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 
 **model** | [**QualerApiModelsClientAttributesFromClientAttributeModel**](QualerApiModelsClientAttributesFromClientAttributeModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

