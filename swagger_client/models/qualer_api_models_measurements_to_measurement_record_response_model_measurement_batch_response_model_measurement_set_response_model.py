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

class QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel(object):
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
        'measurement_name': 'str',
        'is_accredited': 'bool',
        'measurement_quantity_id': 'int',
        'default_unit_of_measure_id': 'int',
        'decimal_places': 'int',
        'significant_figures': 'int',
        'display_options': 'QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions',
        'custom_fields': 'QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields',
        'measurement_points': 'list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel]'
    }

    attribute_map = {
        'measurement_name': 'MeasurementName',
        'is_accredited': 'IsAccredited',
        'measurement_quantity_id': 'MeasurementQuantityId',
        'default_unit_of_measure_id': 'DefaultUnitOfMeasureId',
        'decimal_places': 'DecimalPlaces',
        'significant_figures': 'SignificantFigures',
        'display_options': 'DisplayOptions',
        'custom_fields': 'CustomFields',
        'measurement_points': 'MeasurementPoints'
    }

    def __init__(self, measurement_name=None, is_accredited=None, measurement_quantity_id=None, default_unit_of_measure_id=None, decimal_places=None, significant_figures=None, display_options=None, custom_fields=None, measurement_points=None):  # noqa: E501
        """QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel - a model defined in Swagger"""  # noqa: E501
        self._measurement_name = None
        self._is_accredited = None
        self._measurement_quantity_id = None
        self._default_unit_of_measure_id = None
        self._decimal_places = None
        self._significant_figures = None
        self._display_options = None
        self._custom_fields = None
        self._measurement_points = None
        self.discriminator = None
        if measurement_name is not None:
            self.measurement_name = measurement_name
        if is_accredited is not None:
            self.is_accredited = is_accredited
        if measurement_quantity_id is not None:
            self.measurement_quantity_id = measurement_quantity_id
        if default_unit_of_measure_id is not None:
            self.default_unit_of_measure_id = default_unit_of_measure_id
        if decimal_places is not None:
            self.decimal_places = decimal_places
        if significant_figures is not None:
            self.significant_figures = significant_figures
        if display_options is not None:
            self.display_options = display_options
        if custom_fields is not None:
            self.custom_fields = custom_fields
        if measurement_points is not None:
            self.measurement_points = measurement_points

    @property
    def measurement_name(self):
        """Gets the measurement_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The measurement_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._measurement_name

    @measurement_name.setter
    def measurement_name(self, measurement_name):
        """Sets the measurement_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param measurement_name: The measurement_name of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: str
        """

        self._measurement_name = measurement_name

    @property
    def is_accredited(self):
        """Gets the is_accredited of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The is_accredited of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_accredited

    @is_accredited.setter
    def is_accredited(self, is_accredited):
        """Sets the is_accredited of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param is_accredited: The is_accredited of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_accredited = is_accredited

    @property
    def measurement_quantity_id(self):
        """Gets the measurement_quantity_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The measurement_quantity_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._measurement_quantity_id

    @measurement_quantity_id.setter
    def measurement_quantity_id(self, measurement_quantity_id):
        """Sets the measurement_quantity_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param measurement_quantity_id: The measurement_quantity_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: int
        """

        self._measurement_quantity_id = measurement_quantity_id

    @property
    def default_unit_of_measure_id(self):
        """Gets the default_unit_of_measure_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The default_unit_of_measure_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._default_unit_of_measure_id

    @default_unit_of_measure_id.setter
    def default_unit_of_measure_id(self, default_unit_of_measure_id):
        """Sets the default_unit_of_measure_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param default_unit_of_measure_id: The default_unit_of_measure_id of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: int
        """

        self._default_unit_of_measure_id = default_unit_of_measure_id

    @property
    def decimal_places(self):
        """Gets the decimal_places of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The decimal_places of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._decimal_places

    @decimal_places.setter
    def decimal_places(self, decimal_places):
        """Sets the decimal_places of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param decimal_places: The decimal_places of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: int
        """

        self._decimal_places = decimal_places

    @property
    def significant_figures(self):
        """Gets the significant_figures of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The significant_figures of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._significant_figures

    @significant_figures.setter
    def significant_figures(self, significant_figures):
        """Sets the significant_figures of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param significant_figures: The significant_figures of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: int
        """

        self._significant_figures = significant_figures

    @property
    def display_options(self):
        """Gets the display_options of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The display_options of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions
        """
        return self._display_options

    @display_options.setter
    def display_options(self, display_options):
        """Sets the display_options of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param display_options: The display_options of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelDisplayOptions
        """

        self._display_options = display_options

    @property
    def custom_fields(self):
        """Gets the custom_fields of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The custom_fields of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields
        """
        return self._custom_fields

    @custom_fields.setter
    def custom_fields(self, custom_fields):
        """Sets the custom_fields of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param custom_fields: The custom_fields of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelCustomFields
        """

        self._custom_fields = custom_fields

    @property
    def measurement_points(self):
        """Gets the measurement_points of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501


        :return: The measurement_points of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :rtype: list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel]
        """
        return self._measurement_points

    @measurement_points.setter
    def measurement_points(self, measurement_points):
        """Sets the measurement_points of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.


        :param measurement_points: The measurement_points of this QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel.  # noqa: E501
        :type: list[QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModelMeasurementPointResponseModel]
        """

        self._measurement_points = measurement_points

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
        if issubclass(QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel, dict):
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
        if not isinstance(other, QualerApiModelsMeasurementsToMeasurementRecordResponseModelMeasurementBatchResponseModelMeasurementSetResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
