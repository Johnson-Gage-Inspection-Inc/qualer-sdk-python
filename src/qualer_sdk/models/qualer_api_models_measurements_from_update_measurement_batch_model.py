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


class QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel(object):
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
        "batch_id": "int",
        "batch_type": "str",
        "save_and_delete_empty": "bool",
        "measurement_sets": "list[QualerApiModelsMeasurementsFromUpdateMeasurementSetModel]",
    }

    attribute_map = {
        "batch_id": "BatchId",
        "batch_type": "BatchType",
        "save_and_delete_empty": "SaveAndDeleteEmpty",
        "measurement_sets": "MeasurementSets",
    }

    def __init__(
        self,
        batch_id=None,
        batch_type=None,
        save_and_delete_empty=None,
        measurement_sets=None,
        _configuration=None,
    ):  # noqa: E501
        """QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._batch_id = None
        self._batch_type = None
        self._save_and_delete_empty = None
        self._measurement_sets = None
        self.discriminator = None

        if batch_id is not None:
            self.batch_id = batch_id
        if batch_type is not None:
            self.batch_type = batch_type
        if save_and_delete_empty is not None:
            self.save_and_delete_empty = save_and_delete_empty
        if measurement_sets is not None:
            self.measurement_sets = measurement_sets

    @property
    def batch_id(self):
        """Gets the batch_id of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501


        :return: The batch_id of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :rtype: int
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        """Sets the batch_id of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.


        :param batch_id: The batch_id of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :type: int
        """

        self._batch_id = batch_id

    @property
    def batch_type(self):
        """Gets the batch_type of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501


        :return: The batch_type of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :rtype: str
        """
        return self._batch_type

    @batch_type.setter
    def batch_type(self, batch_type):
        """Sets the batch_type of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.


        :param batch_type: The batch_type of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :type: str
        """

        self._batch_type = batch_type

    @property
    def save_and_delete_empty(self):
        """Gets the save_and_delete_empty of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501


        :return: The save_and_delete_empty of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :rtype: bool
        """
        return self._save_and_delete_empty

    @save_and_delete_empty.setter
    def save_and_delete_empty(self, save_and_delete_empty):
        """Sets the save_and_delete_empty of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.


        :param save_and_delete_empty: The save_and_delete_empty of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :type: bool
        """

        self._save_and_delete_empty = save_and_delete_empty

    @property
    def measurement_sets(self):
        """Gets the measurement_sets of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501


        :return: The measurement_sets of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :rtype: list[QualerApiModelsMeasurementsFromUpdateMeasurementSetModel]
        """
        return self._measurement_sets

    @measurement_sets.setter
    def measurement_sets(self, measurement_sets):
        """Sets the measurement_sets of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.


        :param measurement_sets: The measurement_sets of this QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel.  # noqa: E501
        :type: list[QualerApiModelsMeasurementsFromUpdateMeasurementSetModel]
        """

        self._measurement_sets = measurement_sets

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
        if issubclass(QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel, dict):
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
            other, QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel
        ):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(
            other, QualerApiModelsMeasurementsFromUpdateMeasurementBatchModel
        ):
            return True

        return self.to_dict() != other.to_dict()
