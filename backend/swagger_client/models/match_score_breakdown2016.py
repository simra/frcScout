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

from swagger_client.models.match_score_breakdown2016_alliance import MatchScoreBreakdown2016Alliance  # noqa: F401,E501


class MatchScoreBreakdown2016(object):
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
        'blue': 'MatchScoreBreakdown2016Alliance',
        'red': 'MatchScoreBreakdown2016Alliance'
    }

    attribute_map = {
        'blue': 'blue',
        'red': 'red'
    }

    def __init__(self, blue=None, red=None):  # noqa: E501
        """MatchScoreBreakdown2016 - a model defined in Swagger"""  # noqa: E501

        self._blue = None
        self._red = None
        self.discriminator = None

        if blue is not None:
            self.blue = blue
        if red is not None:
            self.red = red

    @property
    def blue(self):
        """Gets the blue of this MatchScoreBreakdown2016.  # noqa: E501


        :return: The blue of this MatchScoreBreakdown2016.  # noqa: E501
        :rtype: MatchScoreBreakdown2016Alliance
        """
        return self._blue

    @blue.setter
    def blue(self, blue):
        """Sets the blue of this MatchScoreBreakdown2016.


        :param blue: The blue of this MatchScoreBreakdown2016.  # noqa: E501
        :type: MatchScoreBreakdown2016Alliance
        """

        self._blue = blue

    @property
    def red(self):
        """Gets the red of this MatchScoreBreakdown2016.  # noqa: E501


        :return: The red of this MatchScoreBreakdown2016.  # noqa: E501
        :rtype: MatchScoreBreakdown2016Alliance
        """
        return self._red

    @red.setter
    def red(self, red):
        """Sets the red of this MatchScoreBreakdown2016.


        :param red: The red of this MatchScoreBreakdown2016.  # noqa: E501
        :type: MatchScoreBreakdown2016Alliance
        """

        self._red = red

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
        if issubclass(MatchScoreBreakdown2016, dict):
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
        if not isinstance(other, MatchScoreBreakdown2016):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
