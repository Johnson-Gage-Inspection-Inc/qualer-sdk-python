# coding: utf-8

"""
    Qualer.Web.Mvc

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class EmployeePreferenceApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def employee_preference_delete(self, element_page, **kwargs):  # noqa: E501
        """employee_preference_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_preference_delete(element_page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str element_page: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employee_preference_delete_with_http_info(element_page, **kwargs)  # noqa: E501
        else:
            (data) = self.employee_preference_delete_with_http_info(element_page, **kwargs)  # noqa: E501
            return data

    def employee_preference_delete_with_http_info(self, element_page, **kwargs):  # noqa: E501
        """employee_preference_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_preference_delete_with_http_info(element_page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str element_page: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['element_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employee_preference_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'element_page' is set
        if ('element_page' not in params or
                params['element_page'] is None):
            raise ValueError("Missing the required parameter `element_page` when calling `employee_preference_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'element_page' in params:
            path_params['elementPage'] = params['element_page']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/user/preferences/{elementPage}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def employee_preference_get(self, element_page, **kwargs):  # noqa: E501
        """employee_preference_get  # noqa: E501

        elementPage:  AssetManager = 1,  WorkOrders = 2,  ServiceOrderItems = 3,  ServiceSchedules = 4,  ServiceRequests = 5,  Vendors = 6,  VendorAgreements = 7,  ClientAgreements = 8,  WorkCalendar = 9,  Clients = 10,  GlobalAssetManager = 11,  InvoicesManager = 12,  ProductManager = 13,  ProductSpecifications = 14,  DocumentManager = 15  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_preference_get(element_page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str element_page: (required)
        :return: list[QualerApiModelsAssetToEmployeePreferenceResponseModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.employee_preference_get_with_http_info(element_page, **kwargs)  # noqa: E501
        else:
            (data) = self.employee_preference_get_with_http_info(element_page, **kwargs)  # noqa: E501
            return data

    def employee_preference_get_with_http_info(self, element_page, **kwargs):  # noqa: E501
        """employee_preference_get  # noqa: E501

        elementPage:  AssetManager = 1,  WorkOrders = 2,  ServiceOrderItems = 3,  ServiceSchedules = 4,  ServiceRequests = 5,  Vendors = 6,  VendorAgreements = 7,  ClientAgreements = 8,  WorkCalendar = 9,  Clients = 10,  GlobalAssetManager = 11,  InvoicesManager = 12,  ProductManager = 13,  ProductSpecifications = 14,  DocumentManager = 15  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.employee_preference_get_with_http_info(element_page, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str element_page: (required)
        :return: list[QualerApiModelsAssetToEmployeePreferenceResponseModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['element_page']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method employee_preference_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'element_page' is set
        if ('element_page' not in params or
                params['element_page'] is None):
            raise ValueError("Missing the required parameter `element_page` when calling `employee_preference_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'element_page' in params:
            path_params['elementPage'] = params['element_page']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/user/preferences/{elementPage}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[QualerApiModelsAssetToEmployeePreferenceResponseModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
