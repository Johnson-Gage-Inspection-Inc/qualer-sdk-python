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


class QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel(object):
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
        "filter_type": "str",
        "within_days": "int",
        "use_date_range": "bool",
        "start_date": "datetime",
        "end_date": "datetime",
    }

    attribute_map = {
        "filter_type": "FilterType",
        "within_days": "WithinDays",
        "use_date_range": "UseDateRange",
        "start_date": "StartDate",
        "end_date": "EndDate",
    }

    def __init__(
        self,
        filter_type=None,
        within_days=None,
        use_date_range=None,
        start_date=None,
        end_date=None,
        _configuration=None,
    ):  # noqa: E501
        """QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._filter_type = None
        self._within_days = None
        self._use_date_range = None
        self._start_date = None
        self._end_date = None
        self.discriminator = None

        if filter_type is not None:
            self.filter_type = filter_type
        if within_days is not None:
            self.within_days = within_days
        if use_date_range is not None:
            self.use_date_range = use_date_range
        if start_date is not None:
            self.start_date = start_date
        if end_date is not None:
            self.end_date = end_date

    @property
    def filter_type(self):
        """Gets the filter_type of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501


        :return: The filter_type of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._filter_type

    @filter_type.setter
    def filter_type(self, filter_type):
        """Sets the filter_type of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.


        :param filter_type: The filter_type of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :type: str
        """

        self._filter_type = filter_type

    @property
    def within_days(self):
        """Gets the within_days of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501


        :return: The within_days of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._within_days

    @within_days.setter
    def within_days(self, within_days):
        """Sets the within_days of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.


        :param within_days: The within_days of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :type: int
        """

        self._within_days = within_days

    @property
    def use_date_range(self):
        """Gets the use_date_range of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501


        :return: The use_date_range of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._use_date_range

    @use_date_range.setter
    def use_date_range(self, use_date_range):
        """Sets the use_date_range of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.


        :param use_date_range: The use_date_range of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :type: bool
        """

        self._use_date_range = use_date_range

    @property
    def start_date(self):
        """Gets the start_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501


        :return: The start_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.


        :param start_date: The start_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def end_date(self):
        """Gets the end_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501


        :return: The end_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.


        :param end_date: The end_date of this QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

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
            QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel, dict
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
            other, QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel
        ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(
            other, QualerApiModelsAssetToEmployeeFilterPreferenceResponseModel
        ):
            return True

        return self.to_dict() != other.to_dict()
