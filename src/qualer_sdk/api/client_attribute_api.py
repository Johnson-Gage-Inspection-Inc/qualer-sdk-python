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


class ClientAttributeApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_client_attributes(self, client_company_id, **kwargs):  # noqa: E501
        """get_client_attributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_attributes(client_company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_company_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_client_attributes_with_http_info(
                client_company_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.get_client_attributes_with_http_info(
                client_company_id, **kwargs
            )  # noqa: E501
            return data

    def get_client_attributes_with_http_info(
        self, client_company_id, **kwargs
    ):  # noqa: E501
        """get_client_attributes  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_client_attributes_with_http_info(client_company_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_company_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["client_company_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_client_attributes" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'client_company_id' is set
        if self.api_client.client_side_validation and (
            "client_company_id" not in params or params["client_company_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `client_company_id` when calling `get_client_attributes`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "client_company_id" in params:
            path_params["clientCompanyId"] = params["client_company_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json", "application/xml", "text/xml"]
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/service/clients/{clientCompanyId}/attributes",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def upsert_client_attribute(self, client_company_id, model, **kwargs):  # noqa: E501
        """upsert_client_attribute  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_client_attribute(client_company_id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_company_id: (required)
        :param QualerApiModelsClientAttributesFromClientAttributeModel model: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.upsert_client_attribute_with_http_info(
                client_company_id, model, **kwargs
            )  # noqa: E501
        else:
            (data) = self.upsert_client_attribute_with_http_info(
                client_company_id, model, **kwargs
            )  # noqa: E501
            return data

    def upsert_client_attribute_with_http_info(
        self, client_company_id, model, **kwargs
    ):  # noqa: E501
        """upsert_client_attribute  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.upsert_client_attribute_with_http_info(client_company_id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int client_company_id: (required)
        :param QualerApiModelsClientAttributesFromClientAttributeModel model: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["client_company_id", "model"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method upsert_client_attribute" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'client_company_id' is set
        if self.api_client.client_side_validation and (
            "client_company_id" not in params or params["client_company_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `client_company_id` when calling `upsert_client_attribute`"
            )  # noqa: E501
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and (
            "model" not in params or params["model"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `model` when calling `upsert_client_attribute`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "client_company_id" in params:
            path_params["clientCompanyId"] = params["client_company_id"]  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if "model" in params:
            body_params = params["model"]
        # HTTP header `Accept`
        header_params["Accept"] = self.api_client.select_header_accept(
            ["application/json", "text/json", "application/xml", "text/xml"]
        )  # noqa: E501

        # HTTP header `Content-Type`
        header_params["Content-Type"] = (
            self.api_client.select_header_content_type(  # noqa: E501
                [
                    "application/json",
                    "text/json",
                    "application/xml",
                    "text/xml",
                    "application/x-www-form-urlencoded",
                ]
            )
        )  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            "/api/service/clients/{clientCompanyId}/attributes",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="object",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )
