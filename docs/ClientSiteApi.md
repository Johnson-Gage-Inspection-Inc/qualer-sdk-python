# swagger_client.ClientSiteApi

All URIs are relative to *https://jgiquality.qualer.com/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**client_site_create_client_site**](ClientSiteApi.md#client_site_create_client_site) | **POST** /api/service/clients/{clientCompanyId}/sites | Create Client Site.
[**client_site_get_client_sites**](ClientSiteApi.md#client_site_get_client_sites) | **GET** /api/service/clients/{clientCompanyId}/sites | 
[**client_site_update_client_site**](ClientSiteApi.md#client_site_update_client_site) | **PUT** /api/service/clients/{clientCompanyId}/sites | Update Client Site.

# **client_site_create_client_site**
> object client_site_create_client_site(body, client_company_id)

Create Client Site.

CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientSiteApi()
body = swagger_client.QualerApiModelsSiteFromSiteCreateModel() # QualerApiModelsSiteFromSiteCreateModel | Site create model
client_company_id = 56 # int | Client Company Id

try:
    # Create Client Site.
    api_response = api_instance.client_site_create_client_site(body, client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientSiteApi->client_site_create_client_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsSiteFromSiteCreateModel**](QualerApiModelsSiteFromSiteCreateModel.md)| Site create model | 
 **client_company_id** | **int**| Client Company Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_site_get_client_sites**
> list[QualerApiModelsSiteToClientSiteResponse] client_site_get_client_sites(client_company_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientSiteApi()
client_company_id = 56 # int | 

try:
    api_response = api_instance.client_site_get_client_sites(client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientSiteApi->client_site_get_client_sites: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client_company_id** | **int**|  | 

### Return type

[**list[QualerApiModelsSiteToClientSiteResponse]**](QualerApiModelsSiteToClientSiteResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **client_site_update_client_site**
> object client_site_update_client_site(body, client_company_id)

Update Client Site.

CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientSiteApi()
body = swagger_client.QualerApiModelsSiteFromSiteUpdateModel() # QualerApiModelsSiteFromSiteUpdateModel | Site update model
client_company_id = 56 # int | Client Company Id

try:
    # Update Client Site.
    api_response = api_instance.client_site_update_client_site(body, client_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientSiteApi->client_site_update_client_site: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**QualerApiModelsSiteFromSiteUpdateModel**](QualerApiModelsSiteFromSiteUpdateModel.md)| Site update model | 
 **client_company_id** | **int**| Client Company Id | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

