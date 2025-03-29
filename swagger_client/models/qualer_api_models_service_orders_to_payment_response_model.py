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

class QualerApiModelsServiceOrdersToPaymentResponseModel(object):
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
        'service_order_id': 'int',
        'created_by_id': 'int',
        'transaction_id': 'str',
        'transaction_status': 'str',
        'payment_type': 'str',
        'service_order_payment_id': 'int',
        'payment_amount': 'float',
        'details': 'str'
    }

    attribute_map = {
        'service_order_id': 'ServiceOrderId',
        'created_by_id': 'CreatedById',
        'transaction_id': 'TransactionId',
        'transaction_status': 'TransactionStatus',
        'payment_type': 'PaymentType',
        'service_order_payment_id': 'ServiceOrderPaymentId',
        'payment_amount': 'PaymentAmount',
        'details': 'Details'
    }

    def __init__(self, service_order_id=None, created_by_id=None, transaction_id=None, transaction_status=None, payment_type=None, service_order_payment_id=None, payment_amount=None, details=None):  # noqa: E501
        """QualerApiModelsServiceOrdersToPaymentResponseModel - a model defined in Swagger"""  # noqa: E501
        self._service_order_id = None
        self._created_by_id = None
        self._transaction_id = None
        self._transaction_status = None
        self._payment_type = None
        self._service_order_payment_id = None
        self._payment_amount = None
        self._details = None
        self.discriminator = None
        if service_order_id is not None:
            self.service_order_id = service_order_id
        if created_by_id is not None:
            self.created_by_id = created_by_id
        if transaction_id is not None:
            self.transaction_id = transaction_id
        if transaction_status is not None:
            self.transaction_status = transaction_status
        if payment_type is not None:
            self.payment_type = payment_type
        if service_order_payment_id is not None:
            self.service_order_payment_id = service_order_payment_id
        if payment_amount is not None:
            self.payment_amount = payment_amount
        if details is not None:
            self.details = details

    @property
    def service_order_id(self):
        """Gets the service_order_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The service_order_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_order_id

    @service_order_id.setter
    def service_order_id(self, service_order_id):
        """Sets the service_order_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param service_order_id: The service_order_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: int
        """

        self._service_order_id = service_order_id

    @property
    def created_by_id(self):
        """Gets the created_by_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The created_by_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._created_by_id

    @created_by_id.setter
    def created_by_id(self, created_by_id):
        """Sets the created_by_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param created_by_id: The created_by_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: int
        """

        self._created_by_id = created_by_id

    @property
    def transaction_id(self):
        """Gets the transaction_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The transaction_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param transaction_id: The transaction_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: str
        """

        self._transaction_id = transaction_id

    @property
    def transaction_status(self):
        """Gets the transaction_status of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The transaction_status of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._transaction_status

    @transaction_status.setter
    def transaction_status(self, transaction_status):
        """Sets the transaction_status of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param transaction_status: The transaction_status of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: str
        """

        self._transaction_status = transaction_status

    @property
    def payment_type(self):
        """Gets the payment_type of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The payment_type of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._payment_type

    @payment_type.setter
    def payment_type(self, payment_type):
        """Sets the payment_type of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param payment_type: The payment_type of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: str
        """

        self._payment_type = payment_type

    @property
    def service_order_payment_id(self):
        """Gets the service_order_payment_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The service_order_payment_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._service_order_payment_id

    @service_order_payment_id.setter
    def service_order_payment_id(self, service_order_payment_id):
        """Sets the service_order_payment_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param service_order_payment_id: The service_order_payment_id of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: int
        """

        self._service_order_payment_id = service_order_payment_id

    @property
    def payment_amount(self):
        """Gets the payment_amount of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The payment_amount of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._payment_amount

    @payment_amount.setter
    def payment_amount(self, payment_amount):
        """Sets the payment_amount of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param payment_amount: The payment_amount of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: float
        """

        self._payment_amount = payment_amount

    @property
    def details(self):
        """Gets the details of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501


        :return: The details of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._details

    @details.setter
    def details(self, details):
        """Sets the details of this QualerApiModelsServiceOrdersToPaymentResponseModel.


        :param details: The details of this QualerApiModelsServiceOrdersToPaymentResponseModel.  # noqa: E501
        :type: str
        """

        self._details = details

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
        if issubclass(QualerApiModelsServiceOrdersToPaymentResponseModel, dict):
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
        if not isinstance(other, QualerApiModelsServiceOrdersToPaymentResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
