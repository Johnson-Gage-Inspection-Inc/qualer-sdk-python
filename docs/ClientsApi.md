# swagger_client.ClientsApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_create**](ClientsApi.md#clients_create) | **POST** /api/service/clients | Create Client information.
[**clients_get**](ClientsApi.md#clients_get) | **GET** /api/service/clients/{clientCompanyId} | 
[**clients_get_all**](ClientsApi.md#clients_get_all) | **GET** /api/service/clients | 
[**clients_update**](ClientsApi.md#clients_update) | **PUT** /api/service/clients | Update Client information.

# **clients_create**
> QualerApiModelsClientsToCreatedClientCompanyResponse clients_create(body)

Create Client information.

ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
body = swagger_client.QualerApiModelsClientsFromSponsoredClientCreateModel() # QualerApiModelsClientsFromSponsoredClientCreateModel | Client update model

try:
    # Create Client information.
    api_response = api_instance.clients_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsClientsFromSponsoredClientCreateModel**](QualerApiModelsClientsFromSponsoredClientCreateModel.md)| Client update model | 

### Return type

[**QualerApiModelsClientsToCreatedClientCompanyResponse**](QualerApiModelsClientsToCreatedClientCompanyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get**
> QualerApiModelsClientsToClientCompanyResponseModel clients_get(client_company_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.clients_get(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**QualerApiModelsClientsToClientCompanyResponseModel**](QualerApiModelsClientsToClientCompanyResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get_all**
> list[QualerApiModelsClientsToClientCompanyResponseModel] clients_get_all(model_legacy_id=model_legacy_id, model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
model_legacy_id = 'model_legacy_id_example' # str |  (optional)
model_account_number_text = 'model_account_number_text_example' # str |  (optional)
model_company_name = 'model_company_name_example' # str |  (optional)
model_take = 56 # int |  (optional)
model_modified_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.clients_get_all(model_legacy_id=model_legacy_id, model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_legacy_id** | **str**|  | [optional] 
 **model_account_number_text** | **str**|  | [optional] 
 **model_company_name** | **str**|  | [optional] 
 **model_take** | **int**|  | [optional] 
 **model_modified_after** | **datetime**|  | [optional] 

### Return type

[**list[QualerApiModelsClientsToClientCompanyResponseModel]**](QualerApiModelsClientsToClientCompanyResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_update**
> object clients_update(body)

Update Client information.

ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
body = swagger_client.QualerApiModelsClientsFromSponsoredClientEditModel() # QualerApiModelsClientsFromSponsoredClientEditModel | Client update model

try:
    # Update Client information.
    api_response = api_instance.clients_update(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsClientsFromSponsoredClientEditModel**](QualerApiModelsClientsFromSponsoredClientEditModel.md)| Client update model | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

