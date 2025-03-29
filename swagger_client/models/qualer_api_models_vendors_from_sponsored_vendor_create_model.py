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

class QualerApiModelsVendorsFromSponsoredVendorCreateModel(object):
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
        'account_number_text': 'str',
        'domain_name': 'str',
        'custom_vendor_name': 'str',
        'currency_id': 'int',
        'company_name': 'str',
        'billing_address': 'QualerApiModelsAddressAddressModel',
        'shipping_address': 'QualerApiModelsAddressAddressModel'
    }

    attribute_map = {
        'account_number_text': 'AccountNumberText',
        'domain_name': 'DomainName',
        'custom_vendor_name': 'CustomVendorName',
        'currency_id': 'CurrencyId',
        'company_name': 'CompanyName',
        'billing_address': 'BillingAddress',
        'shipping_address': 'ShippingAddress'
    }

    def __init__(self, account_number_text=None, domain_name=None, custom_vendor_name=None, currency_id=None, company_name=None, billing_address=None, shipping_address=None):  # noqa: E501
        """QualerApiModelsVendorsFromSponsoredVendorCreateModel - a model defined in Swagger"""  # noqa: E501
        self._account_number_text = None
        self._domain_name = None
        self._custom_vendor_name = None
        self._currency_id = None
        self._company_name = None
        self._billing_address = None
        self._shipping_address = None
        self.discriminator = None
        if account_number_text is not None:
            self.account_number_text = account_number_text
        if domain_name is not None:
            self.domain_name = domain_name
        if custom_vendor_name is not None:
            self.custom_vendor_name = custom_vendor_name
        if currency_id is not None:
            self.currency_id = currency_id
        if company_name is not None:
            self.company_name = company_name
        if billing_address is not None:
            self.billing_address = billing_address
        if shipping_address is not None:
            self.shipping_address = shipping_address

    @property
    def account_number_text(self):
        """Gets the account_number_text of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The account_number_text of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: str
        """
        return self._account_number_text

    @account_number_text.setter
    def account_number_text(self, account_number_text):
        """Sets the account_number_text of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param account_number_text: The account_number_text of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: str
        """

        self._account_number_text = account_number_text

    @property
    def domain_name(self):
        """Gets the domain_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The domain_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        """Sets the domain_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param domain_name: The domain_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: str
        """

        self._domain_name = domain_name

    @property
    def custom_vendor_name(self):
        """Gets the custom_vendor_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The custom_vendor_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: str
        """
        return self._custom_vendor_name

    @custom_vendor_name.setter
    def custom_vendor_name(self, custom_vendor_name):
        """Sets the custom_vendor_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param custom_vendor_name: The custom_vendor_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: str
        """

        self._custom_vendor_name = custom_vendor_name

    @property
    def currency_id(self):
        """Gets the currency_id of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The currency_id of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: int
        """
        return self._currency_id

    @currency_id.setter
    def currency_id(self, currency_id):
        """Sets the currency_id of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param currency_id: The currency_id of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: int
        """

        self._currency_id = currency_id

    @property
    def company_name(self):
        """Gets the company_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The company_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: str
        """
        return self._company_name

    @company_name.setter
    def company_name(self, company_name):
        """Sets the company_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param company_name: The company_name of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: str
        """

        self._company_name = company_name

    @property
    def billing_address(self):
        """Gets the billing_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The billing_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: QualerApiModelsAddressAddressModel
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param billing_address: The billing_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: QualerApiModelsAddressAddressModel
        """

        self._billing_address = billing_address

    @property
    def shipping_address(self):
        """Gets the shipping_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501


        :return: The shipping_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :rtype: QualerApiModelsAddressAddressModel
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.


        :param shipping_address: The shipping_address of this QualerApiModelsVendorsFromSponsoredVendorCreateModel.  # noqa: E501
        :type: QualerApiModelsAddressAddressModel
        """

        self._shipping_address = shipping_address

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
        if issubclass(QualerApiModelsVendorsFromSponsoredVendorCreateModel, dict):
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
        if not isinstance(other, QualerApiModelsVendorsFromSponsoredVendorCreateModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
