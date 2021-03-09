from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('媒体管理')
@allure.story('媒体素材管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestMediaOrTemplateManage:

    add_datas = DoExcel('sucai_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('媒体素材管理--新增素材')
    def test_add_sucai(self, data, enter_the_homepage):
        enter_the_homepage.goto_sucai_manage().add_sucai(
            sucai_name=data['sucai_name'],
            dirpath=data['dirpath'],
            sucai_type=data['sucai_type'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('sucai_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('媒体素材管理--修改素材')
    def test_modify_sucai(self, data, enter_the_homepage):
        enter_the_homepage.goto_sucai_manage().modify_sucai(
            sucai_modify=data['sucai_modify'],
            sucai_name=data['sucai_name'],
            dirpath=data['dirpath'],
            sucai_type=data['sucai_type'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('sucai_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('媒体素材管理--删除素材')
    def test_delete_sucai(self, data, enter_the_homepage):
        enter_the_homepage.goto_sucai_manage().delete_sucai(sucai_delete=data['sucai_delete'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('媒体素材管理--新增已删除的素材')
    def test_add_sucai_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_sucai_manage().add_sucai(
            sucai_name=data['sucai_name'],
            dirpath=data['dirpath'],
            sucai_type=data['sucai_type'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()


