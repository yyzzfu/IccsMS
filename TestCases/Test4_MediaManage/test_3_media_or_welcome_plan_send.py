from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('媒体管理')
@allure.story('媒体下发计划')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestMediaOrWelcomePlanSend:

    add_datas = DoExcel('plan_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('媒体下发计划--新增媒体下发计划')
    def test_add_plan(self, data, enter_the_homepage):
        enter_the_homepage.goto_media_or_welcome_paln_send().add_plan(
            add_type=data['add_type'],
            plan_name=data['plan_name'],
            sucai=data['sucai'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            equipment=data['equipment']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('plan_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('媒体下发计划--修改媒体下发计划')
    def test_modify_plan(self, data, enter_the_homepage):
        enter_the_homepage.goto_media_or_welcome_paln_send().modify_plan(
            plan_modify=data['plan_modify'],
            plan_name=data['plan_name'],
            sucai=data['sucai'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            equipment=data['equipment']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('plan_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('媒体下发计划--删除媒体下发计划')
    def test_delete_plan(self, data, enter_the_homepage):
        enter_the_homepage.goto_media_or_welcome_paln_send().delete_plan(plan_delete=data['plan_delete'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('媒体下发计划--新增已删除的媒体下发计划')
    def test_add_plan_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_media_or_welcome_paln_send().add_plan(
            add_type=data['add_type'],
            plan_name=data['plan_name'],
            sucai=data['sucai'],
            start_date=data['start_date'],
            end_date=data['end_date'],
            start_time=data['start_time'],
            end_time=data['end_time'],
            equipment=data['equipment']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()
