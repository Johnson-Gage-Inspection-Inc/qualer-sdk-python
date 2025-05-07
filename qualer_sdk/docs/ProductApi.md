# qualer_sdk.ProductApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**product_add_manufacturer**](ProductApi.md#product_add_manufacturer) | **POST** /api/manufacturers/add | 
[**product_add_product**](ProductApi.md#product_add_product) | **POST** /api/products/add | 
[**product_get_inventory_count**](ProductApi.md#product_get_inventory_count) | **GET** /api/products/inventorycount | 
[**product_get_manufacturers**](ProductApi.md#product_get_manufacturers) | **GET** /api/manufacturers | 
[**product_get_product**](ProductApi.md#product_get_product) | **GET** /api/products/{productId} | 
[**product_product**](ProductApi.md#product_product) | **PUT** /api/products/{productId} | 
[**product_put_inventory_count**](ProductApi.md#product_put_inventory_count) | **PUT** /api/products/inventorycount | 


# **product_add_manufacturer**
> object product_add_manufacturer(manufacturer_name)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()
manufacturer_name = 'manufacturer_name_example' # str | 

try:
    api_response = api_instance.product_add_manufacturer(manufacturer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_add_manufacturer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **manufacturer_name** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_add_product**
> object product_add_product(model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()
model = qualer_sdk.QualerWebMvcAreasApiModelsProductFromProductApiEditModel() # QualerWebMvcAreasApiModelsProductFromProductApiEditModel | 

try:
    api_response = api_instance.product_add_product(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**QualerWebMvcAreasApiModelsProductFromProductApiEditModel**](QualerWebMvcAreasApiModelsProductFromProductApiEditModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_inventory_count**
> list[QualerApiModelsInventoryToInventoryResponseModel] product_get_inventory_count()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()

try:
    api_response = api_instance.product_get_inventory_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_get_inventory_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsInventoryToInventoryResponseModel]**](QualerApiModelsInventoryToInventoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_manufacturers**
> list[QualerApiModelsProductToManufacturerResponseModel] product_get_manufacturers()



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()

try:
    api_response = api_instance.product_get_manufacturers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_get_manufacturers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[QualerApiModelsProductToManufacturerResponseModel]**](QualerApiModelsProductToManufacturerResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_get_product**
> QualerApiModelsProductToProductApiResponseModel product_get_product(product_id)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()
product_id = 56 # int | 

try:
    api_response = api_instance.product_get_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 

### Return type

[**QualerApiModelsProductToProductApiResponseModel**](QualerApiModelsProductToProductApiResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_product**
> object product_product(product_id, model)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()
product_id = 56 # int | 
model = qualer_sdk.QualerWebMvcAreasApiModelsProductFromProductApiEditModel() # QualerWebMvcAreasApiModelsProductFromProductApiEditModel | 

try:
    api_response = api_instance.product_product(product_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 
 **model** | [**QualerWebMvcAreasApiModelsProductFromProductApiEditModel**](QualerWebMvcAreasApiModelsProductFromProductApiEditModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product_put_inventory_count**
> object product_put_inventory_count(models)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()
models = [qualer_sdk.QualerApiModelsInventoryFromInventoryCountModel()] # list[QualerApiModelsInventoryFromInventoryCountModel] | 

try:
    api_response = api_instance.product_put_inventory_count(models)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product_put_inventory_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models** | [**list[QualerApiModelsInventoryFromInventoryCountModel]**](QualerApiModelsInventoryFromInventoryCountModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

