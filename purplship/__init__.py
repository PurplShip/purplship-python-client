# coding: utf-8

# flake8: noqa

"""
    Purplship Open Source Multi-carrier Shipping API

     Purplship is an open source multi-carrier shipping API that simplifies the integration of logistic carrier services  The **proxy** endpoints are stateless and forwards calls to carriers web services.   # noqa: E501

    OpenAPI spec version: v1-2020.10.0
    Contact: hello@purplship.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

# import apis into sdk package
from purplship.api.addresses_api import AddressesApi
from purplship.api.carriers_api import CarriersApi
from purplship.api.customs_api import CustomsApi
from purplship.api.parcels_api import ParcelsApi
from purplship.api.pickups_api import PickupsApi
from purplship.api.rates_api import RatesApi
from purplship.api.shipments_api import ShipmentsApi
from purplship.api.shipping_api import ShippingApi
from purplship.api.tracking_api import TrackingApi
from purplship.api.utils_api import UtilsApi

# import ApiClient
from purplship.api_client import ApiClient
from purplship.configuration import Configuration


api_key = None
api_key_prefix = 'Token'
host = None
api_client = None

configuration = Configuration()


def init_client():
    global api_client
    if (api_client is not None) and (host == configuration.host) and (api_key == configuration.api_key['Authorization']):
        return api_client

    configuration.host = host
    configuration.api_key['Authorization'] = f'{api_key_prefix} {api_key}'
    api_client = ApiClient(configuration)
    return api_client


class Addresses:

    @staticmethod
    def create(*args, **kwargs):
        return AddressesApi(init_client()).create(*args, **kwargs)

    @staticmethod
    def list(*args, **kwargs):
        return AddressesApi(init_client()).list(*args, **kwargs)

    @staticmethod
    def retrieve(*args, **kwargs):
        return AddressesApi(init_client()).retrieve(*args, **kwargs)

    @staticmethod
    def update(*args, **kwargs):
        return AddressesApi(init_client()).update(*args, **kwargs)


class Carriers:

    @staticmethod
    def list(*args, **kwargs):
        return CarriersApi(init_client()).list(*args, **kwargs)


class Customs:

    @staticmethod
    def create(*args, **kwargs):
        return CustomsApi(init_client()).create(*args, **kwargs)

    @staticmethod
    def list(*args, **kwargs):
        return CustomsApi(init_client()).list(*args, **kwargs)

    @staticmethod
    def retrieve(*args, **kwargs):
        return CustomsApi(init_client()).retrieve(*args, **kwargs)

    @staticmethod
    def update(*args, **kwargs):
        return CustomsApi(init_client()).update(*args, **kwargs)


class Parcels:

    @staticmethod
    def create(*args, **kwargs):
        return ParcelsApi(init_client()).create(*args, **kwargs)

    @staticmethod
    def list(*args, **kwargs):
        return ParcelsApi(init_client()).list(*args, **kwargs)

    @staticmethod
    def retrieve(*args, **kwargs):
        return ParcelsApi(init_client()).retrieve(*args, **kwargs)

    @staticmethod
    def update(*args, **kwargs):
        return ParcelsApi(init_client()).update(*args, **kwargs)


class Pickups:

    @staticmethod
    def cancel(*args, **kwargs):
        return PickupsApi(init_client()).cancel(*args, **kwargs)

    @staticmethod
    def schedule(*args, **kwargs):
        return PickupsApi(init_client()).schedule(*args, **kwargs)

    @staticmethod
    def update(*args, **kwargs):
        return PickupsApi(init_client()).update(*args, **kwargs)


class Rates:

    @staticmethod
    def fetch(*args, **kwargs):
        return RatesApi(init_client()).fetch(*args, **kwargs)


class Shipments:

    @staticmethod
    def cancel(*args, **kwargs):
        return ShipmentsApi(init_client()).cancel(*args, **kwargs)

    @staticmethod
    def cancel_pickup(*args, **kwargs):
        return ShipmentsApi(init_client()).cancel_pickup(*args, **kwargs)

    @staticmethod
    def create(*args, **kwargs):
        return ShipmentsApi(init_client()).create(*args, **kwargs)

    @staticmethod
    def list(*args, **kwargs):
        return ShipmentsApi(init_client()).list(*args, **kwargs)

    @staticmethod
    def options(*args, **kwargs):
        return ShipmentsApi(init_client()).options(*args, **kwargs)

    @staticmethod
    def pickups(*args, **kwargs):
        return ShipmentsApi(init_client()).pickups(*args, **kwargs)

    @staticmethod
    def purchase(*args, **kwargs):
        return ShipmentsApi(init_client()).purchase(*args, **kwargs)

    @staticmethod
    def rates(*args, **kwargs):
        return ShipmentsApi(init_client()).rates(*args, **kwargs)

    @staticmethod
    def retrieve(*args, **kwargs):
        return ShipmentsApi(init_client()).retrieve(*args, **kwargs)

    @staticmethod
    def retrieve_pickup(*args, **kwargs):
        return ShipmentsApi(init_client()).retrieve_pickup(*args, **kwargs)

    @staticmethod
    def schedule_pickup(*args, **kwargs):
        return ShipmentsApi(init_client()).schedule_pickup(*args, **kwargs)

    @staticmethod
    def track(*args, **kwargs):
        return ShipmentsApi(init_client()).track(*args, **kwargs)

    @staticmethod
    def tracking_statuses(*args, **kwargs):
        return ShipmentsApi(init_client()).tracking_statuses(*args, **kwargs)

    @staticmethod
    def update_pickup(*args, **kwargs):
        return ShipmentsApi(init_client()).update_pickup(*args, **kwargs)


class Shipping:

    @staticmethod
    def buy_label(*args, **kwargs):
        return ShippingApi(init_client()).buy_label(*args, **kwargs)

    @staticmethod
    def void_label(*args, **kwargs):
        return ShippingApi(init_client()).void_label(*args, **kwargs)


class Tracking:

    @staticmethod
    def fetch(*args, **kwargs):
        return TrackingApi(init_client()).fetch(*args, **kwargs)


class Utils:

    @staticmethod
    def print_label(*args, **kwargs):
        return UtilsApi(init_client()).print_label(*args, **kwargs)

    @staticmethod
    def references(*args, **kwargs):
        return UtilsApi(init_client()).references(*args, **kwargs)
