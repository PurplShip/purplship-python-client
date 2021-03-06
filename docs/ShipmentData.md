# ShipmentData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**shipper** | [**AddressData**](AddressData.md) |  | 
**recipient** | [**AddressData**](AddressData.md) |  | 
**parcels** | [**list[ParcelData]**](ParcelData.md) | The shipment&#x27;s parcels | 
**options** | **object** |  The options available for the shipment.Please consult the reference for additional specific carriers options.  | [optional] 
**payment** | [**PaymentData**](PaymentData.md) |  | [optional] 
**customs** | [**CustomsData**](CustomsData.md) |  | [optional] 
**doc_images** | [**list[Doc]**](Doc.md) |  The list of documents to attach for a paperless interantional trade.  eg: Invoices...  | [optional] 
**reference** | **str** | The shipment reference | [optional] 
**services** | **list[str]** |  The requested carrier service for the shipment.  Please consult the reference for specific carriers services.Note that this is a list because on a Multi-carrier rate request you could specify a service per carrier.  | [optional] 
**carrier_ids** | **list[str]** |  The list of configured carriers you wish to get rates from.  *Note that the request will be sent to all carriers in nothing is specified*  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

