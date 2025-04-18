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

from qualer_sdk.api_client import ApiClient


class ServiceOrderShipmentsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def service_order_shipments_append_shipment_tracking_number(self, body, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_append_shipment_tracking_number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_append_shipment_tracking_number(body, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QualerApiModelsServiceOrdersFromAppendTrackingNumberModel body: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_order_shipments_append_shipment_tracking_number_with_http_info(body, service_order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.service_order_shipments_append_shipment_tracking_number_with_http_info(body, service_order_id, **kwargs)  # noqa: E501
            return data

    def service_order_shipments_append_shipment_tracking_number_with_http_info(self, body, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_append_shipment_tracking_number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_append_shipment_tracking_number_with_http_info(body, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QualerApiModelsServiceOrdersFromAppendTrackingNumberModel body: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'service_order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_order_shipments_append_shipment_tracking_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `service_order_shipments_append_shipment_tracking_number`")  # noqa: E501
        # verify the required parameter 'service_order_id' is set
        if ('service_order_id' not in params or
                params['service_order_id'] is None):
            raise ValueError("Missing the required parameter `service_order_id` when calling `service_order_shipments_append_shipment_tracking_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_order_id' in params:
            path_params['serviceOrderId'] = params['service_order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'tracking_number' in params:
            form_params.append(('TrackingNumber', params['tracking_number']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/service/workorders/{serviceOrderId}/shipments/trackingnumber', 'PUT',
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

    def service_order_shipments_append_shipment_tracking_number(self, tracking_number, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_append_shipment_tracking_number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_append_shipment_tracking_number(tracking_number, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tracking_number: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_order_shipments_append_shipment_tracking_number_with_http_info(tracking_number, service_order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.service_order_shipments_append_shipment_tracking_number_with_http_info(tracking_number, service_order_id, **kwargs)  # noqa: E501
            return data

    def service_order_shipments_append_shipment_tracking_number_with_http_info(self, tracking_number, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_append_shipment_tracking_number  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_append_shipment_tracking_number_with_http_info(tracking_number, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str tracking_number: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tracking_number', 'service_order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_order_shipments_append_shipment_tracking_number" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'tracking_number' is set
        if ('tracking_number' not in params or
                params['tracking_number'] is None):
            raise ValueError("Missing the required parameter `tracking_number` when calling `service_order_shipments_append_shipment_tracking_number`")  # noqa: E501
        # verify the required parameter 'service_order_id' is set
        if ('service_order_id' not in params or
                params['service_order_id'] is None):
            raise ValueError("Missing the required parameter `service_order_id` when calling `service_order_shipments_append_shipment_tracking_number`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_order_id' in params:
            path_params['serviceOrderId'] = params['service_order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'tracking_number' in params:
            form_params.append(('TrackingNumber', params['tracking_number']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/service/workorders/{serviceOrderId}/shipments/trackingnumber', 'PUT',
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

    def service_order_shipments_update_shipment_status(self, body, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_update_shipment_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_update_shipment_status(body, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel body: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_order_shipments_update_shipment_status_with_http_info(body, service_order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.service_order_shipments_update_shipment_status_with_http_info(body, service_order_id, **kwargs)  # noqa: E501
            return data

    def service_order_shipments_update_shipment_status_with_http_info(self, body, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_update_shipment_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_update_shipment_status_with_http_info(body, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QualerApiModelsServiceOrdersFromUpdateShipmentStatusModel body: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'service_order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_order_shipments_update_shipment_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `service_order_shipments_update_shipment_status`")  # noqa: E501
        # verify the required parameter 'service_order_id' is set
        if ('service_order_id' not in params or
                params['service_order_id'] is None):
            raise ValueError("Missing the required parameter `service_order_id` when calling `service_order_shipments_update_shipment_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_order_id' in params:
            path_params['serviceOrderId'] = params['service_order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'shipment_status' in params:
            form_params.append(('ShipmentStatus', params['shipment_status']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/service/workorders/{serviceOrderId}/shipments/status', 'PUT',
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

    def service_order_shipments_update_shipment_status(self, shipment_status, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_update_shipment_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_update_shipment_status(shipment_status, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_status: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.service_order_shipments_update_shipment_status_with_http_info(shipment_status, service_order_id, **kwargs)  # noqa: E501
        else:
            (data) = self.service_order_shipments_update_shipment_status_with_http_info(shipment_status, service_order_id, **kwargs)  # noqa: E501
            return data

    def service_order_shipments_update_shipment_status_with_http_info(self, shipment_status, service_order_id, **kwargs):  # noqa: E501
        """service_order_shipments_update_shipment_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.service_order_shipments_update_shipment_status_with_http_info(shipment_status, service_order_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str shipment_status: (required)
        :param int service_order_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['shipment_status', 'service_order_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method service_order_shipments_update_shipment_status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'shipment_status' is set
        if ('shipment_status' not in params or
                params['shipment_status'] is None):
            raise ValueError("Missing the required parameter `shipment_status` when calling `service_order_shipments_update_shipment_status`")  # noqa: E501
        # verify the required parameter 'service_order_id' is set
        if ('service_order_id' not in params or
                params['service_order_id'] is None):
            raise ValueError("Missing the required parameter `service_order_id` when calling `service_order_shipments_update_shipment_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service_order_id' in params:
            path_params['serviceOrderId'] = params['service_order_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'shipment_status' in params:
            form_params.append(('ShipmentStatus', params['shipment_status']))  # noqa: E501

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json', 'application/xml', 'text/xml'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/service/workorders/{serviceOrderId}/shipments/status', 'PUT',
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
