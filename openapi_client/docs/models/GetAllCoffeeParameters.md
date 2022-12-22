# openapi_client.model.get_all_coffee_parameters.GetAllCoffeeParameters

Parameters used in query

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  | Parameters used in query | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**offset** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**limit** | decimal.Decimal, int,  | decimal.Decimal,  |  | value must be a 32 bit integer
**kind** | [**CoffeeKind**](CoffeeKind.md) | [**CoffeeKind**](CoffeeKind.md) |  | [optional] 
**created** | [**DataOrdering**](DataOrdering.md) | [**DataOrdering**](DataOrdering.md) |  | [optional] 
**updated** | [**DataOrdering**](DataOrdering.md) | [**DataOrdering**](DataOrdering.md) |  | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

