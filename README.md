# purplship-python

Purplship is a Multi-carrier Shipping API that simplifies the integration of logistic carrier services.

Visit [purplship.com](https://purplship.com) to deploy your private cloud multi-carrier shipping API instance.

## Documentation

See the full [Python API docs](https://docs.purplship.com/#/guide).

## Requirements

Python 3.4+

## Installation & Usage

### pip install

```sh
pip install purplship-python
```

Then import the package:

```python
import purplship
```

### Usage

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import purplship
from purplship.rest import ApiException
from pprint import pprint

# Configure API key authorization: Token
purplship.api_key = 'YOUR_API_KEY'
purplship.host = 'https://instance.purplship.api/v1'

try:
    api_response = purplship.Carriers.list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling purplship.Carriers->list: %s\n" % e)

```

## Documentation For Models

- [Address](docs/Address.md)
- [AddressData](docs/AddressData.md)
- [Card](docs/Card.md)
- [CarrierSettings](docs/CarrierSettings.md)
- [Charge](docs/Charge.md)
- [Commodity](docs/Commodity.md)
- [Customs](docs/Customs.md)
- [CustomsData](docs/CustomsData.md)
- [Doc](docs/Doc.md)
- [ErrorResponse](docs/ErrorResponse.md)
- [LabelPrintingRequest](docs/LabelPrintingRequest.md)
- [Message](docs/Message.md)
- [OperationConfirmation](docs/OperationConfirmation.md)
- [OperationResponse](docs/OperationResponse.md)
- [Parcel](docs/Parcel.md)
- [ParcelData](docs/ParcelData.md)
- [Payment](docs/Payment.md)
- [PaymentData](docs/PaymentData.md)
- [Pickup](docs/Pickup.md)
- [PickupCancelData](docs/PickupCancelData.md)
- [PickupCancelRequest](docs/PickupCancelRequest.md)
- [PickupData](docs/PickupData.md)
- [PickupRequest](docs/PickupRequest.md)
- [PickupResponse](docs/PickupResponse.md)
- [PickupUpdateData](docs/PickupUpdateData.md)
- [PickupUpdateRequest](docs/PickupUpdateRequest.md)
- [Rate](docs/Rate.md)
- [RateRequest](docs/RateRequest.md)
- [RateResponse](docs/RateResponse.md)
- [References](docs/References.md)
- [Shipment](docs/Shipment.md)
- [ShipmentCancelRequest](docs/ShipmentCancelRequest.md)
- [ShipmentData](docs/ShipmentData.md)
- [ShipmentPurchaseData](docs/ShipmentPurchaseData.md)
- [ShipmentResponse](docs/ShipmentResponse.md)
- [ShippingRequest](docs/ShippingRequest.md)
- [TrackingEvent](docs/TrackingEvent.md)
- [TrackingResponse](docs/TrackingResponse.md)
- [TrackingStatus](docs/TrackingStatus.md)

## Author

PurplShip Team | hello@purplship.com | [purplship.com](https://purplship.com)
