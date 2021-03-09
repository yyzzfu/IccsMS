from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('设备管理')
@allure.story('设备管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestHallEquipment:

    add_datas = DoExcel('hall_equipment_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('设备管理--新增功能')
    def test_add_hall_equipment(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_equipment().add_hall_equipment(
            hall_equipment_name=data['hall_equipment_name'],
            hall_equipment_type=data['hall_equipment_type'],
            hall_equipment_child_type=data['hall_equipment_child_type'],
            equipment_code=data['equipment_code'],
            mac_address=data['mac_address'],
            protocol_address=data['protocol_address'],
            area=data['area'],
            remarks=data['remarks'],
            equipment_gateway_parent=data['equipment_gateway_parent'],
            equipment_gateway_parent_port=data['equipment_gateway_parent_port'],
            equipment_gateway_protocol=data['equipment_gateway_protocol']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('hall_equipment_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('设备管理--修改功能')
    def test_modify_hall_equipment(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_equipment().modify_hall_equipment(
            modify_hall_equipment=data['modify_hall_equipment'],
            hall_equipment_name=data['hall_equipment_name'],
            hall_equipment_type=data['hall_equipment_type'],
            hall_equipment_child_type=data['hall_equipment_child_type'],
            equipment_code=data['equipment_code'],
            mac_address=data['mac_address'],
            protocol_address=data['protocol_address'],
            area=data['area'],
            remarks=data['remarks'],
            equipment_gateway_parent=data['equipment_gateway_parent'],
            equipment_gateway_parent_port=data['equipment_gateway_parent_port'],
            equipment_gateway_protocol=data['equipment_gateway_protocol']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('hall_equipment_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('设备管理--删除功能')
    def test_delete_hall_equipment(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_equipment().delete_hall_equipment(delete_hall_equipment=data['delete_hall_equipment'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('设备管理--新增已删除的设备')
    def test_add_hall_equipment_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_equipment().add_hall_equipment(
            hall_equipment_name=data['hall_equipment_name'],
            hall_equipment_type=data['hall_equipment_type'],
            hall_equipment_child_type=data['hall_equipment_child_type'],
            equipment_code=data['equipment_code'],
            mac_address=data['mac_address'],
            protocol_address=data['protocol_address'],
            area=data['area'],
            remarks=data['remarks'],
            equipment_gateway_parent=data['equipment_gateway_parent'],
            equipment_gateway_parent_port=data['equipment_gateway_parent_port'],
            equipment_gateway_protocol=data['equipment_gateway_protocol']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()