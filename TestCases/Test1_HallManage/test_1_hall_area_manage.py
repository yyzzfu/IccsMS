from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('营业厅管理')
@allure.story('区域管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestHallManage:
    add_datas = DoExcel('area_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('区域管理--新增功能')
    def test_add_hall_area(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_area_manage().add_hall_area(hall_area_name=data['hall_area_name'])
        assert '成功' in enter_the_homepage.get_success_save_tip()

    modify_datas = DoExcel('area_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', modify_datas)
    @allure.title('区域管理--修改功能')
    def test_modify_hall_area(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_area_manage().modify_hall_area(
            hall_area_modify=data['hall_area_modify'], hall_area_name=data['hall_area_name'])
        assert '成功' in enter_the_homepage.get_success_save_tip()

    delete_datas = DoExcel('area_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', delete_datas)
    @allure.title('区域管理--删除功能')
    def test_delete_hall_area(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_area_manage().delete_hall_area(hall_area_delete=data['hall_area_delete'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('区域管理--新增已删除的区域')
    def test_add_hall_area_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_area_manage().add_hall_area(hall_area_name=data['hall_area_name'])
        assert '成功' in enter_the_homepage.get_success_save_tip()
