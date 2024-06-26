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

from swagger_client.models.event_ranking_extra_stats_info import EventRankingExtraStatsInfo  # noqa: F401,E501
from swagger_client.models.event_ranking_rankings import EventRankingRankings  # noqa: F401,E501
from swagger_client.models.event_ranking_sort_order_info import EventRankingSortOrderInfo  # noqa: F401,E501


class EventRanking(object):
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
        'rankings': 'list[EventRankingRankings]',
        'extra_stats_info': 'list[EventRankingExtraStatsInfo]',
        'sort_order_info': 'list[EventRankingSortOrderInfo]'
    }

    attribute_map = {
        'rankings': 'rankings',
        'extra_stats_info': 'extra_stats_info',
        'sort_order_info': 'sort_order_info'
    }

    def __init__(self, rankings=None, extra_stats_info=None, sort_order_info=None):  # noqa: E501
        """EventRanking - a model defined in Swagger"""  # noqa: E501

        self._rankings = None
        self._extra_stats_info = None
        self._sort_order_info = None
        self.discriminator = None

        self.rankings = rankings
        if extra_stats_info is not None:
            self.extra_stats_info = extra_stats_info
        self.sort_order_info = sort_order_info

    @property
    def rankings(self):
        """Gets the rankings of this EventRanking.  # noqa: E501

        List of rankings at the event.  # noqa: E501

        :return: The rankings of this EventRanking.  # noqa: E501
        :rtype: list[EventRankingRankings]
        """
        return self._rankings

    @rankings.setter
    def rankings(self, rankings):
        """Sets the rankings of this EventRanking.

        List of rankings at the event.  # noqa: E501

        :param rankings: The rankings of this EventRanking.  # noqa: E501
        :type: list[EventRankingRankings]
        """
        if rankings is None:
            raise ValueError("Invalid value for `rankings`, must not be `None`")  # noqa: E501

        self._rankings = rankings

    @property
    def extra_stats_info(self):
        """Gets the extra_stats_info of this EventRanking.  # noqa: E501

        List of special TBA-generated values provided in the `extra_stats` array for each item.  # noqa: E501

        :return: The extra_stats_info of this EventRanking.  # noqa: E501
        :rtype: list[EventRankingExtraStatsInfo]
        """
        return self._extra_stats_info

    @extra_stats_info.setter
    def extra_stats_info(self, extra_stats_info):
        """Sets the extra_stats_info of this EventRanking.

        List of special TBA-generated values provided in the `extra_stats` array for each item.  # noqa: E501

        :param extra_stats_info: The extra_stats_info of this EventRanking.  # noqa: E501
        :type: list[EventRankingExtraStatsInfo]
        """

        self._extra_stats_info = extra_stats_info

    @property
    def sort_order_info(self):
        """Gets the sort_order_info of this EventRanking.  # noqa: E501

        List of year-specific values provided in the `sort_orders` array for each team.  # noqa: E501

        :return: The sort_order_info of this EventRanking.  # noqa: E501
        :rtype: list[EventRankingSortOrderInfo]
        """
        return self._sort_order_info

    @sort_order_info.setter
    def sort_order_info(self, sort_order_info):
        """Sets the sort_order_info of this EventRanking.

        List of year-specific values provided in the `sort_orders` array for each team.  # noqa: E501

        :param sort_order_info: The sort_order_info of this EventRanking.  # noqa: E501
        :type: list[EventRankingSortOrderInfo]
        """
        if sort_order_info is None:
            raise ValueError("Invalid value for `sort_order_info`, must not be `None`")  # noqa: E501

        self._sort_order_info = sort_order_info

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
        if issubclass(EventRanking, dict):
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
        if not isinstance(other, EventRanking):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
