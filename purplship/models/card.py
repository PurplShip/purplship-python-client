# coding: utf-8

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2020.8.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class Card(object):
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
        'type': 'str',
        'number': 'str',
        'expiry_month': 'str',
        'expiry_year': 'str',
        'security_code': 'str',
        'name': 'str',
        'postal_code': 'str'
    }

    attribute_map = {
        'type': 'type',
        'number': 'number',
        'expiry_month': 'expiryMonth',
        'expiry_year': 'expiryYear',
        'security_code': 'securityCode',
        'name': 'name',
        'postal_code': 'postalCode'
    }

    def __init__(self, type=None, number=None, expiry_month=None, expiry_year=None, security_code=None, name=None, postal_code=None):  # noqa: E501
        """Card - a model defined in Swagger"""  # noqa: E501

        self._type = None
        self._number = None
        self._expiry_month = None
        self._expiry_year = None
        self._security_code = None
        self._name = None
        self._postal_code = None
        self.discriminator = None

        self.type = type
        self.number = number
        self.expiry_month = expiry_month
        self.expiry_year = expiry_year
        self.security_code = security_code
        if name is not None:
            self.name = name
        if postal_code is not None:
            self.postal_code = postal_code

    @property
    def type(self):
        """Gets the type of this Card.  # noqa: E501

        The credit card type  # noqa: E501

        :return: The type of this Card.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Card.

        The credit card type  # noqa: E501

        :param type: The type of this Card.  # noqa: E501
        :type: str
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")  # noqa: E501
        if type is not None and len(type) < 1:
            raise ValueError("Invalid value for `type`, length must be greater than or equal to `1`")  # noqa: E501

        self._type = type

    @property
    def number(self):
        """Gets the number of this Card.  # noqa: E501

        The credit card number  # noqa: E501

        :return: The number of this Card.  # noqa: E501
        :rtype: str
        """
        return self._number

    @number.setter
    def number(self, number):
        """Sets the number of this Card.

        The credit card number  # noqa: E501

        :param number: The number of this Card.  # noqa: E501
        :type: str
        """
        if number is None:
            raise ValueError("Invalid value for `number`, must not be `None`")  # noqa: E501
        if number is not None and len(number) < 1:
            raise ValueError("Invalid value for `number`, length must be greater than or equal to `1`")  # noqa: E501

        self._number = number

    @property
    def expiry_month(self):
        """Gets the expiry_month of this Card.  # noqa: E501

        The credit card expiry month (MM)  # noqa: E501

        :return: The expiry_month of this Card.  # noqa: E501
        :rtype: str
        """
        return self._expiry_month

    @expiry_month.setter
    def expiry_month(self, expiry_month):
        """Sets the expiry_month of this Card.

        The credit card expiry month (MM)  # noqa: E501

        :param expiry_month: The expiry_month of this Card.  # noqa: E501
        :type: str
        """
        if expiry_month is None:
            raise ValueError("Invalid value for `expiry_month`, must not be `None`")  # noqa: E501
        if expiry_month is not None and len(expiry_month) < 1:
            raise ValueError("Invalid value for `expiry_month`, length must be greater than or equal to `1`")  # noqa: E501

        self._expiry_month = expiry_month

    @property
    def expiry_year(self):
        """Gets the expiry_year of this Card.  # noqa: E501

        The credit card expiry year (YYYY)  # noqa: E501

        :return: The expiry_year of this Card.  # noqa: E501
        :rtype: str
        """
        return self._expiry_year

    @expiry_year.setter
    def expiry_year(self, expiry_year):
        """Sets the expiry_year of this Card.

        The credit card expiry year (YYYY)  # noqa: E501

        :param expiry_year: The expiry_year of this Card.  # noqa: E501
        :type: str
        """
        if expiry_year is None:
            raise ValueError("Invalid value for `expiry_year`, must not be `None`")  # noqa: E501
        if expiry_year is not None and len(expiry_year) < 1:
            raise ValueError("Invalid value for `expiry_year`, length must be greater than or equal to `1`")  # noqa: E501

        self._expiry_year = expiry_year

    @property
    def security_code(self):
        """Gets the security_code of this Card.  # noqa: E501

        The credit card security code often at the back (000)  # noqa: E501

        :return: The security_code of this Card.  # noqa: E501
        :rtype: str
        """
        return self._security_code

    @security_code.setter
    def security_code(self, security_code):
        """Sets the security_code of this Card.

        The credit card security code often at the back (000)  # noqa: E501

        :param security_code: The security_code of this Card.  # noqa: E501
        :type: str
        """
        if security_code is None:
            raise ValueError("Invalid value for `security_code`, must not be `None`")  # noqa: E501
        if security_code is not None and len(security_code) < 1:
            raise ValueError("Invalid value for `security_code`, length must be greater than or equal to `1`")  # noqa: E501

        self._security_code = security_code

    @property
    def name(self):
        """Gets the name of this Card.  # noqa: E501

        The name inscribed on the credit card  # noqa: E501

        :return: The name of this Card.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Card.

        The name inscribed on the credit card  # noqa: E501

        :param name: The name of this Card.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def postal_code(self):
        """Gets the postal_code of this Card.  # noqa: E501

        The credit card registration address postal code  # noqa: E501

        :return: The postal_code of this Card.  # noqa: E501
        :rtype: str
        """
        return self._postal_code

    @postal_code.setter
    def postal_code(self, postal_code):
        """Sets the postal_code of this Card.

        The credit card registration address postal code  # noqa: E501

        :param postal_code: The postal_code of this Card.  # noqa: E501
        :type: str
        """

        self._postal_code = postal_code

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
        if issubclass(Card, dict):
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
        if not isinstance(other, Card):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
