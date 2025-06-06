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


class QualerApiModelsProductToProductApiResponseModel(object):
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
        "product_id": "int",
        "parent_product_id": "int",
        "category_id": "int",
        "manufacturer_id": "int",
        "manufacturer_name": "str",
        "product_name": "str",
        "parent_product_name": "str",
        "manufacturer_part_number": "str",
        "product_description": "str",
        "is_family": "bool",
        "is_discontinued": "bool",
        "is_stock_item": "bool",
        "unit_sale_price": "float",
        "supplier_information": "str",
        "quantity_on_hand": "int",
        "product_code": "str",
        "category_name": "str",
        "parent_category_name": "str",
    }

    attribute_map = {
        "product_id": "ProductId",
        "parent_product_id": "ParentProductId",
        "category_id": "CategoryId",
        "manufacturer_id": "ManufacturerId",
        "manufacturer_name": "ManufacturerName",
        "product_name": "ProductName",
        "parent_product_name": "ParentProductName",
        "manufacturer_part_number": "ManufacturerPartNumber",
        "product_description": "ProductDescription",
        "is_family": "IsFamily",
        "is_discontinued": "IsDiscontinued",
        "is_stock_item": "IsStockItem",
        "unit_sale_price": "UnitSalePrice",
        "supplier_information": "SupplierInformation",
        "quantity_on_hand": "QuantityOnHand",
        "product_code": "ProductCode",
        "category_name": "CategoryName",
        "parent_category_name": "ParentCategoryName",
    }

    def __init__(
        self,
        product_id=None,
        parent_product_id=None,
        category_id=None,
        manufacturer_id=None,
        manufacturer_name=None,
        product_name=None,
        parent_product_name=None,
        manufacturer_part_number=None,
        product_description=None,
        is_family=None,
        is_discontinued=None,
        is_stock_item=None,
        unit_sale_price=None,
        supplier_information=None,
        quantity_on_hand=None,
        product_code=None,
        category_name=None,
        parent_category_name=None,
        _configuration=None,
    ):  # noqa: E501
        """QualerApiModelsProductToProductApiResponseModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._product_id = None
        self._parent_product_id = None
        self._category_id = None
        self._manufacturer_id = None
        self._manufacturer_name = None
        self._product_name = None
        self._parent_product_name = None
        self._manufacturer_part_number = None
        self._product_description = None
        self._is_family = None
        self._is_discontinued = None
        self._is_stock_item = None
        self._unit_sale_price = None
        self._supplier_information = None
        self._quantity_on_hand = None
        self._product_code = None
        self._category_name = None
        self._parent_category_name = None
        self.discriminator = None

        if product_id is not None:
            self.product_id = product_id
        if parent_product_id is not None:
            self.parent_product_id = parent_product_id
        if category_id is not None:
            self.category_id = category_id
        if manufacturer_id is not None:
            self.manufacturer_id = manufacturer_id
        if manufacturer_name is not None:
            self.manufacturer_name = manufacturer_name
        if product_name is not None:
            self.product_name = product_name
        if parent_product_name is not None:
            self.parent_product_name = parent_product_name
        if manufacturer_part_number is not None:
            self.manufacturer_part_number = manufacturer_part_number
        if product_description is not None:
            self.product_description = product_description
        if is_family is not None:
            self.is_family = is_family
        if is_discontinued is not None:
            self.is_discontinued = is_discontinued
        if is_stock_item is not None:
            self.is_stock_item = is_stock_item
        if unit_sale_price is not None:
            self.unit_sale_price = unit_sale_price
        if supplier_information is not None:
            self.supplier_information = supplier_information
        if quantity_on_hand is not None:
            self.quantity_on_hand = quantity_on_hand
        if product_code is not None:
            self.product_code = product_code
        if category_name is not None:
            self.category_name = category_name
        if parent_category_name is not None:
            self.parent_category_name = parent_category_name

    @property
    def product_id(self):
        """Gets the product_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The product_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this QualerApiModelsProductToProductApiResponseModel.


        :param product_id: The product_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: int
        """

        self._product_id = product_id

    @property
    def parent_product_id(self):
        """Gets the parent_product_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The parent_product_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._parent_product_id

    @parent_product_id.setter
    def parent_product_id(self, parent_product_id):
        """Sets the parent_product_id of this QualerApiModelsProductToProductApiResponseModel.


        :param parent_product_id: The parent_product_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: int
        """

        self._parent_product_id = parent_product_id

    @property
    def category_id(self):
        """Gets the category_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The category_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._category_id

    @category_id.setter
    def category_id(self, category_id):
        """Sets the category_id of this QualerApiModelsProductToProductApiResponseModel.


        :param category_id: The category_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: int
        """

        self._category_id = category_id

    @property
    def manufacturer_id(self):
        """Gets the manufacturer_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The manufacturer_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._manufacturer_id

    @manufacturer_id.setter
    def manufacturer_id(self, manufacturer_id):
        """Sets the manufacturer_id of this QualerApiModelsProductToProductApiResponseModel.


        :param manufacturer_id: The manufacturer_id of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: int
        """

        self._manufacturer_id = manufacturer_id

    @property
    def manufacturer_name(self):
        """Gets the manufacturer_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The manufacturer_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_name

    @manufacturer_name.setter
    def manufacturer_name(self, manufacturer_name):
        """Sets the manufacturer_name of this QualerApiModelsProductToProductApiResponseModel.


        :param manufacturer_name: The manufacturer_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._manufacturer_name = manufacturer_name

    @property
    def product_name(self):
        """Gets the product_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The product_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this QualerApiModelsProductToProductApiResponseModel.


        :param product_name: The product_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._product_name = product_name

    @property
    def parent_product_name(self):
        """Gets the parent_product_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The parent_product_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_product_name

    @parent_product_name.setter
    def parent_product_name(self, parent_product_name):
        """Sets the parent_product_name of this QualerApiModelsProductToProductApiResponseModel.


        :param parent_product_name: The parent_product_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._parent_product_name = parent_product_name

    @property
    def manufacturer_part_number(self):
        """Gets the manufacturer_part_number of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The manufacturer_part_number of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._manufacturer_part_number

    @manufacturer_part_number.setter
    def manufacturer_part_number(self, manufacturer_part_number):
        """Sets the manufacturer_part_number of this QualerApiModelsProductToProductApiResponseModel.


        :param manufacturer_part_number: The manufacturer_part_number of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._manufacturer_part_number = manufacturer_part_number

    @property
    def product_description(self):
        """Gets the product_description of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The product_description of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._product_description

    @product_description.setter
    def product_description(self, product_description):
        """Sets the product_description of this QualerApiModelsProductToProductApiResponseModel.


        :param product_description: The product_description of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._product_description = product_description

    @property
    def is_family(self):
        """Gets the is_family of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The is_family of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_family

    @is_family.setter
    def is_family(self, is_family):
        """Sets the is_family of this QualerApiModelsProductToProductApiResponseModel.


        :param is_family: The is_family of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_family = is_family

    @property
    def is_discontinued(self):
        """Gets the is_discontinued of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The is_discontinued of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_discontinued

    @is_discontinued.setter
    def is_discontinued(self, is_discontinued):
        """Sets the is_discontinued of this QualerApiModelsProductToProductApiResponseModel.


        :param is_discontinued: The is_discontinued of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_discontinued = is_discontinued

    @property
    def is_stock_item(self):
        """Gets the is_stock_item of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The is_stock_item of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_stock_item

    @is_stock_item.setter
    def is_stock_item(self, is_stock_item):
        """Sets the is_stock_item of this QualerApiModelsProductToProductApiResponseModel.


        :param is_stock_item: The is_stock_item of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_stock_item = is_stock_item

    @property
    def unit_sale_price(self):
        """Gets the unit_sale_price of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The unit_sale_price of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._unit_sale_price

    @unit_sale_price.setter
    def unit_sale_price(self, unit_sale_price):
        """Sets the unit_sale_price of this QualerApiModelsProductToProductApiResponseModel.


        :param unit_sale_price: The unit_sale_price of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: float
        """

        self._unit_sale_price = unit_sale_price

    @property
    def supplier_information(self):
        """Gets the supplier_information of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The supplier_information of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._supplier_information

    @supplier_information.setter
    def supplier_information(self, supplier_information):
        """Sets the supplier_information of this QualerApiModelsProductToProductApiResponseModel.


        :param supplier_information: The supplier_information of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._supplier_information = supplier_information

    @property
    def quantity_on_hand(self):
        """Gets the quantity_on_hand of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The quantity_on_hand of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._quantity_on_hand

    @quantity_on_hand.setter
    def quantity_on_hand(self, quantity_on_hand):
        """Sets the quantity_on_hand of this QualerApiModelsProductToProductApiResponseModel.


        :param quantity_on_hand: The quantity_on_hand of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: int
        """

        self._quantity_on_hand = quantity_on_hand

    @property
    def product_code(self):
        """Gets the product_code of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The product_code of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._product_code

    @product_code.setter
    def product_code(self, product_code):
        """Sets the product_code of this QualerApiModelsProductToProductApiResponseModel.


        :param product_code: The product_code of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._product_code = product_code

    @property
    def category_name(self):
        """Gets the category_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The category_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._category_name

    @category_name.setter
    def category_name(self, category_name):
        """Sets the category_name of this QualerApiModelsProductToProductApiResponseModel.


        :param category_name: The category_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._category_name = category_name

    @property
    def parent_category_name(self):
        """Gets the parent_category_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501


        :return: The parent_category_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._parent_category_name

    @parent_category_name.setter
    def parent_category_name(self, parent_category_name):
        """Sets the parent_category_name of this QualerApiModelsProductToProductApiResponseModel.


        :param parent_category_name: The parent_category_name of this QualerApiModelsProductToProductApiResponseModel.  # noqa: E501
        :type: str
        """

        self._parent_category_name = parent_category_name

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
        if issubclass(QualerApiModelsProductToProductApiResponseModel, dict):
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
        if not isinstance(other, QualerApiModelsProductToProductApiResponseModel):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, QualerApiModelsProductToProductApiResponseModel):
            return True

        return self.to_dict() != other.to_dict()
