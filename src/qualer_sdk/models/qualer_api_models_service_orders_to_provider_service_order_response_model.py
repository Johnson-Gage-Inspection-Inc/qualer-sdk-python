# coding: utf-8

"""
Qualer.Web.Mvc

No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

OpenAPI spec version: v1

Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from qualer_sdk.configuration import Configuration


class QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        "service_order_id": "int",
        "guid": "str",
        "service_order_number": "int",
        "custom_order_number": "str",
        "due_date": "datetime",
        "assets": "int",
        "completed_assets": "int",
        "order_status": "str",
        "is_quality_control_fail": "bool",
        "service_private_comments": "str",
        "client_company_id": "int",
        "client_company_name": "str",
        "client_site_name": "str",
        "client_legacy_id": "str",
        "business_from_time": "datetime",
        "business_to_time": "datetime",
        "timeframe": "str",
        "site_access_notes": "str",
        "desired_date": "datetime",
        "deadline_date": "datetime",
        "request_from_date": "datetime",
        "request_from_time": "datetime",
        "request_to_date": "datetime",
        "request_to_time": "datetime",
    }

    attribute_map = {
        "service_order_id": "ServiceOrderId",
        "guid": "Guid",
        "service_order_number": "ServiceOrderNumber",
        "custom_order_number": "CustomOrderNumber",
        "due_date": "DueDate",
        "assets": "Assets",
        "completed_assets": "CompletedAssets",
        "order_status": "OrderStatus",
        "is_quality_control_fail": "IsQualityControlFail",
        "service_private_comments": "ServicePrivateComments",
        "client_company_id": "ClientCompanyId",
        "client_company_name": "ClientCompanyName",
        "client_site_name": "ClientSiteName",
        "client_legacy_id": "ClientLegacyId",
        "business_from_time": "BusinessFromTime",
        "business_to_time": "BusinessToTime",
        "timeframe": "Timeframe",
        "site_access_notes": "SiteAccessNotes",
        "desired_date": "DesiredDate",
        "deadline_date": "DeadlineDate",
        "request_from_date": "RequestFromDate",
        "request_from_time": "RequestFromTime",
        "request_to_date": "RequestToDate",
        "request_to_time": "RequestToTime",
    }

    def __init__(
        self,
        service_order_id=None,
        guid=None,
        service_order_number=None,
        custom_order_number=None,
        due_date=None,
        assets=None,
        completed_assets=None,
        order_status=None,
        is_quality_control_fail=None,
        service_private_comments=None,
        client_company_id=None,
        client_company_name=None,
        client_site_name=None,
        client_legacy_id=None,
        business_from_time=None,
        business_to_time=None,
        timeframe=None,
        site_access_notes=None,
        desired_date=None,
        deadline_date=None,
        request_from_date=None,
        request_from_time=None,
        request_to_date=None,
        request_to_time=None,
        _configuration=None,
    ):  # noqa: E501
        """QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._service_order_id = None
        self._guid = None
        self._service_order_number = None
        self._custom_order_number = None
        self._due_date = None
        self._assets = None
        self._completed_assets = None
        self._order_status = None
        self._is_quality_control_fail = None
        self._service_private_comments = None
        self._client_company_id = None
        self._client_company_name = None
        self._client_site_name = None
        self._client_legacy_id = None
        self._business_from_time = None
        self._business_to_time = None
        self._timeframe = None
        self._site_access_notes = None
        self._desired_date = None
        self._deadline_date = None
        self._request_from_date = None
        self._request_from_time = None
        self._request_to_date = None
        self._request_to_time = None
        self.discriminator = None

        if service_order_id is not None:
            self.service_order_id = service_order_id
        if guid is not None:
            self.guid = guid
        if service_order_number is not None:
            self.service_order_number = service_order_number
        if custom_order_number is not None:
            self.custom_order_number = custom_order_number
        if due_date is not None:
            self.due_date = due_date
        if assets is not None:
            self.assets = assets
        if completed_assets is not None:
            self.completed_assets = completed_assets
        if order_status is not None:
            self.order_status = order_status
        if is_quality_control_fail is not None:
            self.is_quality_control_fail = is_quality_control_fail
        if service_private_comments is not None:
            self.service_private_comments = service_private_comments
        if client_company_id is not None:
            self.client_company_id = client_company_id
        if client_company_name is not None:
            self.client_company_name = client_company_name
        if client_site_name is not None:
            self.client_site_name = client_site_name
        if client_legacy_id is not None:
            self.client_legacy_id = client_legacy_id
        if business_from_time is not None:
            self.business_from_time = business_from_time
        if business_to_time is not None:
            self.business_to_time = business_to_time
        if timeframe is not None:
            self.timeframe = timeframe
        if site_access_notes is not None:
            self.site_access_notes = site_access_notes
        if desired_date is not None:
            self.desired_date = desired_date
        if deadline_date is not None:
            self.deadline_date = deadline_date
        if request_from_date is not None:
            self.request_from_date = request_from_date
        if request_from_time is not None:
            self.request_from_time = request_from_time
        if request_to_date is not None:
            self.request_to_date = request_to_date
        if request_to_time is not None:
            self.request_to_time = request_to_time

    @property
    def service_order_id(self):
        """Gets the service_order_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The service_order_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_order_id

    @service_order_id.setter
    def service_order_id(self, service_order_id):
        """Sets the service_order_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param service_order_id: The service_order_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: int
        """

        self._service_order_id = service_order_id

    @property
    def guid(self):
        """Gets the guid of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The guid of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._guid

    @guid.setter
    def guid(self, guid):
        """Sets the guid of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param guid: The guid of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._guid = guid

    @property
    def service_order_number(self):
        """Gets the service_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The service_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_order_number

    @service_order_number.setter
    def service_order_number(self, service_order_number):
        """Sets the service_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param service_order_number: The service_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: int
        """

        self._service_order_number = service_order_number

    @property
    def custom_order_number(self):
        """Gets the custom_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The custom_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._custom_order_number

    @custom_order_number.setter
    def custom_order_number(self, custom_order_number):
        """Sets the custom_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param custom_order_number: The custom_order_number of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._custom_order_number = custom_order_number

    @property
    def due_date(self):
        """Gets the due_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The due_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param due_date: The due_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._due_date = due_date

    @property
    def assets(self):
        """Gets the assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._assets

    @assets.setter
    def assets(self, assets):
        """Sets the assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param assets: The assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: int
        """

        self._assets = assets

    @property
    def completed_assets(self):
        """Gets the completed_assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The completed_assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._completed_assets

    @completed_assets.setter
    def completed_assets(self, completed_assets):
        """Sets the completed_assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param completed_assets: The completed_assets of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: int
        """

        self._completed_assets = completed_assets

    @property
    def order_status(self):
        """Gets the order_status of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The order_status of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._order_status

    @order_status.setter
    def order_status(self, order_status):
        """Sets the order_status of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param order_status: The order_status of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "New",
            "Draft",
            "WaitingForApproval",
            "Submitted",
            "Processing",
            "QualityControl",
            "Cancelled",
            "WaitingForClientSignOff",
            "Completed",
            "Denied",
            "Delayed",
            "Scheduling",
            "Closed",
            "WaitingForVendorSignOff",
            "DelayedApproval",
            "Ready",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and order_status not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `order_status` ({0}), must be one of {1}".format(  # noqa: E501
                    order_status, allowed_values
                )
            )

        self._order_status = order_status

    @property
    def is_quality_control_fail(self):
        """Gets the is_quality_control_fail of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The is_quality_control_fail of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_quality_control_fail

    @is_quality_control_fail.setter
    def is_quality_control_fail(self, is_quality_control_fail):
        """Sets the is_quality_control_fail of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param is_quality_control_fail: The is_quality_control_fail of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_quality_control_fail = is_quality_control_fail

    @property
    def service_private_comments(self):
        """Gets the service_private_comments of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The service_private_comments of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._service_private_comments

    @service_private_comments.setter
    def service_private_comments(self, service_private_comments):
        """Sets the service_private_comments of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param service_private_comments: The service_private_comments of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._service_private_comments = service_private_comments

    @property
    def client_company_id(self):
        """Gets the client_company_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The client_company_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._client_company_id

    @client_company_id.setter
    def client_company_id(self, client_company_id):
        """Sets the client_company_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param client_company_id: The client_company_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: int
        """

        self._client_company_id = client_company_id

    @property
    def client_company_name(self):
        """Gets the client_company_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The client_company_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._client_company_name

    @client_company_name.setter
    def client_company_name(self, client_company_name):
        """Sets the client_company_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param client_company_name: The client_company_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._client_company_name = client_company_name

    @property
    def client_site_name(self):
        """Gets the client_site_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The client_site_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._client_site_name

    @client_site_name.setter
    def client_site_name(self, client_site_name):
        """Sets the client_site_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param client_site_name: The client_site_name of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._client_site_name = client_site_name

    @property
    def client_legacy_id(self):
        """Gets the client_legacy_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The client_legacy_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._client_legacy_id

    @client_legacy_id.setter
    def client_legacy_id(self, client_legacy_id):
        """Sets the client_legacy_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param client_legacy_id: The client_legacy_id of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._client_legacy_id = client_legacy_id

    @property
    def business_from_time(self):
        """Gets the business_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The business_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._business_from_time

    @business_from_time.setter
    def business_from_time(self, business_from_time):
        """Sets the business_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param business_from_time: The business_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._business_from_time = business_from_time

    @property
    def business_to_time(self):
        """Gets the business_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The business_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._business_to_time

    @business_to_time.setter
    def business_to_time(self, business_to_time):
        """Sets the business_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param business_to_time: The business_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._business_to_time = business_to_time

    @property
    def timeframe(self):
        """Gets the timeframe of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The timeframe of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._timeframe

    @timeframe.setter
    def timeframe(self, timeframe):
        """Sets the timeframe of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param timeframe: The timeframe of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """
        allowed_values = [
            "AsSoonAsPossible",
            "Urgent",
            "OnDateTime",
            "WithinRange",
            "BeforeDate",
        ]  # noqa: E501
        if (
            self._configuration.client_side_validation
            and timeframe not in allowed_values
        ):
            raise ValueError(
                "Invalid value for `timeframe` ({0}), must be one of {1}".format(  # noqa: E501
                    timeframe, allowed_values
                )
            )

        self._timeframe = timeframe

    @property
    def site_access_notes(self):
        """Gets the site_access_notes of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The site_access_notes of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._site_access_notes

    @site_access_notes.setter
    def site_access_notes(self, site_access_notes):
        """Sets the site_access_notes of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param site_access_notes: The site_access_notes of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: str
        """

        self._site_access_notes = site_access_notes

    @property
    def desired_date(self):
        """Gets the desired_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The desired_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._desired_date

    @desired_date.setter
    def desired_date(self, desired_date):
        """Sets the desired_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param desired_date: The desired_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._desired_date = desired_date

    @property
    def deadline_date(self):
        """Gets the deadline_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The deadline_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._deadline_date

    @deadline_date.setter
    def deadline_date(self, deadline_date):
        """Sets the deadline_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param deadline_date: The deadline_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._deadline_date = deadline_date

    @property
    def request_from_date(self):
        """Gets the request_from_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The request_from_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._request_from_date

    @request_from_date.setter
    def request_from_date(self, request_from_date):
        """Sets the request_from_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param request_from_date: The request_from_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._request_from_date = request_from_date

    @property
    def request_from_time(self):
        """Gets the request_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The request_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._request_from_time

    @request_from_time.setter
    def request_from_time(self, request_from_time):
        """Sets the request_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param request_from_time: The request_from_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._request_from_time = request_from_time

    @property
    def request_to_date(self):
        """Gets the request_to_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The request_to_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._request_to_date

    @request_to_date.setter
    def request_to_date(self, request_to_date):
        """Sets the request_to_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param request_to_date: The request_to_date of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._request_to_date = request_to_date

    @property
    def request_to_time(self):
        """Gets the request_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501


        :return: The request_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._request_to_time

    @request_to_time.setter
    def request_to_time(self, request_to_time):
        """Sets the request_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.


        :param request_to_time: The request_to_time of this QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel.  # noqa: E501
        :type: datetime
        """

        self._request_to_time = request_to_time

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(
                    map(lambda x: x.to_dict() if hasattr(x, "to_dict") else x, value)
                )
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(
                    map(
                        lambda item: (
                            (item[0], item[1].to_dict())
                            if hasattr(item[1], "to_dict")
                            else item
                        ),
                        value.items(),
                    )
                )
            else:
                result[attr] = value
        if issubclass(
            QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel, dict
        ):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(
            other, QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel
        ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(
            other, QualerApiModelsServiceOrdersToProviderServiceOrderResponseModel
        ):
            return True

        return self.to_dict() != other.to_dict()
