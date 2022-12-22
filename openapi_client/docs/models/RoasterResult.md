# openapi_client.model.roaster_result.RoasterResult

## Model Type Info
Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | -------------
dict, frozendict.frozendict,  | frozendict.frozendict,  |  | 

### Dictionary Keys
Key | Input Type | Accessed Type | Description | Notes
------------ | ------------- | ------------- | ------------- | -------------
**created** | str,  | str,  | When it was created | 
**name** | str,  | str,  | Label name of roaster | 
**fullName** | str,  | str,  | Full name of roaster | 
**id** | str, uuid.UUID,  | str,  | Roaster id | value must be a uuid
**updated** | str,  | str,  | When was updated | 
**country** | str,  | str,  | From what country roaster origin | [optional] 
**city** | str,  | str,  | In what city roaster originate | [optional] 
**any_string_name** | dict, frozendict.frozendict, str, date, datetime, int, float, bool, decimal.Decimal, None, list, tuple, bytes, io.FileIO, io.BufferedReader | frozendict.frozendict, str, BoolClass, decimal.Decimal, NoneClass, tuple, bytes, FileIO | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../../README.md#documentation-for-models) [[Back to API list]](../../README.md#documentation-for-api-endpoints) [[Back to README]](../../README.md)

