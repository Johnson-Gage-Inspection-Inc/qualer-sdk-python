# swagger_client.VendorsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**vendors_create**](VendorsApi.md#vendors_create) | **POST** /api/service/vendors | Create Vendor information.
[**vendors_get**](VendorsApi.md#vendors_get) | **GET** /api/service/vendors/{vendorCompanyId} | 
[**vendors_get_all**](VendorsApi.md#vendors_get_all) | **GET** /api/service/vendors | 
[**vendors_update**](VendorsApi.md#vendors_update) | **PUT** /api/service/vendors | Update Vendor information.


# **vendors_create**
> QualerApiModelsVendorsToCreatedVendorCompanyResponse vendors_create(model)

Create Vendor information.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorsApi()
model = swagger_client.QualerApiModelsVendorsFromSponsoredVendorCreateModel() # QualerApiModelsVendorsFromSponsoredVendorCreateModel | Vendor update model

try:
    # Create Vendor information.
    api_response = api_instance.vendors_create(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsVendorsFromSponsoredVendorCreateModel**](QualerApiModelsVendorsFromSponsoredVendorCreateModel.md)| Vendor update model | 

### Return type

[**QualerApiModelsVendorsToCreatedVendorCompanyResponse**](QualerApiModelsVendorsToCreatedVendorCompanyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_get**
> QualerApiModelsVendorsToVendorCompanyResponseModel vendors_get(vendor_company_id)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorsApi()
vendor_company_id = 56 # int | 

try:
    api_response = api_instance.vendors_get(vendor_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_company_id** | **int**|  | 

### Return type

[**QualerApiModelsVendorsToVendorCompanyResponseModel**](QualerApiModelsVendorsToVendorCompanyResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_get_all**
> list[QualerApiModelsVendorsToVendorCompanyResponseModel] vendors_get_all(model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorsApi()
model_account_number_text = 'model_account_number_text_example' # str |  (optional)
model_company_name = 'model_company_name_example' # str |  (optional)
model_take = 56 # int |  (optional)
model_modified_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.vendors_get_all(model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors_get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_account_number_text** | **str**|  | [optional] 
 **model_company_name** | **str**|  | [optional] 
 **model_take** | **int**|  | [optional] 
 **model_modified_after** | **datetime**|  | [optional] 

### Return type

[**list[QualerApiModelsVendorsToVendorCompanyResponseModel]**](QualerApiModelsVendorsToVendorCompanyResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **vendors_update**
> object vendors_update(model)

Update Vendor information.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VendorsApi()
model = swagger_client.QualerApiModelsVendorsFromSponsoredVendorEditModel() # QualerApiModelsVendorsFromSponsoredVendorEditModel | Vendor update model

try:
    # Update Vendor information.
    api_response = api_instance.vendors_update(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->vendors_update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerApiModelsVendorsFromSponsoredVendorEditModel**](QualerApiModelsVendorsFromSponsoredVendorEditModel.md)| Vendor update model | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

