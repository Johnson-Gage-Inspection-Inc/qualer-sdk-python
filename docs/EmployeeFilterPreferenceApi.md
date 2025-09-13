# qualer_sdk.EmployeeFilterPreferenceApi

All URIs are relative to *https://jgiquality.qualer.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_employee_filter_preferences**](EmployeeFilterPreferenceApi.md#get_employee_filter_preferences) | **GET** /api/user/filters | GetEmployeeFilterPreferences
[**update_employee_filter_preference**](EmployeeFilterPreferenceApi.md#update_employee_filter_preference) | **PUT** /api/user/filters | UpdateEmployeeFilterPreference


# **get_employee_filter_preferences**
> list[AssetToEmployeeFilterPreferenceResponseModel] get_employee_filter_preferences()

GetEmployeeFilterPreferences

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeeFilterPreferenceApi()

try:
    # GetEmployeeFilterPreferences
    api_response = api_instance.get_employee_filter_preferences()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeFilterPreferenceApi->get_employee_filter_preferences: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[AssetToEmployeeFilterPreferenceResponseModel]**](AssetToEmployeeFilterPreferenceResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_employee_filter_preference**
> object update_employee_filter_preference(model)

UpdateEmployeeFilterPreference

### Example
```python
from __future__ import print_function
import time
import qualer_sdk
from qualer_sdk.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = qualer_sdk.EmployeeFilterPreferenceApi()
model = qualer_sdk.AssetFromUpdateFilterPreferenceModel() # AssetFromUpdateFilterPreferenceModel | FilterType: \\  DueForService(AssetsDue), RecentlyServiced(AssetsRecentlyServiced), NotServiced(AssetsNotServiced), \\  RecentlyPurchased(AssetsRecentlyPurchased), WarrantyExpiring(AssetsWarrantyExpires), \\  DueForReplacement(AssetsDueForReplacement), ServicePending(AssetsServicePending) \\                WithinDays: 30                UseDateRange: true, false                StartDate: '2020-01-01' optional                EndDate: '2020-05-31' optional

try:
    # UpdateEmployeeFilterPreference
    api_response = api_instance.update_employee_filter_preference(model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EmployeeFilterPreferenceApi->update_employee_filter_preference: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **model** | [**AssetFromUpdateFilterPreferenceModel**](AssetFromUpdateFilterPreferenceModel.md)| FilterType: \\  DueForService(AssetsDue), RecentlyServiced(AssetsRecentlyServiced), NotServiced(AssetsNotServiced), \\  RecentlyPurchased(AssetsRecentlyPurchased), WarrantyExpiring(AssetsWarrantyExpires), \\  DueForReplacement(AssetsDueForReplacement), ServicePending(AssetsServicePending) \\                WithinDays: 30                UseDateRange: true, false                StartDate: &#39;2020-01-01&#39; optional                EndDate: &#39;2020-05-31&#39; optional | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

