from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('设备管理')
@allure.story('场景设置')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestHallScene:

    add_datas = DoExcel('hall_scene_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('场景设置--新增功能')
    def test_add_hall_equipment(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_scence().add_hall_scene(
            hall_scene_name=data['hall_scene_name'],
            hall_scene_remarks=data['hall_scene_remarks'],
            add_type=data['add_type'],
            equipment=data['equipment'],
            execute_order=data['execute_order'],
            parameter=data['parameter'],
            action_execute_sequence=data['action_execute_sequence'],
            delay_execute_sequence=data['delay_execute_sequence'],
            delay_time=data['delay_time']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('hall_scene_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('场景设置--修改功能')
    def test_modify_hall_equipment(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_scence().modify_hall_scene(
            modify_hall_scene=data['modify_hall_scene'],
            hall_scene_name=data['hall_scene_name'],
            hall_scene_remarks=data['hall_scene_remarks'],
            add_type=data['add_type'],
            equipment=data['equipment'],
            execute_order=data['execute_order'],
            parameter=data['parameter'],
            action_execute_sequence=data['action_execute_sequence'],
            delay_execute_sequence=data['delay_execute_sequence'],
            delay_time=data['delay_time']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('disuse_or_use_hall_scene').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('场景设置--禁用功能')
    def test_disuse_hall_scene(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_scence().disuse_hall_scene(disuse_hall_scene=data['disuse_hall_scene'])
        assert '成功' in enter_the_homepage.get_success_save_tip()

    @pytest.mark.parametrize('data', datas)
    @allure.title('场景设置--启用功能')
    def test_use_hall_scene(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_scence().use_hall_scene(use_hall_scene=data['use_hall_scene'])
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('hall_scene_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('场景设置--删除功能')
    def test_delete_hall_equipment(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_scence().delete_hall_scene(delete_hall_scene=data['delete_hall_scene'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('场景设置--新增已删除的场景')
    def test_add_hall_equipment_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_scence().add_hall_scene(
            hall_scene_name=data['hall_scene_name'],
            hall_scene_remarks=data['hall_scene_remarks'],
            add_type=data['add_type'],
            equipment=data['equipment'],
            execute_order=data['execute_order'],
            parameter=data['parameter'],
            action_execute_sequence=data['action_execute_sequence'],
            delay_execute_sequence=data['delay_execute_sequence'],
            delay_time=data['delay_time']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()