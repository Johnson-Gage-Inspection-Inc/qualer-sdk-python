# qualer_sdk.ProductApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_manufacturer**](ProductApi.md#add_manufacturer) | **POST** /api/manufacturers/add | 
[**add_product**](ProductApi.md#add_product) | **POST** /api/products/add | 
[**get_inventory_count**](ProductApi.md#get_inventory_count) | **GET** /api/products/inventorycount | 
[**get_manufacturers**](ProductApi.md#get_manufacturers) | **GET** /api/manufacturers | 
[**get_product**](ProductApi.md#get_product) | **GET** /api/products/{productId} | 
[**product**](ProductApi.md#product) | **PUT** /api/products/{productId} | 
[**put_inventory_count**](ProductApi.md#put_inventory_count) | **PUT** /api/products/inventorycount | 


# **add_manufacturer**
> object add_manufacturer(manufacturer_name)



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
    api_response = api_instance.add_manufacturer(manufacturer_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_manufacturer: %s\n" % e)
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

# **add_product**
> object add_product(model)



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
    api_response = api_instance.add_product(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->add_product: %s\n" % e)
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

# **get_inventory_count**
> list[InventoryToInventoryResponseModel] get_inventory_count()



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
    api_response = api_instance.get_inventory_count()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_inventory_count: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[InventoryToInventoryResponseModel]**](InventoryToInventoryResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_manufacturers**
> list[ProductToManufacturerResponseModel] get_manufacturers()



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
    api_response = api_instance.get_manufacturers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_manufacturers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductToManufacturerResponseModel]**](ProductToManufacturerResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_product**
> ProductToProductApiResponseModel get_product(product_id)



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
    api_response = api_instance.get_product(product_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->get_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product_id** | **int**|  | 

### Return type

[**ProductToProductApiResponseModel**](ProductToProductApiResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **product**
> object product(product_id, model)



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
    api_response = api_instance.product(product_id, model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->product: %s\n" % e)
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

# **put_inventory_count**
> object put_inventory_count(models)



### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.ProductApi()
models = [qualer_sdk.InventoryFromInventoryCountModel()] # list[InventoryFromInventoryCountModel] | 

try:
    api_response = api_instance.put_inventory_count(models)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductApi->put_inventory_count: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **models** | [**list[InventoryFromInventoryCountModel]**](InventoryFromInventoryCountModel.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

