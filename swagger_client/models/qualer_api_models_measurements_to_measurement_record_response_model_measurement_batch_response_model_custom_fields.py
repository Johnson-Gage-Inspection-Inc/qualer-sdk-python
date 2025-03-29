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

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields(object):
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
        'description': 'str',
        'result': 'str',
        'items': 'list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel]'
    }

    attribute_map = {
        'description': 'Description',
        'result': 'Result',
        'items': 'Items'
    }

    def __init__(self, description=None, result=None, items=None):  # noqa: E501
        """QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._result = None
        self._items = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if result is not None:
            self.result = result
        if items is not None:
            self.items = items

    @property
    def description(self):
        """Gets the description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501


        :return: The description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.


        :param description: The description of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def result(self):
        """Gets the result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501


        :return: The result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        """Sets the result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.


        :param result: The result of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501
        :type: str
        """

        self._result = result

    @property
    def items(self):
        """Gets the items of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501


        :return: The items of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501
        :rtype: list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.


        :param items: The items of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields.  # noqa: E501
        :type: list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFieldsCreateMeasurementFieldResponseModel]
        """

        self._items = items

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
        if issubclass(QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields, dict):
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
        if not isinstance(other, QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
