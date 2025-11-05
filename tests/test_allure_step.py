import allure


@allure.step("Building")
def building_api():
    pass
@allure.step("Create")
def create_course():
    pass
@allure.step("Delete")
def delete_course():
    pass

def test_feature():
    building_api()
    create_course()
    delete_course()