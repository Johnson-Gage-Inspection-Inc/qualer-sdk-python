# qualer_sdk.VendorsApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create**](VendorsApi.md#create) | **POST** /api/service/vendors | Create Vendor information.
[**get**](VendorsApi.md#get) | **GET** /api/service/vendors/{vendorCompanyId} | 
[**get_all**](VendorsApi.md#get_all) | **GET** /api/service/vendors | 
[**update**](VendorsApi.md#update) | **PUT** /api/service/vendors | Update Vendor information.


# **create**
> VendorsToCreatedVendorCompanyResponse create(model)

Create Vendor information.



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.VendorsApi()
model = qualer_sdk.VendorsFromSponsoredVendorCreateModel() # VendorsFromSponsoredVendorCreateModel | Vendor update model

try:
    # Create Vendor information.
    api_response = api_instance.create(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**VendorsFromSponsoredVendorCreateModel**](VendorsFromSponsoredVendorCreateModel.md)| Vendor update model | 

### Return type

[**VendorsToCreatedVendorCompanyResponse**](VendorsToCreatedVendorCompanyResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get**
> VendorsToVendorCompanyResponseModel get(vendor_company_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.VendorsApi()
vendor_company_id = 56 # int | 

try:
    api_response = api_instance.get(vendor_company_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **vendor_company_id** | **int**|  | 

### Return type

[**VendorsToVendorCompanyResponseModel**](VendorsToVendorCompanyResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_all**
> list[VendorsToVendorCompanyResponseModel] get_all(model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.VendorsApi()
model_account_number_text = 'model_account_number_text_example' # str |  (optional)
model_company_name = 'model_company_name_example' # str |  (optional)
model_take = 56 # int |  (optional)
model_modified_after = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.get_all(model_account_number_text=model_account_number_text, model_company_name=model_company_name, model_take=model_take, model_modified_after=model_modified_after)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->get_all: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model_account_number_text** | **str**|  | [optional] 
 **model_company_name** | **str**|  | [optional] 
 **model_take** | **int**|  | [optional] 
 **model_modified_after** | **datetime**|  | [optional] 

### Return type

[**list[VendorsToVendorCompanyResponseModel]**](VendorsToVendorCompanyResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update**
> object update(model)

Update Vendor information.



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.VendorsApi()
model = qualer_sdk.VendorsFromSponsoredVendorEditModel() # VendorsFromSponsoredVendorEditModel | Vendor update model

try:
    # Update Vendor information.
    api_response = api_instance.update(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VendorsApi->update: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**VendorsFromSponsoredVendorEditModel**](VendorsFromSponsoredVendorEditModel.md)| Vendor update model | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

