# coding: utf-8

from __future__ import absolute_import

from datetime import date, datetime  # noqa: F401
from typing import Dict, List  # noqa: F401

from app import util
from app.api.models.base_model_ import Model
from app.api.models.coordinates import Coordinates  # noqa: F401,E501
from app.api.models.quantity import Quantity  # noqa: F401,E501


class Demand(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(
        self, location: Coordinates = None, quantity: Quantity = None
    ):  # noqa: E501
        """Demand - a model defined in Swagger

        :param location: The location of this Demand.  # noqa: E501
        :type location: Coordinates
        :param quantity: The quantity of this Demand.  # noqa: E501
        :type quantity: Quantity
        """
        self.swagger_types = {"location": Coordinates, "quantity": Quantity}

        self.attribute_map = {"location": "location", "quantity": "quantity"}
        self._location = location
        self._quantity = quantity

    @classmethod
    def from_dict(cls, dikt) -> "Demand":
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Demand of this Demand.  # noqa: E501
        :rtype: Demand
        """
        return util.deserialize_model(dikt, cls)

    @property
    def location(self) -> Coordinates:
        """Gets the location of this Demand.


        :return: The location of this Demand.
        :rtype: Coordinates
        """
        return self._location

    @location.setter
    def location(self, location: Coordinates):
        """Sets the location of this Demand.


        :param location: The location of this Demand.
        :type location: Coordinates
        """
        if location is None:
            raise ValueError(
                "Invalid value for `location`, must not be `None`"
            )  # noqa: E501

        self._location = location

    @property
    def quantity(self) -> Quantity:
        """Gets the quantity of this Demand.


        :return: The quantity of this Demand.
        :rtype: Quantity
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity: Quantity):
        """Sets the quantity of this Demand.


        :param quantity: The quantity of this Demand.
        :type quantity: Quantity
        """
        if quantity is None:
            raise ValueError(
                "Invalid value for `quantity`, must not be `None`"
            )  # noqa: E501

        self._quantity = quantity
