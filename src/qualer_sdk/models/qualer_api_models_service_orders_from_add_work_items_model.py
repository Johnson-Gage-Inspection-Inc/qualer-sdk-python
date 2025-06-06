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


class QualerApiModelsServiceOrdersFromAddWorkItemsModel(object):
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
    swagger_types = {"asset_ids": "list[int]", "schedule_segment_ids": "list[int]"}

    attribute_map = {
        "asset_ids": "AssetIds",
        "schedule_segment_ids": "ScheduleSegmentIds",
    }

    def __init__(
        self, asset_ids=None, schedule_segment_ids=None, _configuration=None
    ):  # noqa: E501
        """QualerApiModelsServiceOrdersFromAddWorkItemsModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._asset_ids = None
        self._schedule_segment_ids = None
        self.discriminator = None

        if asset_ids is not None:
            self.asset_ids = asset_ids
        if schedule_segment_ids is not None:
            self.schedule_segment_ids = schedule_segment_ids

    @property
    def asset_ids(self):
        """Gets the asset_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.  # noqa: E501


        :return: The asset_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._asset_ids

    @asset_ids.setter
    def asset_ids(self, asset_ids):
        """Sets the asset_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.


        :param asset_ids: The asset_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.  # noqa: E501
        :type: list[int]
        """

        self._asset_ids = asset_ids

    @property
    def schedule_segment_ids(self):
        """Gets the schedule_segment_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.  # noqa: E501


        :return: The schedule_segment_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.  # noqa: E501
        :rtype: list[int]
        """
        return self._schedule_segment_ids

    @schedule_segment_ids.setter
    def schedule_segment_ids(self, schedule_segment_ids):
        """Sets the schedule_segment_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.


        :param schedule_segment_ids: The schedule_segment_ids of this QualerApiModelsServiceOrdersFromAddWorkItemsModel.  # noqa: E501
        :type: list[int]
        """

        self._schedule_segment_ids = schedule_segment_ids

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
        if issubclass(QualerApiModelsServiceOrdersFromAddWorkItemsModel, dict):
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
        if not isinstance(other, QualerApiModelsServiceOrdersFromAddWorkItemsModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualerApiModelsServiceOrdersFromAddWorkItemsModel):
            return True

        return self.to_dict() != other.to_dict()
