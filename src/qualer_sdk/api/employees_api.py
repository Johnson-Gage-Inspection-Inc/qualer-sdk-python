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


class EmployeesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def add_employee_department(self, employee_id, model, **kwargs):  # noqa: E501
        """# noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_employee_department(employee_id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id:  (required)
        :param QualerApiModelsEmployeesFromEmployeeDepartmentModel model:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.add_employee_department_with_http_info(
                employee_id, model, **kwargs
            )  # noqa: E501
        else:
            (data) = self.add_employee_department_with_http_info(
                employee_id, model, **kwargs
            )  # noqa: E501
            return data

    def add_employee_department_with_http_info(
        self, employee_id, model, **kwargs
    ):  # noqa: E501
        """# noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_employee_department_with_http_info(employee_id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id:  (required)
        :param QualerApiModelsEmployeesFromEmployeeDepartmentModel model:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["employee_id", "model"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_employee_department" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'employee_id' is set
        if self.api_client.client_side_validation and (
            "employee_id" not in params or params["employee_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `employee_id` when calling `add_employee_department`"
            )  # noqa: E501
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and (
            "model" not in params or params["model"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `model` when calling `add_employee_department`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "employee_id" in params:
            path_params["employeeId"] = params["employee_id"]  # noqa: E501

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
            "/api/employees/{employeeId}/department",
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

    def create_employee(self, model, **kwargs):  # noqa: E501
        """Create Employee  # noqa: E501

        CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_employee(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QualerApiModelsEmployeesFromCreateEmployeeModel model: (required)
        :return: QualerApiModelsEmployeesToCreatedEmployeeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.create_employee_with_http_info(model, **kwargs)  # noqa: E501
        else:
            (data) = self.create_employee_with_http_info(model, **kwargs)  # noqa: E501
            return data

    def create_employee_with_http_info(self, model, **kwargs):  # noqa: E501
        """Create Employee  # noqa: E501

        CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_employee_with_http_info(model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param QualerApiModelsEmployeesFromCreateEmployeeModel model: (required)
        :return: QualerApiModelsEmployeesToCreatedEmployeeResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["model"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_employee" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and (
            "model" not in params or params["model"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `model` when calling `create_employee`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}

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
            "/api/employees",
            "POST",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="QualerApiModelsEmployeesToCreatedEmployeeResponse",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def delete_employee_department(
        self, employee_id, department_id, **kwargs
    ):  # noqa: E501
        """# noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_employee_department(employee_id, department_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id:  (required)
        :param int department_id:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.delete_employee_department_with_http_info(
                employee_id, department_id, **kwargs
            )  # noqa: E501
        else:
            (data) = self.delete_employee_department_with_http_info(
                employee_id, department_id, **kwargs
            )  # noqa: E501
            return data

    def delete_employee_department_with_http_info(
        self, employee_id, department_id, **kwargs
    ):  # noqa: E501
        """# noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_employee_department_with_http_info(employee_id, department_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id:  (required)
        :param int department_id:  (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["employee_id", "department_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_employee_department" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'employee_id' is set
        if self.api_client.client_side_validation and (
            "employee_id" not in params or params["employee_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `employee_id` when calling `delete_employee_department`"
            )  # noqa: E501
        # verify the required parameter 'department_id' is set
        if self.api_client.client_side_validation and (
            "department_id" not in params or params["department_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `department_id` when calling `delete_employee_department`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "employee_id" in params:
            path_params["employeeId"] = params["employee_id"]  # noqa: E501
        if "department_id" in params:
            path_params["departmentId"] = params["department_id"]  # noqa: E501

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
            "/api/employees/{employeeId}/department/{departmentId}",
            "DELETE",
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

    def get_employee(self, employee_id, **kwargs):  # noqa: E501
        """get_employee  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_employee(employee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id: (required)
        :return: QualerApiModelsClientsToEmployeeResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_employee_with_http_info(employee_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_employee_with_http_info(
                employee_id, **kwargs
            )  # noqa: E501
            return data

    def get_employee_with_http_info(self, employee_id, **kwargs):  # noqa: E501
        """get_employee  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_employee_with_http_info(employee_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id: (required)
        :return: QualerApiModelsClientsToEmployeeResponseModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["employee_id"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_employee" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'employee_id' is set
        if self.api_client.client_side_validation and (
            "employee_id" not in params or params["employee_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `employee_id` when calling `get_employee`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "employee_id" in params:
            path_params["employeeId"] = params["employee_id"]  # noqa: E501

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
            "/api/employees/{employeeId}",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="QualerApiModelsClientsToEmployeeResponseModel",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def get_employees(self, **kwargs):  # noqa: E501
        """get_employees  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_employees(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str model_search_string:
        :return: list[QualerApiModelsClientsToEmployeeResponseModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.get_employees_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.get_employees_with_http_info(**kwargs)  # noqa: E501
            return data

    def get_employees_with_http_info(self, **kwargs):  # noqa: E501
        """get_employees  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_employees_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str model_search_string:
        :return: list[QualerApiModelsClientsToEmployeeResponseModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["model_search_string"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_employees" % key
                )
            params[key] = val
        del params["kwargs"]

        collection_formats = {}

        path_params = {}

        query_params = []
        if "model_search_string" in params:
            query_params.append(
                ("model.searchString", params["model_search_string"])
            )  # noqa: E501

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
            "/api/employees",
            "GET",
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type="list[QualerApiModelsClientsToEmployeeResponseModel]",  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get("async_req"),
            _return_http_data_only=params.get("_return_http_data_only"),
            _preload_content=params.get("_preload_content", True),
            _request_timeout=params.get("_request_timeout"),
            collection_formats=collection_formats,
        )

    def update_employee(self, employee_id, model, **kwargs):  # noqa: E501
        """Update Employee  # noqa: E501

        CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_employee(employee_id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id: (required)
        :param QualerApiModelsEmployeesFromUpdateEmployeeModel model: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs["_return_http_data_only"] = True
        if kwargs.get("async_req"):
            return self.update_employee_with_http_info(
                employee_id, model, **kwargs
            )  # noqa: E501
        else:
            (data) = self.update_employee_with_http_info(
                employee_id, model, **kwargs
            )  # noqa: E501
            return data

    def update_employee_with_http_info(
        self, employee_id, model, **kwargs
    ):  # noqa: E501
        """Update Employee  # noqa: E501

        CultureName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\".<br />  CultureUiName examples: \"en-US\", \"en-AU\" , \"de-DE\", \"es-ES\"<br />  List of culture codes: GET /api/common/culturelist\"  List of UI culture codes: GET /api/common/cultureuilist\"  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_employee_with_http_info(employee_id, model, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int employee_id: (required)
        :param QualerApiModelsEmployeesFromUpdateEmployeeModel model: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ["employee_id", "model"]  # noqa: E501
        all_params.append("async_req")
        all_params.append("_return_http_data_only")
        all_params.append("_preload_content")
        all_params.append("_request_timeout")

        params = locals()
        for key, val in six.iteritems(params["kwargs"]):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_employee" % key
                )
            params[key] = val
        del params["kwargs"]
        # verify the required parameter 'employee_id' is set
        if self.api_client.client_side_validation and (
            "employee_id" not in params or params["employee_id"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `employee_id` when calling `update_employee`"
            )  # noqa: E501
        # verify the required parameter 'model' is set
        if self.api_client.client_side_validation and (
            "model" not in params or params["model"] is None
        ):  # noqa: E501
            raise ValueError(
                "Missing the required parameter `model` when calling `update_employee`"
            )  # noqa: E501

        collection_formats = {}

        path_params = {}
        if "employee_id" in params:
            path_params["employeeId"] = params["employee_id"]  # noqa: E501

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
            "/api/employees/{employeeId}",
            "PUT",
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
