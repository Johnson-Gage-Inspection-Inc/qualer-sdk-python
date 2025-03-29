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

class QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse(object):
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
        'field_id': 'str',
        'type': 'str',
        'value': 'str',
        'service_order_item_id': 'int',
        'service_order_item_task_id': 'int'
    }

    attribute_map = {
        'field_id': 'FieldId',
        'type': 'Type',
        'value': 'Value',
        'service_order_item_id': 'ServiceOrderItemId',
        'service_order_item_task_id': 'ServiceOrderItemTaskId'
    }

    def __init__(self, field_id=None, type=None, value=None, service_order_item_id=None, service_order_item_task_id=None):  # noqa: E501
        """QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse - a model defined in Swagger"""  # noqa: E501
        self._field_id = None
        self._type = None
        self._value = None
        self._service_order_item_id = None
        self._service_order_item_task_id = None
        self.discriminator = None
        if field_id is not None:
            self.field_id = field_id
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if service_order_item_id is not None:
            self.service_order_item_id = service_order_item_id
        if service_order_item_task_id is not None:
            self.service_order_item_task_id = service_order_item_task_id

    @property
    def field_id(self):
        """Gets the field_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501


        :return: The field_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :rtype: str
        """
        return self._field_id

    @field_id.setter
    def field_id(self, field_id):
        """Sets the field_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.


        :param field_id: The field_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :type: str
        """

        self._field_id = field_id

    @property
    def type(self):
        """Gets the type of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501


        :return: The type of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.


        :param type: The type of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :type: str
        """
        allowed_values = ["Int", "Double", "String", "Boolean", "Date", "List", "DateTime", "ValueLookup"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def value(self):
        """Gets the value of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501


        :return: The value of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.


        :param value: The value of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def service_order_item_id(self):
        """Gets the service_order_item_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501


        :return: The service_order_item_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :rtype: int
        """
        return self._service_order_item_id

    @service_order_item_id.setter
    def service_order_item_id(self, service_order_item_id):
        """Sets the service_order_item_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.


        :param service_order_item_id: The service_order_item_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :type: int
        """

        self._service_order_item_id = service_order_item_id

    @property
    def service_order_item_task_id(self):
        """Gets the service_order_item_task_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501


        :return: The service_order_item_task_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :rtype: int
        """
        return self._service_order_item_task_id

    @service_order_item_task_id.setter
    def service_order_item_task_id(self, service_order_item_task_id):
        """Sets the service_order_item_task_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.


        :param service_order_item_task_id: The service_order_item_task_id of this QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse.  # noqa: E501
        :type: int
        """

        self._service_order_item_task_id = service_order_item_task_id

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
        if issubclass(QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse, dict):
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
        if not isinstance(other, QualerApiModelsReportDatasetsToServiceOrderItemFieldResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
