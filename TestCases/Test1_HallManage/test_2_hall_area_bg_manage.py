from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('营业厅管理')
@allure.story('区域分布图管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestHallAreaBgManage:

    datas = DoExcel('hall_area_bg_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('区域分布图管理--新增功能')
    def test_add_hall_area_bg(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_area_bg_manage().add_hall_area_bg(
            dirpath=data['dirpath'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_hall_area_bg_success_save_tip()

    datas = DoExcel('hall_area_bg_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('区域分布图管理--修改功能')
    def test_modify_hall_area_bg(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_area_bg_manage().modify_hall_area_bg(
            dirpath=data['dirpath'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_hall_area_bg_success_save_tip()
