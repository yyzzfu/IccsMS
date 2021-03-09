from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
@allure.feature('设备管理')
@allure.story('测控管理')
class TestHallControl:

    add_datas = DoExcel('hall_control_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('测控管理--新增功能')
    def test_add_hall_control(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_control().add_hall_control(
            hall_gateway=data['hall_gateway'],
            hall_gateway_port=data['hall_gateway_port'],
            hall_control_name=data['hall_control_name'],
            hall_control_amount=data['hall_control_amount'],
            hall_control_start_address=data['hall_control_start_address'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    delete_datas = DoExcel('hall_control_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', delete_datas)
    @allure.title('测控管理--修改功能')
    def test_modify_hall_control(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_control().modify_hall_control(
            modify_hall_control=data['modify_hall_control'],
            hall_gateway=data['hall_gateway'],
            hall_gateway_port=data['hall_gateway_port'],
            hall_control_name=data['hall_control_name'],
            hall_control_amount=data['hall_control_amount'],
            hall_control_start_address=data['hall_control_start_address'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    delete_datas = DoExcel('hall_control_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', delete_datas)
    @allure.title('测控管理--删除功能')
    def test_delete_hall_control(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_control().delete_hall_control(delete_hall_control=data['delete_hall_control'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('测控管理--新增已删除的测控')
    def test_add_hall_control_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_control().add_hall_control(
            hall_gateway=data['hall_gateway'],
            hall_gateway_port=data['hall_gateway_port'],
            hall_control_name=data['hall_control_name'],
            hall_control_amount=data['hall_control_amount'],
            hall_control_start_address=data['hall_control_start_address'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()
