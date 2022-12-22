# openapi_client.model.patch_coffee_request.PatchCoffeeRequest

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**name** | str,  | str,  | Name of coffee | [optional] 
**grammage** | [**Grammage**](Grammage.md) | [**Grammage**](Grammage.md) |  | [optional] 
**[origin](#origin)** | list, tuple,  | tuple,  | Where coffee beans comes from | [optional] 
**kind** | [**CoffeeKind**](CoffeeKind.md) | [**CoffeeKind**](CoffeeKind.md) |  | [optional] 
**[beans](#beans)** | list, tuple,  | tuple,  | From where coffee comes from (Arabica, Robusta etc.) and in what ratio | [optional] 
**[processing](#processing)** | list, tuple,  | tuple,  | How coffee was processed (Honey, Natural etc.) | [optional] 
**roastingLevel** | decimal.Decimal, int,  | decimal.Decimal,  | Roasting level of beans - 2: Blond, 5: Medium, 8: Dark | [optional] value must be a 32 bit integer
**[dedicated](#dedicated)** | list, tuple,  | tuple,  | Dedicated to what type of brewing | [optional] 
**description** | str,  | str,  | Description of product | [optional] 
**speciality** | bool,  | BoolClass,  | Rated as speciality coffee by roaster | [optional] 
**[roastingDates](#roastingDates)** | list, tuple,  | tuple,  | When coffee was roasted - in format yyyy-MM-dd | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

# origin

Where coffee beans comes from

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Where coffee beans comes from | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str,  | str,  |  | 

# beans

From where coffee comes from (Arabica, Robusta etc.) and in what ratio

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | From where coffee comes from (Arabica, Robusta etc.) and in what ratio | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Beans**](Beans.md) | [**Beans**](Beans.md) | [**Beans**](Beans.md) |  | 

# processing

How coffee was processed (Honey, Natural etc.)

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | How coffee was processed (Honey, Natural etc.) | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**Processing**](Processing.md) | [**Processing**](Processing.md) | [**Processing**](Processing.md) |  | 

# dedicated

Dedicated to what type of brewing

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | Dedicated to what type of brewing | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
[**BrewingMethod**](BrewingMethod.md) | [**BrewingMethod**](BrewingMethod.md) | [**BrewingMethod**](BrewingMethod.md) |  | 

# roastingDates

When coffee was roasted - in format yyyy-MM-dd

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
list, tuple,  | tuple,  | When coffee was roasted - in format yyyy-MM-dd | 

### Tuple Items
Class Name | Input Type | Accessed Type | Description | Notes
------------- | ------------- | ------------- | ------------- | -------------
items | str, date,  | str,  |  | value must conform to RFC-3339 full-date YYYY-MM-DD

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

