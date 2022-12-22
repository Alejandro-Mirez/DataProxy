# openapi_client.model.get_roaster_coffee_result.GetRoasterCoffeeResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**count** | decimal.Decimal, int,  | decimal.Decimal,  | Count of all results | value must be a 64 bit integer
**parameters** | [**GetRoasterCoffeeParameters**](GetRoasterCoffeeParameters.md) | [**GetRoasterCoffeeParameters**](GetRoasterCoffeeParameters.md) |  | 
**[results](#results)** | list, tuple,  | tuple,  | Results in actual page | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# results

Results in actual page

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Results in actual page | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**CoffeeResult**](CoffeeResult.md) | [**CoffeeResult**](CoffeeResult.md) | [**CoffeeResult**](CoffeeResult.md) |  | 

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

