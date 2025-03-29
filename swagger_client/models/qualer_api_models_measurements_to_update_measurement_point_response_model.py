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

class QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel(object):
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
        'measurement_point_id': 'int',
        'specification_name': 'str',
        'unit_of_measure': 'str',
        'expected_value': 'float',
        'base_value': 'float',
        'test_value': 'float',
        'nominal': 'float',
        'range_min': 'float',
        'range_max': 'float',
        'tolerance_type': 'str',
        'tolerance_mode': 'str',
        'tolerance_unit': 'str',
        'precision_type': 'str',
        'precision': 'float',
        'tolerance_minimum': 'float',
        'tolerance_maximum': 'float',
        'resolution': 'float',
        'resolution_count': 'float',
        'is_accredited': 'bool',
        'linked_measurement_point_id': 'int',
        'hysteresis_point': 'str',
        'hide_from_certificate': 'bool',
        'is_measurement_not_taken': 'bool',
        'measurement_not_taken_result': 'str',
        'measurement_not_taken_reason': 'str',
        'influence_parameter1_parameter_id': 'int',
        'influence_parameter1_value': 'str',
        'influence_parameter2_parameter_id': 'int',
        'influence_parameter2_value': 'str',
        'measurements': 'list[QualerApiModelsMeasurementsToUpdateMeasurementResponseModel]',
        'measurement_condition_factors': 'list[QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse]',
        'primary_measurement_tool': 'QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel',
        'secondary_measurement_tool': 'QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel'
    }

    attribute_map = {
        'measurement_point_id': 'MeasurementPointId',
        'specification_name': 'SpecificationName',
        'unit_of_measure': 'UnitOfMeasure',
        'expected_value': 'ExpectedValue',
        'base_value': 'BaseValue',
        'test_value': 'TestValue',
        'nominal': 'Nominal',
        'range_min': 'RangeMin',
        'range_max': 'RangeMax',
        'tolerance_type': 'ToleranceType',
        'tolerance_mode': 'ToleranceMode',
        'tolerance_unit': 'ToleranceUnit',
        'precision_type': 'PrecisionType',
        'precision': 'Precision',
        'tolerance_minimum': 'ToleranceMinimum',
        'tolerance_maximum': 'ToleranceMaximum',
        'resolution': 'Resolution',
        'resolution_count': 'ResolutionCount',
        'is_accredited': 'IsAccredited',
        'linked_measurement_point_id': 'LinkedMeasurementPointId',
        'hysteresis_point': 'HysteresisPoint',
        'hide_from_certificate': 'HideFromCertificate',
        'is_measurement_not_taken': 'IsMeasurementNotTaken',
        'measurement_not_taken_result': 'MeasurementNotTakenResult',
        'measurement_not_taken_reason': 'MeasurementNotTakenReason',
        'influence_parameter1_parameter_id': 'InfluenceParameter1ParameterId',
        'influence_parameter1_value': 'InfluenceParameter1Value',
        'influence_parameter2_parameter_id': 'InfluenceParameter2ParameterId',
        'influence_parameter2_value': 'InfluenceParameter2Value',
        'measurements': 'Measurements',
        'measurement_condition_factors': 'MeasurementConditionFactors',
        'primary_measurement_tool': 'PrimaryMeasurementTool',
        'secondary_measurement_tool': 'SecondaryMeasurementTool'
    }

    def __init__(self, measurement_point_id=None, specification_name=None, unit_of_measure=None, expected_value=None, base_value=None, test_value=None, nominal=None, range_min=None, range_max=None, tolerance_type=None, tolerance_mode=None, tolerance_unit=None, precision_type=None, precision=None, tolerance_minimum=None, tolerance_maximum=None, resolution=None, resolution_count=None, is_accredited=None, linked_measurement_point_id=None, hysteresis_point=None, hide_from_certificate=None, is_measurement_not_taken=None, measurement_not_taken_result=None, measurement_not_taken_reason=None, influence_parameter1_parameter_id=None, influence_parameter1_value=None, influence_parameter2_parameter_id=None, influence_parameter2_value=None, measurements=None, measurement_condition_factors=None, primary_measurement_tool=None, secondary_measurement_tool=None):  # noqa: E501
        """QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel - a model defined in Swagger"""  # noqa: E501
        self._measurement_point_id = None
        self._specification_name = None
        self._unit_of_measure = None
        self._expected_value = None
        self._base_value = None
        self._test_value = None
        self._nominal = None
        self._range_min = None
        self._range_max = None
        self._tolerance_type = None
        self._tolerance_mode = None
        self._tolerance_unit = None
        self._precision_type = None
        self._precision = None
        self._tolerance_minimum = None
        self._tolerance_maximum = None
        self._resolution = None
        self._resolution_count = None
        self._is_accredited = None
        self._linked_measurement_point_id = None
        self._hysteresis_point = None
        self._hide_from_certificate = None
        self._is_measurement_not_taken = None
        self._measurement_not_taken_result = None
        self._measurement_not_taken_reason = None
        self._influence_parameter1_parameter_id = None
        self._influence_parameter1_value = None
        self._influence_parameter2_parameter_id = None
        self._influence_parameter2_value = None
        self._measurements = None
        self._measurement_condition_factors = None
        self._primary_measurement_tool = None
        self._secondary_measurement_tool = None
        self.discriminator = None
        if measurement_point_id is not None:
            self.measurement_point_id = measurement_point_id
        if specification_name is not None:
            self.specification_name = specification_name
        if unit_of_measure is not None:
            self.unit_of_measure = unit_of_measure
        if expected_value is not None:
            self.expected_value = expected_value
        if base_value is not None:
            self.base_value = base_value
        if test_value is not None:
            self.test_value = test_value
        if nominal is not None:
            self.nominal = nominal
        if range_min is not None:
            self.range_min = range_min
        if range_max is not None:
            self.range_max = range_max
        if tolerance_type is not None:
            self.tolerance_type = tolerance_type
        if tolerance_mode is not None:
            self.tolerance_mode = tolerance_mode
        if tolerance_unit is not None:
            self.tolerance_unit = tolerance_unit
        if precision_type is not None:
            self.precision_type = precision_type
        if precision is not None:
            self.precision = precision
        if tolerance_minimum is not None:
            self.tolerance_minimum = tolerance_minimum
        if tolerance_maximum is not None:
            self.tolerance_maximum = tolerance_maximum
        if resolution is not None:
            self.resolution = resolution
        if resolution_count is not None:
            self.resolution_count = resolution_count
        if is_accredited is not None:
            self.is_accredited = is_accredited
        if linked_measurement_point_id is not None:
            self.linked_measurement_point_id = linked_measurement_point_id
        if hysteresis_point is not None:
            self.hysteresis_point = hysteresis_point
        if hide_from_certificate is not None:
            self.hide_from_certificate = hide_from_certificate
        if is_measurement_not_taken is not None:
            self.is_measurement_not_taken = is_measurement_not_taken
        if measurement_not_taken_result is not None:
            self.measurement_not_taken_result = measurement_not_taken_result
        if measurement_not_taken_reason is not None:
            self.measurement_not_taken_reason = measurement_not_taken_reason
        if influence_parameter1_parameter_id is not None:
            self.influence_parameter1_parameter_id = influence_parameter1_parameter_id
        if influence_parameter1_value is not None:
            self.influence_parameter1_value = influence_parameter1_value
        if influence_parameter2_parameter_id is not None:
            self.influence_parameter2_parameter_id = influence_parameter2_parameter_id
        if influence_parameter2_value is not None:
            self.influence_parameter2_value = influence_parameter2_value
        if measurements is not None:
            self.measurements = measurements
        if measurement_condition_factors is not None:
            self.measurement_condition_factors = measurement_condition_factors
        if primary_measurement_tool is not None:
            self.primary_measurement_tool = primary_measurement_tool
        if secondary_measurement_tool is not None:
            self.secondary_measurement_tool = secondary_measurement_tool

    @property
    def measurement_point_id(self):
        """Gets the measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._measurement_point_id

    @measurement_point_id.setter
    def measurement_point_id(self, measurement_point_id):
        """Sets the measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param measurement_point_id: The measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: int
        """

        self._measurement_point_id = measurement_point_id

    @property
    def specification_name(self):
        """Gets the specification_name of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The specification_name of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._specification_name

    @specification_name.setter
    def specification_name(self, specification_name):
        """Sets the specification_name of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param specification_name: The specification_name of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._specification_name = specification_name

    @property
    def unit_of_measure(self):
        """Gets the unit_of_measure of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The unit_of_measure of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._unit_of_measure

    @unit_of_measure.setter
    def unit_of_measure(self, unit_of_measure):
        """Sets the unit_of_measure of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param unit_of_measure: The unit_of_measure of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._unit_of_measure = unit_of_measure

    @property
    def expected_value(self):
        """Gets the expected_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The expected_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._expected_value

    @expected_value.setter
    def expected_value(self, expected_value):
        """Sets the expected_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param expected_value: The expected_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._expected_value = expected_value

    @property
    def base_value(self):
        """Gets the base_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The base_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._base_value

    @base_value.setter
    def base_value(self, base_value):
        """Sets the base_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param base_value: The base_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._base_value = base_value

    @property
    def test_value(self):
        """Gets the test_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The test_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._test_value

    @test_value.setter
    def test_value(self, test_value):
        """Sets the test_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param test_value: The test_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._test_value = test_value

    @property
    def nominal(self):
        """Gets the nominal of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The nominal of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._nominal

    @nominal.setter
    def nominal(self, nominal):
        """Sets the nominal of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param nominal: The nominal of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._nominal = nominal

    @property
    def range_min(self):
        """Gets the range_min of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The range_min of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._range_min

    @range_min.setter
    def range_min(self, range_min):
        """Sets the range_min of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param range_min: The range_min of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._range_min = range_min

    @property
    def range_max(self):
        """Gets the range_max of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The range_max of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._range_max

    @range_max.setter
    def range_max(self, range_max):
        """Sets the range_max of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param range_max: The range_max of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._range_max = range_max

    @property
    def tolerance_type(self):
        """Gets the tolerance_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The tolerance_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._tolerance_type

    @tolerance_type.setter
    def tolerance_type(self, tolerance_type):
        """Sets the tolerance_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param tolerance_type: The tolerance_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._tolerance_type = tolerance_type

    @property
    def tolerance_mode(self):
        """Gets the tolerance_mode of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The tolerance_mode of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._tolerance_mode

    @tolerance_mode.setter
    def tolerance_mode(self, tolerance_mode):
        """Sets the tolerance_mode of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param tolerance_mode: The tolerance_mode of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._tolerance_mode = tolerance_mode

    @property
    def tolerance_unit(self):
        """Gets the tolerance_unit of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The tolerance_unit of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._tolerance_unit

    @tolerance_unit.setter
    def tolerance_unit(self, tolerance_unit):
        """Sets the tolerance_unit of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param tolerance_unit: The tolerance_unit of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._tolerance_unit = tolerance_unit

    @property
    def precision_type(self):
        """Gets the precision_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The precision_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._precision_type

    @precision_type.setter
    def precision_type(self, precision_type):
        """Sets the precision_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param precision_type: The precision_type of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._precision_type = precision_type

    @property
    def precision(self):
        """Gets the precision of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The precision of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param precision: The precision of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._precision = precision

    @property
    def tolerance_minimum(self):
        """Gets the tolerance_minimum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The tolerance_minimum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._tolerance_minimum

    @tolerance_minimum.setter
    def tolerance_minimum(self, tolerance_minimum):
        """Sets the tolerance_minimum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param tolerance_minimum: The tolerance_minimum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._tolerance_minimum = tolerance_minimum

    @property
    def tolerance_maximum(self):
        """Gets the tolerance_maximum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The tolerance_maximum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._tolerance_maximum

    @tolerance_maximum.setter
    def tolerance_maximum(self, tolerance_maximum):
        """Sets the tolerance_maximum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param tolerance_maximum: The tolerance_maximum of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._tolerance_maximum = tolerance_maximum

    @property
    def resolution(self):
        """Gets the resolution of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The resolution of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._resolution

    @resolution.setter
    def resolution(self, resolution):
        """Sets the resolution of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param resolution: The resolution of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._resolution = resolution

    @property
    def resolution_count(self):
        """Gets the resolution_count of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The resolution_count of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: float
        """
        return self._resolution_count

    @resolution_count.setter
    def resolution_count(self, resolution_count):
        """Sets the resolution_count of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param resolution_count: The resolution_count of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: float
        """

        self._resolution_count = resolution_count

    @property
    def is_accredited(self):
        """Gets the is_accredited of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The is_accredited of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_accredited

    @is_accredited.setter
    def is_accredited(self, is_accredited):
        """Sets the is_accredited of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param is_accredited: The is_accredited of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_accredited = is_accredited

    @property
    def linked_measurement_point_id(self):
        """Gets the linked_measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The linked_measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._linked_measurement_point_id

    @linked_measurement_point_id.setter
    def linked_measurement_point_id(self, linked_measurement_point_id):
        """Sets the linked_measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param linked_measurement_point_id: The linked_measurement_point_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: int
        """

        self._linked_measurement_point_id = linked_measurement_point_id

    @property
    def hysteresis_point(self):
        """Gets the hysteresis_point of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The hysteresis_point of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._hysteresis_point

    @hysteresis_point.setter
    def hysteresis_point(self, hysteresis_point):
        """Sets the hysteresis_point of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param hysteresis_point: The hysteresis_point of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._hysteresis_point = hysteresis_point

    @property
    def hide_from_certificate(self):
        """Gets the hide_from_certificate of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The hide_from_certificate of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._hide_from_certificate

    @hide_from_certificate.setter
    def hide_from_certificate(self, hide_from_certificate):
        """Sets the hide_from_certificate of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param hide_from_certificate: The hide_from_certificate of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: bool
        """

        self._hide_from_certificate = hide_from_certificate

    @property
    def is_measurement_not_taken(self):
        """Gets the is_measurement_not_taken of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The is_measurement_not_taken of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: bool
        """
        return self._is_measurement_not_taken

    @is_measurement_not_taken.setter
    def is_measurement_not_taken(self, is_measurement_not_taken):
        """Sets the is_measurement_not_taken of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param is_measurement_not_taken: The is_measurement_not_taken of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: bool
        """

        self._is_measurement_not_taken = is_measurement_not_taken

    @property
    def measurement_not_taken_result(self):
        """Gets the measurement_not_taken_result of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The measurement_not_taken_result of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._measurement_not_taken_result

    @measurement_not_taken_result.setter
    def measurement_not_taken_result(self, measurement_not_taken_result):
        """Sets the measurement_not_taken_result of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param measurement_not_taken_result: The measurement_not_taken_result of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._measurement_not_taken_result = measurement_not_taken_result

    @property
    def measurement_not_taken_reason(self):
        """Gets the measurement_not_taken_reason of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The measurement_not_taken_reason of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._measurement_not_taken_reason

    @measurement_not_taken_reason.setter
    def measurement_not_taken_reason(self, measurement_not_taken_reason):
        """Sets the measurement_not_taken_reason of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param measurement_not_taken_reason: The measurement_not_taken_reason of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._measurement_not_taken_reason = measurement_not_taken_reason

    @property
    def influence_parameter1_parameter_id(self):
        """Gets the influence_parameter1_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The influence_parameter1_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._influence_parameter1_parameter_id

    @influence_parameter1_parameter_id.setter
    def influence_parameter1_parameter_id(self, influence_parameter1_parameter_id):
        """Sets the influence_parameter1_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param influence_parameter1_parameter_id: The influence_parameter1_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: int
        """

        self._influence_parameter1_parameter_id = influence_parameter1_parameter_id

    @property
    def influence_parameter1_value(self):
        """Gets the influence_parameter1_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The influence_parameter1_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._influence_parameter1_value

    @influence_parameter1_value.setter
    def influence_parameter1_value(self, influence_parameter1_value):
        """Sets the influence_parameter1_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param influence_parameter1_value: The influence_parameter1_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._influence_parameter1_value = influence_parameter1_value

    @property
    def influence_parameter2_parameter_id(self):
        """Gets the influence_parameter2_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The influence_parameter2_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: int
        """
        return self._influence_parameter2_parameter_id

    @influence_parameter2_parameter_id.setter
    def influence_parameter2_parameter_id(self, influence_parameter2_parameter_id):
        """Sets the influence_parameter2_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param influence_parameter2_parameter_id: The influence_parameter2_parameter_id of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: int
        """

        self._influence_parameter2_parameter_id = influence_parameter2_parameter_id

    @property
    def influence_parameter2_value(self):
        """Gets the influence_parameter2_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The influence_parameter2_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: str
        """
        return self._influence_parameter2_value

    @influence_parameter2_value.setter
    def influence_parameter2_value(self, influence_parameter2_value):
        """Sets the influence_parameter2_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param influence_parameter2_value: The influence_parameter2_value of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: str
        """

        self._influence_parameter2_value = influence_parameter2_value

    @property
    def measurements(self):
        """Gets the measurements of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The measurements of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: list[QualerApiModelsMeasurementsToUpdateMeasurementResponseModel]
        """
        return self._measurements

    @measurements.setter
    def measurements(self, measurements):
        """Sets the measurements of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param measurements: The measurements of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: list[QualerApiModelsMeasurementsToUpdateMeasurementResponseModel]
        """

        self._measurements = measurements

    @property
    def measurement_condition_factors(self):
        """Gets the measurement_condition_factors of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The measurement_condition_factors of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: list[QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse]
        """
        return self._measurement_condition_factors

    @measurement_condition_factors.setter
    def measurement_condition_factors(self, measurement_condition_factors):
        """Sets the measurement_condition_factors of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param measurement_condition_factors: The measurement_condition_factors of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: list[QualerApiModelsMeasurementsToUpdateMeasurementConditionFactorResponse]
        """

        self._measurement_condition_factors = measurement_condition_factors

    @property
    def primary_measurement_tool(self):
        """Gets the primary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The primary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel
        """
        return self._primary_measurement_tool

    @primary_measurement_tool.setter
    def primary_measurement_tool(self, primary_measurement_tool):
        """Sets the primary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param primary_measurement_tool: The primary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel
        """

        self._primary_measurement_tool = primary_measurement_tool

    @property
    def secondary_measurement_tool(self):
        """Gets the secondary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501


        :return: The secondary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :rtype: QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel
        """
        return self._secondary_measurement_tool

    @secondary_measurement_tool.setter
    def secondary_measurement_tool(self, secondary_measurement_tool):
        """Sets the secondary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.


        :param secondary_measurement_tool: The secondary_measurement_tool of this QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel.  # noqa: E501
        :type: QualerApiModelsMeasurementsToUpdateMeasurementToolResponseModel
        """

        self._secondary_measurement_tool = secondary_measurement_tool

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
        if issubclass(QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel, dict):
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
        if not isinstance(other, QualerApiModelsMeasurementsToUpdateMeasurementPointResponseModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
