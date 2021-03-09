from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@pytest.mark.skip(reason="普利人脸服务连接目前不可用")
@allure.epic('项目名称：中控平台V2.1')
@allure.feature('人脸识别')
@allure.story('终端管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestTerminalManage:

    datas = DoExcel('terminal_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('终端管理--新增摄像头')
    def test_add_teiminal(self, data, enter_the_homepage):
        enter_the_homepage.goto_terminal_manage().add_terminal(
            terminal_name=data['terminal_name'],
            terminal_type=data['terminal_type'],
            terminal_ip=data['terminal_ip'],
            terminal_port=data['terminal_port'],
            terminal_username=data['terminal_username'],
            terminal_password=data['terminal_password'],
            area=data['area'],
            push=data['push']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('terminal_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('终端管理--修改摄像头')
    def test_modify_teiminal(self, data, enter_the_homepage):
        enter_the_homepage.goto_terminal_manage().modify_terminal(
            terminal_modify=data['terminal_modify'],
            terminal_name=data['terminal_name'],
            terminal_type=data['terminal_type'],
            terminal_ip=data['terminal_ip'],
            terminal_port=data['terminal_port'],
            terminal_username=data['terminal_username'],
            terminal_password=data['terminal_password'],
            area=data['area'],
            push=data['push']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('terminal_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('终端管理--删除摄像头')
    def test_delete_teiminal(self, data, enter_the_homepage):
        enter_the_homepage.goto_terminal_manage().delete_terminal(terminal_delete=data['terminal_delete'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()



