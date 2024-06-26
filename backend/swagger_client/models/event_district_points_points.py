# coding: utf-8

"""
    The Blue Alliance API v3

    # Overview    Information and statistics about FIRST Robotics Competition teams and events.   # Authentication   All endpoints require an Auth Key to be passed in the header `X-TBA-Auth-Key`. If you do not have an auth key yet, you can obtain one from your [Account Page](/account).    A `User-Agent` header may need to be set to prevent a 403 Unauthorized error.  # noqa: E501

    OpenAPI spec version: 3.04.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class EventDistrictPointsPoints(object):
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
        'alliance_points': 'int',
        'award_points': 'int',
        'qual_points': 'int',
        'elim_points': 'int',
        'total': 'int'
    }

    attribute_map = {
        'alliance_points': 'alliance_points',
        'award_points': 'award_points',
        'qual_points': 'qual_points',
        'elim_points': 'elim_points',
        'total': 'total'
    }

    def __init__(self, alliance_points=None, award_points=None, qual_points=None, elim_points=None, total=None):  # noqa: E501
        """EventDistrictPointsPoints - a model defined in Swagger"""  # noqa: E501

        self._alliance_points = None
        self._award_points = None
        self._qual_points = None
        self._elim_points = None
        self._total = None
        self.discriminator = None

        self.alliance_points = alliance_points
        self.award_points = award_points
        self.qual_points = qual_points
        self.elim_points = elim_points
        self.total = total

    @property
    def alliance_points(self):
        """Gets the alliance_points of this EventDistrictPointsPoints.  # noqa: E501

        Points awarded for alliance selection  # noqa: E501

        :return: The alliance_points of this EventDistrictPointsPoints.  # noqa: E501
        :rtype: int
        """
        return self._alliance_points

    @alliance_points.setter
    def alliance_points(self, alliance_points):
        """Sets the alliance_points of this EventDistrictPointsPoints.

        Points awarded for alliance selection  # noqa: E501

        :param alliance_points: The alliance_points of this EventDistrictPointsPoints.  # noqa: E501
        :type: int
        """
        if alliance_points is None:
            raise ValueError("Invalid value for `alliance_points`, must not be `None`")  # noqa: E501

        self._alliance_points = alliance_points

    @property
    def award_points(self):
        """Gets the award_points of this EventDistrictPointsPoints.  # noqa: E501

        Points awarded for event awards.  # noqa: E501

        :return: The award_points of this EventDistrictPointsPoints.  # noqa: E501
        :rtype: int
        """
        return self._award_points

    @award_points.setter
    def award_points(self, award_points):
        """Sets the award_points of this EventDistrictPointsPoints.

        Points awarded for event awards.  # noqa: E501

        :param award_points: The award_points of this EventDistrictPointsPoints.  # noqa: E501
        :type: int
        """
        if award_points is None:
            raise ValueError("Invalid value for `award_points`, must not be `None`")  # noqa: E501

        self._award_points = award_points

    @property
    def qual_points(self):
        """Gets the qual_points of this EventDistrictPointsPoints.  # noqa: E501

        Points awarded for qualification match performance.  # noqa: E501

        :return: The qual_points of this EventDistrictPointsPoints.  # noqa: E501
        :rtype: int
        """
        return self._qual_points

    @qual_points.setter
    def qual_points(self, qual_points):
        """Sets the qual_points of this EventDistrictPointsPoints.

        Points awarded for qualification match performance.  # noqa: E501

        :param qual_points: The qual_points of this EventDistrictPointsPoints.  # noqa: E501
        :type: int
        """
        if qual_points is None:
            raise ValueError("Invalid value for `qual_points`, must not be `None`")  # noqa: E501

        self._qual_points = qual_points

    @property
    def elim_points(self):
        """Gets the elim_points of this EventDistrictPointsPoints.  # noqa: E501

        Points awarded for elimination match performance.  # noqa: E501

        :return: The elim_points of this EventDistrictPointsPoints.  # noqa: E501
        :rtype: int
        """
        return self._elim_points

    @elim_points.setter
    def elim_points(self, elim_points):
        """Sets the elim_points of this EventDistrictPointsPoints.

        Points awarded for elimination match performance.  # noqa: E501

        :param elim_points: The elim_points of this EventDistrictPointsPoints.  # noqa: E501
        :type: int
        """
        if elim_points is None:
            raise ValueError("Invalid value for `elim_points`, must not be `None`")  # noqa: E501

        self._elim_points = elim_points

    @property
    def total(self):
        """Gets the total of this EventDistrictPointsPoints.  # noqa: E501

        Total points awarded at this event.  # noqa: E501

        :return: The total of this EventDistrictPointsPoints.  # noqa: E501
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this EventDistrictPointsPoints.

        Total points awarded at this event.  # noqa: E501

        :param total: The total of this EventDistrictPointsPoints.  # noqa: E501
        :type: int
        """
        if total is None:
            raise ValueError("Invalid value for `total`, must not be `None`")  # noqa: E501

        self._total = total

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
        if issubclass(EventDistrictPointsPoints, dict):
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
        if not isinstance(other, EventDistrictPointsPoints):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
