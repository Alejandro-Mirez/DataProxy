from coffee_freaks_api_client.models import RoasterRequestEntity, RoasterResult, CoffeeResultWithRoaster, CoffeeRequestEntity, CoffeeKind, Grammage, UnitType
from app.src.data_store import DataStore


def test_save_new_roaster(mocker):
    mock_client = mocker.Mock()
    mock_client.get_all_roasters.return_value = []

    data_store = DataStore(mock_client)

    test_roaster = RoasterRequestEntity(name="name", full_address="fullName")
    data_store.save_roaster(test_roaster)
    assert mock_client.add_roaster.called

def test_save_existing_roaster(mocker):
    mock_client = mocker.Mock()
    mock_client.get_all_roasters.return_value = [
        RoasterResult(id="id", name="name", full_address="fullName", created="created", updated="updated")
    ]

    data_store = DataStore(mock_client)

    test_roaster = RoasterRequestEntity(name="name", full_address="fullName")
    data_store.save_roaster(test_roaster)
    assert mock_client.update_roaster.called
    mock_client.update_roaster.assert_called_with("id", test_roaster)

def test_save_another_roaster(mocker):
    mock_client = mocker.Mock()
    mock_client.get_all_roasters.return_value = [
        RoasterResult(id="id", name="name", full_address="fullName", created="created", updated="updated")
    ]

    data_store = DataStore(mock_client)

    test_roaster = RoasterRequestEntity(name="diff_name", full_address="diff_fullName")
    data_store.save_roaster(test_roaster)
    assert mock_client.add_roaster.called

def test_save_new_coffee(mocker):
    mock_client = mocker.Mock()
    mock_client.get_all_coffee_with_rosters.return_value = []

    data_store = DataStore(mock_client)

    test_coffee = CoffeeRequestEntity(name="name", grammage=[Grammage(150, UnitType.GRAM)], kind=CoffeeKind.GROUND, speciality=False)
    test_roaster = RoasterResult(id="id", name="name", full_address="fullName", created="created", updated="updated")

    data_store.save_coffee(test_roaster, test_coffee)
    assert mock_client.add_coffee.called


def test_save_existing_coffee(mocker):
    mock_client = mocker.Mock()

    test_roaster = RoasterResult(id="r_id", name="r_name", full_address="r_fullName", created="r_created", updated="r_updated")

    mock_client.get_all_coffee_with_rosters.return_value = [
        CoffeeResultWithRoaster(id="c_id", roaster=test_roaster, name="c_name", grammage=[Grammage(150, UnitType.GRAM)], kind=CoffeeKind.GROUND, speciality=False, created="c_created", updated="c_updated")
    ]
    data_store = DataStore(mock_client)

    test_coffee = CoffeeRequestEntity(name="c_name", grammage=[Grammage(150, UnitType.GRAM)], kind=CoffeeKind.GROUND, speciality=False)

    data_store.save_coffee(test_roaster, test_coffee)
    assert mock_client.update_coffee.called
    mock_client.update_coffee.assert_called_with("r_id", "c_id", test_coffee)


def save_another_coffee(mocker):
    mock_client = mocker.Mock()
    test_roaster = RoasterResult(id="r_id", name="r_name", full_address="r_fullName", created="r_created", updated="r_updated")

    mock_client.get_all_coffee_with_rosters.return_value = [
        CoffeeResultWithRoaster(id="c_id", roaster=test_roaster, name="c_name", grammage=[Grammage(150, UnitType.GRAM)], kind=CoffeeKind.GROUND, speciality=False, created="c_created", updated="c_updated")
    ]

    data_store = DataStore(mock_client)

    new_coffee = CoffeeRequestEntity(name="new_name", grammage=[Grammage(150, UnitType.GRAM)], kind=CoffeeKind.GROUND, speciality=False)
    new_roaster = RoasterResult(id="new_id", name="new_name", full_address="new_fullName", created="created", updated="updated")

    data_store.save_coffee(new_roaster, new_coffee)
    assert mock_client.add_coffee.called
