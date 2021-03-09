from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@allure.feature('媒体管理')
@allure.story('欢迎词管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestWelcomeManage:

    add_datas = DoExcel('welcome_word_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('欢迎词管理--新增欢迎词')
    def test_add_welcome_word(self, data, enter_the_homepage):
        enter_the_homepage.goto_welcome_manage().add_welcome_word(
            welcome_template=data['welcome_template'],
            title=data['title'],
            content=data['content']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('welcome_word_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('欢迎词管理--修改欢迎词')
    def test_modify_welcome_word(self, data, enter_the_homepage):
        enter_the_homepage.goto_welcome_manage().modify_welcome_word(
            welcome_modify=data['welcome_modify'],
            welcome_template=data['welcome_template'],
            title=data['title'],
            content=data['content']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('welcome_word_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('欢迎词管理--删除欢迎词')
    def test_delete_welcome_word(self, data, enter_the_homepage):
        enter_the_homepage.goto_welcome_manage().delete_welcome_word(welcome_delete=data['welcome_delete'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)
    @allure.title('欢迎词管理--新增已删除的欢迎词')
    def test_add_welcome_word_delete(self, data, enter_the_homepage):
        enter_the_homepage.goto_welcome_manage().add_welcome_word(
            welcome_template=data['welcome_template'],
            title=data['title'],
            content=data['content']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()
