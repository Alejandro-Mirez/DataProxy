import os.path

import pytest

from coffee_freaks_api_client.models import RoasterRequestEntity, CoffeeRequestEntity, Grammage, UnitType, CoffeeKind, \
    Beans, BeansKind, Processing, BrewingMethod, RoasterResult, CoffeeResult
from coffee_freaks_api_client.types import UNSET
from app.src.data_service import DataService
from app.src.model import Item
import json
import datetime

json_file = open(f'{os.path.dirname(__file__)}/data.json', encoding='utf8')
jsons = json.load(json_file)

default_roaster_result = RoasterResult(id="id", name="name", full_address="fullName", created="created",
                                       updated="updated")
default_coffee_result = CoffeeResult(id="id", roaster_id="roaster_id", name="c_name",
                                     grammage=[Grammage(250, UnitType.GRAM)], kind=CoffeeKind.BEANS, speciality=False,
                                     created="c_created", updated="c_updated")


def test_johan_1(mocker):
    mock_data_store = mocker.Mock()

    mock_data_store.save_roaster.return_value = default_roaster_result
    mock_data_store.save_coffee.return_value = default_coffee_result

    data_service = DataService(mock_data_store)

    item = Item.parse_obj(jsons[0])

    expected_roaster = RoasterRequestEntity(name="Johan & Nyström",
                                            full_address="Johan & Nystrom Kafferostare Tehandlare Hamringevagen 1 14641 Tullinge, Sweden / Szwecja",
                                            country="Sweden", city="Tullinge")
    expected_coffee = CoffeeRequestEntity(name="Etiopia Guji Filter 250g", grammage=[Grammage(250, UnitType.GRAM)],
                                          kind=CoffeeKind.BEANS,
                                          speciality=False, origin=["Etiopia"], beans=[Beans(BeansKind.ARABICA, 1)],
                                          processing=[Processing.NATURAL], roasting_level=2,
                                          dedicated=[BrewingMethod.DRIP], description="description",
                                          roasting_dates=[datetime.date(2022, 11, 14)])

    data_service.process_data(item)

    assert mock_data_store.save_roaster.called
    assert mock_data_store.save_coffee.called

    mock_data_store.save_roaster.assert_called_with(expected_roaster)
    mock_data_store.save_coffee.assert_called_with(default_roaster_result, expected_coffee)


def test_hayb(mocker):
    mock_data_store = mocker.Mock()

    mock_data_store.save_roaster.return_value = default_roaster_result
    mock_data_store.save_coffee.return_value = default_coffee_result

    data_service = DataService(mock_data_store)

    item = Item.parse_obj(jsons[1])

    expected_roaster = RoasterRequestEntity(name="HAYB",
                                            full_address="HAYB Coffee Sp. z o.o. Al. Jerozolimskie 200 02-486 Warszawa",
                                            country="Poland", city="Warsaw")
    expected_coffee = CoffeeRequestEntity(name="Się Przelewa Kwiat 500g", grammage=[Grammage(500, UnitType.GRAM)],
                                          kind=CoffeeKind.BEANS,
                                          speciality=True, origin=["Etiopia"], beans=[Beans(BeansKind.ARABICA, 1)],
                                          processing=[Processing.WASHED], roasting_level=2,
                                          dedicated=[BrewingMethod.DRIP], description="description",
                                          roasting_dates=[datetime.date(2022, 9, 27)])

    data_service.process_data(item)

    assert mock_data_store.save_roaster.called
    assert mock_data_store.save_coffee.called

    mock_data_store.save_roaster.assert_called_with(expected_roaster)
    mock_data_store.save_coffee.assert_called_with(default_roaster_result, expected_coffee)


def test_johan_2(mocker):
    mock_data_store = mocker.Mock()

    mock_data_store.save_roaster.return_value = default_roaster_result
    mock_data_store.save_coffee.return_value = default_coffee_result

    data_service = DataService(mock_data_store)

    item = Item.parse_obj(jsons[2])

    expected_roaster = RoasterRequestEntity(name="Johan & Nyström",
                                            full_address="Johan & Nystrom Kafferostare Tehandlare Hamringevagen 1 14641 Tullinge, Sweden / Szwecja",
                                            country="Sweden", city="Tullinge")
    expected_coffee = CoffeeRequestEntity(name="Fika - Kawa mielona Filter 500g",
                                          grammage=[Grammage(500, UnitType.GRAM)], kind=CoffeeKind.GROUND,
                                          speciality=False, beans=[Beans(BeansKind.ARABICA, 1)], roasting_level=5,
                                          dedicated=[BrewingMethod.DRIP, BrewingMethod.ESPRESSO],
                                          description="description", roasting_dates=[datetime.date(2022, 7, 17)])

    data_service.process_data(item)

    assert mock_data_store.save_roaster.called
    assert mock_data_store.save_coffee.called

    mock_data_store.save_roaster.assert_called_with(expected_roaster)
    mock_data_store.save_coffee.assert_called_with(default_roaster_result, expected_coffee)


def test_illy(mocker):
    mock_data_store = mocker.Mock()

    mock_data_store.save_roaster.return_value = default_roaster_result
    mock_data_store.save_coffee.return_value = default_coffee_result

    data_service = DataService(mock_data_store)

    item = Item.parse_obj(jsons[3])

    expected_roaster = RoasterRequestEntity(name="Illy",
                                            full_address="Illycaffe S.p.A. | P.IVA 00055180327 | Via Flavia 110, 34147 Trieste - Italy / Włochy",
                                            country="Italy", city="Trieste")
    expected_coffee = CoffeeRequestEntity(name="Intenso Bold Roast - Kawa mielona",
                                          grammage=[Grammage(250, UnitType.GRAM)], kind=CoffeeKind.GROUND,
                                          speciality=False, beans=[Beans(BeansKind.ARABICA, 1)], roasting_level=8,
                                          dedicated=[BrewingMethod.ESPRESSO], description="description",
                                          roasting_dates=[datetime.date(2022, 1, 10)])

    data_service.process_data(item)

    assert mock_data_store.save_roaster.called
    assert mock_data_store.save_coffee.called

    mock_data_store.save_roaster.assert_called_with(expected_roaster)
    mock_data_store.save_coffee.assert_called_with(default_roaster_result, expected_coffee)


def test_bialetti(mocker):
    mock_data_store = mocker.Mock()

    mock_data_store.save_roaster.return_value = default_roaster_result
    mock_data_store.save_coffee.return_value = default_coffee_result

    data_service = DataService(mock_data_store)

    item = Item.parse_obj(jsons[4])

    expected_roaster = RoasterRequestEntity(name="Bialetti",
                                            full_address="Beyond The Bean Limited, Cala Trading Estate, Ashton Vale Road, Bristol, England / Anglia",
                                            country="United Kingdom", city="Bristol")
    expected_coffee = CoffeeRequestEntity(name="Milano - 16 Kapsułek", grammage=[Grammage(16, UnitType.PIECE)],
                                          kind=CoffeeKind.CAPSULES,
                                          speciality=False,
                                          beans=[Beans(BeansKind.ARABICA, 0.5), Beans(BeansKind.ROBUSTA, 0.5)],
                                          roasting_level=8, dedicated=[BrewingMethod.ESPRESSO],
                                          description="description")

    data_service.process_data(item)

    assert mock_data_store.save_roaster.called
    assert mock_data_store.save_coffee.called

    mock_data_store.save_roaster.assert_called_with(expected_roaster)
    mock_data_store.save_coffee.assert_called_with(default_roaster_result, expected_coffee)


def test_find_roaster_country_pl_fn(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={
            "Pełna nazwa producenta:": "Poland"
        }
    )
    result = data_service._DataService__find_roaster_country(test_item)
    assert bool(result)


def test_find_roaster_country_pl_tags(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=["Polska"],
        description="",
        details={
            "Pełna nazwa producenta:": ""
        }
    )
    result = data_service._DataService__find_roaster_country(test_item)
    assert bool(result)


def test_find_roaster_country_gb_tags(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=["england"],
        description="",
        details={
            "Pełna nazwa producenta:": ""
        }
    )
    result = data_service._DataService__find_roaster_country(test_item)
    assert bool(result)


def test_find_roaster_country_gb_fn_et_tags(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=["Etiopia"],
        description="",
        details={
            "Pełna nazwa producenta:": "England"
        }
    )
    result = data_service._DataService__find_roaster_country(test_item)
    assert bool(result)


def test_find_roaster_city_pl(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={
            "Pełna nazwa producenta:": "Warszawa"
        }
    )
    result = data_service._DataService__find_roaster_city("PL", test_item)
    assert bool(result)


def test_find_roaster_city_no_fn(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={
            "Pełna nazwa producenta:": ""
        }
    )
    result = data_service._DataService__find_roaster_city("PL", test_item)
    assert not bool(result)


def test_find_roaster_city_no_fn_no_iso(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={
            "Pełna nazwa producenta:": ""
        }
    )
    result = data_service._DataService__find_roaster_city("", test_item)
    assert not bool(result)


def test_create_roaster_ok(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=["polska palarnia"],
        description="",
        details={
            "Producent:": "HAYB",
            "Pełna nazwa producenta:": "HAYB Coffee Sp. z o.o. Al. Jerozolimskie 200 02-486 Warszawa"
        }
    )
    country = data_service._DataService__find_roaster_country(test_item)
    data_service._DataService__find_roaster_city(country, test_item)
    result = data_service._DataService__create_roaster(test_item)
    assert bool(result)


def test_get_coffee_name_producer_name(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="HAYB - Się Przelewa Kwiat 500g",
        tags=[],
        description="",
        details={
            "Producent:": "HAYB"
        }
    )

    result = data_service._DataService__get_coffee_name(test_item)
    expected = "Się Przelewa Kwiat 500g"
    assert result == expected


def test_get_coffee_name(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="HAYB - Się Przelewa Kwiat 500g",
        tags=[],
        description="",
        details={
            "Producent:": "Producent"
        }
    )

    result = data_service._DataService__get_coffee_name(test_item)
    expected = "HAYB - Się Przelewa Kwiat 500g"
    assert result == expected


def test_is_speciality_tags(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=["speciality"],
        description="",
        details={}
    )

    result = data_service._DataService__is_speciality(test_item)
    assert bool(result)


def test_is_speciality_description(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="speciality",
        details={}
    )

    result = data_service._DataService__is_speciality(test_item)
    assert bool(result)


def test_is_speciality_not_speciality(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={}
    )

    result = data_service._DataService__is_speciality(test_item)
    expected = False
    assert result == expected


def test_get_roasting_level(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Stopień palenia ziaren:": "Jasny"}
    )

    result = data_service._DataService__get_roasting_level(test_item)
    expected = 2
    assert result == expected


def test_get_roasting_level_no_level(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={}
    )

    result = data_service._DataService__get_roasting_level(test_item)
    expected = UNSET
    assert result == expected


def test_get_roasting_date_no_date(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={}
    )

    result = data_service._DataService__get_roasting_date(test_item)
    assert not bool(result)


def test_get_origin_two_origins(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Pochodzenie:": "kraj_1, kraj_2"}
    )

    result = data_service._DataService__get_origin(test_item)
    expected = ["kraj_1", "kraj_2"]
    assert result == expected


def test_get_beans_two_beans(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Arabica / Robusta:": "50/50"}
    )

    result = data_service._DataService__get_beans(test_item)
    assert len(result) == 2


def test_get_beans(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Arabica / Robusta:": "100% Arabica"}
    )

    result = data_service._DataService__get_beans(test_item)
    assert bool(result)


def test_get_processing_no_processing(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={}
    )

    result = data_service._DataService__get_processing(test_item)
    assert not bool(result)


@pytest.mark.skip(reason="There is no Anaerobic in processing yet")
def test_get_processing_new_processing(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Obróbka:": "Natural i Anaerobic"}
    )

    result = data_service._DataService__get_processing(test_item)
    expected = [Processing.NATURAL, Processing.ANAEROBIC]
    assert result == expected


def test_get_processing_two_processings(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Obróbka:": "Natural i Honey"}
    )

    result = data_service._DataService__get_processing(test_item)
    expected = [Processing.NATURAL, Processing.HONEY]
    assert result == expected


def test_get_dedication_two_dedications(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Przeznaczenie:": "Drip i espresso"}
    )

    result = data_service._DataService__get_dedication(test_item)
    expected = [BrewingMethod.DRIP, BrewingMethod.ESPRESSO]
    assert result == expected


def test_get_grammage_piece(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Opakowanie:": "16 sztuk"}
    )

    result = data_service._DataService__get_grammage(test_item)
    expected = [Grammage(16, UnitType.PIECE)]
    assert result == expected


def test_get_kind_capsules(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Rodzaj kawy:": "w kapsułkach"}
    )

    result = data_service._DataService__get_kind(test_item)
    expected = "capsules"
    assert result == expected


def test_get_kind_instant_1(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Rodzaj kawy:": "instant"}
    )

    result = data_service._DataService__get_kind(test_item)
    expected = "instant"
    assert result == expected


def test_get_kind_instant_2(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="",
        tags=[],
        description="",
        details={"Rodzaj kawy:": "rozpuszczalna"}
    )

    result = data_service._DataService__get_kind(test_item)
    expected = "instant"
    assert result == expected


def test_create_coffee_ok(mocker):
    mock_data_store = mocker.Mock()
    data_service = DataService(mock_data_store)

    test_item = Item(
        title="Bialetti - Milano - 16 Kapsułek",
        tags=["bialetti", "włoska", "kawa", "kapsułka"],
        description="Prawdziwa włoska kawa w kapsułkach.",
        details={
            "Ean:": "8001306965002",
            "Producent:": "Bialetti",
            "Opakowanie:": "16 sztuk",
            "Rodzaj kawy:": "W kapsułkach",
            "Arabica / Robusta:": "50/50",
            "Stopień palenia ziaren:": "Ciemny",
            "Przeznaczenie:": "Espresso",
            "Pełna nazwa producenta:": "Beyond The Bean Limited, Cala Trading Estate, Ashton Vale Road, Bristol, England / Anglia",
            "Wysyłka w ciągu:": "1 dzień roboczy"
        }
    )

    result = data_service._DataService__create_coffee(test_item)
    assert bool(result)
