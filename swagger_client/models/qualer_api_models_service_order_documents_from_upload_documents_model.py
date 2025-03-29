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

class QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel(object):
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
        'report_type': 'str',
        'is_private': 'bool'
    }

    attribute_map = {
        'report_type': 'ReportType',
        'is_private': 'IsPrivate'
    }

    def __init__(self, report_type=None, is_private=None):  # noqa: E501
        """QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel - a model defined in Swagger"""  # noqa: E501
        self._report_type = None
        self._is_private = None
        self.discriminator = None
        if report_type is not None:
            self.report_type = report_type
        if is_private is not None:
            self.is_private = is_private

    @property
    def report_type(self):
        """Gets the report_type of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.  # noqa: E501


        :return: The report_type of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.  # noqa: E501
        :rtype: str
        """
        return self._report_type

    @report_type.setter
    def report_type(self, report_type):
        """Sets the report_type of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.


        :param report_type: The report_type of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.  # noqa: E501
        :type: str
        """

        self._report_type = report_type

    @property
    def is_private(self):
        """Gets the is_private of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.  # noqa: E501


        :return: The is_private of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_private

    @is_private.setter
    def is_private(self, is_private):
        """Sets the is_private of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.


        :param is_private: The is_private of this QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel.  # noqa: E501
        :type: bool
        """

        self._is_private = is_private

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel, dict):
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
        if not isinstance(other, QualerApiModelsServiceOrderDocumentsFromUploadDocumentsModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
