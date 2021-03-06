# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2020.10.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class PickupResponse(object):
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
        'messages': 'list[Message]',
        'pickup': 'Pickup'
    }

    attribute_map = {
        'messages': 'messages',
        'pickup': 'pickup'
    }

    def __init__(self, messages=None, pickup=None):  # noqa: E501
        """PickupResponse - a model defined in Swagger"""  # noqa: E501
        self._messages = None
        self._pickup = None
        self.discriminator = None
        if messages is not None:
            self.messages = messages
        if pickup is not None:
            self.pickup = pickup

    @property
    def messages(self):
        """Gets the messages of this PickupResponse.  # noqa: E501

        The list of note or warning messages  # noqa: E501

        :return: The messages of this PickupResponse.  # noqa: E501
        :rtype: list[Message]
        """
        return self._messages

    @messages.setter
    def messages(self, messages):
        """Sets the messages of this PickupResponse.

        The list of note or warning messages  # noqa: E501

        :param messages: The messages of this PickupResponse.  # noqa: E501
        :type: list[Message]
        """

        self._messages = messages

    @property
    def pickup(self):
        """Gets the pickup of this PickupResponse.  # noqa: E501


        :return: The pickup of this PickupResponse.  # noqa: E501
        :rtype: Pickup
        """
        return self._pickup

    @pickup.setter
    def pickup(self, pickup):
        """Sets the pickup of this PickupResponse.


        :param pickup: The pickup of this PickupResponse.  # noqa: E501
        :type: Pickup
        """

        self._pickup = pickup

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
        if issubclass(PickupResponse, dict):
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
        if not isinstance(other, PickupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
