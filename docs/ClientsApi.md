# qualer_sdk.ClientsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](ClientsApi.md#create) | **POST** /api/service/clients | Create Client information.
[**get**](ClientsApi.md#get) | **GET** /api/service/clients/{clientCompanyId} | 
[**get_all**](ClientsApi.md#get_all) | **GET** /api/service/clients | 
[**update**](ClientsApi.md#update) | **PUT** /api/service/clients | Update Client information.


# **create**
> QualerApiModelsClientsToCreatedClientCompanyResponse create(model)

Create Client information.

ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientsApi()
model = qualer_sdk.QualerApiModelsClientsFromSponsoredClientCreateModel() # QualerApiModelsClientsFromSponsoredClientCreateModel | Client update model

try:
    # Create Client information.
    api_response = api_instance.create(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsClientsFromSponsoredClientCreateModel**](QualerApiModelsClientsFromSponsoredClientCreateModel.md)| Client update model | 

### Return type

[**QualerApiModelsClientsToCreatedClientCompanyResponse**](QualerApiModelsClientsToCreatedClientCompanyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> QualerApiModelsClientsToClientCompanyResponseModel get(client_company_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientsApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.get(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get: %s\n" % e)
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

# **get_all**
> list[QualerApiModelsClientsToClientCompanyResponseModel] get_all(model_legacy_id=model_legacy_id, model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientsApi()
model_legacy_id = 'model_legacy_id_example' # str |  (optional)
model_account_number_text = 'model_account_number_text_example' # str |  (optional)
model_company_name = 'model_company_name_example' # str |  (optional)
model_take = 56 # int |  (optional)
model_modified_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_all(model_legacy_id=model_legacy_id, model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->get_all: %s\n" % e)
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

# **update**
> object update(model)

Update Client information.

ClientStatus: Prospect = 0, Approved = 1, NotApproved = 2, Hidden = 3

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ClientsApi()
model = qualer_sdk.QualerApiModelsClientsFromSponsoredClientEditModel() # QualerApiModelsClientsFromSponsoredClientEditModel | Client update model

try:
    # Update Client information.
    api_response = api_instance.update(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsClientsFromSponsoredClientEditModel**](QualerApiModelsClientsFromSponsoredClientEditModel.md)| Client update model | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

