from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@allure.epic('项目名称：中控平台V2.1')
@pytest.mark.usefixtures('enter_the_homepage')   # 使用fixtures--》conftest中的enter_the_homepage
@pytest.mark.usefixtures('refresh')    # 使用fixtures--》conftest中的refresh
@allure.feature('设备管理')    # allure测试报告中的一级标题
@allure.story('网络通道管理')  # allure测试报告中的二级标题
class TestHallGateway:

    add_datas = DoExcel('hall_gateway_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', add_datas)  # 参数化
    @allure.title('网络通道管理--新增功能')
    def test_add_hall_gateway(self, data, enter_the_homepage):   # 传入enter_the_homepage，并使用其返回值，返回值为conftest--》enter_the_homepage中的homepage
        # 在网络通道新增界面，在各输入框中输入数据
        enter_the_homepage.goto_hall_gateway().add_hall_gateway(
            name=data['hall_gateway_name'],
            ip=data['hall_gateway_ip'],
            portAmount=data['hall_gateway_port_amount'],
            portStart=data['hall_gateway_port_start'],
            remarks=data['remarks']
        )
        # 断言--》界面中新增的网络通道名称是否与输入的名称一致，且‘保存网络通道成功’提示信息是否存在，两者都符合则用例通过，任意一个不符合则用例失败
        assert '成功' in enter_the_homepage.get_success_save_tip()

    modify_datas = DoExcel('hall_gateway_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', modify_datas)
    @allure.title('网络通道管理--修改功能')
    def test_modify_hall_gateway(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_gateway().modify_hall_gateway(
            modify_hall_gateway=data['modify_hall_gateway'],
            name=data['hall_gateway_name'],
            ip=data['hall_gateway_ip'],
            portAmount=data['hall_gateway_port_amount'],
            portStart=data['hall_gateway_port_start'],
            remarks=data['remarks']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    delete_datas = DoExcel('hall_gateway_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', delete_datas)
    @allure.title('网络通道管理--删除功能')
    def test_delete_hall_gateway(self, data, enter_the_homepage):
        enter_the_homepage.goto_hall_gateway().delete_hall_gateway(delete_hall_gateway=data['delete_hall_gateway'])
        assert '成功' in enter_the_homepage.get_success_delete_tip()

    @pytest.mark.parametrize('data', add_datas)  # 参数化
    @allure.title('网络通道管理--新增已删除的网络通道')
    def test_add_hall_gateway_delete(self, data, enter_the_homepage):  # 传入enter_the_homepage，并使用其返回值，返回值为conftest--》enter_the_homepage中的homepage
        # 在网络通道新增界面，在各输入框中输入数据
        enter_the_homepage.goto_hall_gateway().add_hall_gateway(
            name=data['hall_gateway_name'],
            ip=data['hall_gateway_ip'],
            portAmount=data['hall_gateway_port_amount'],
            portStart=data['hall_gateway_port_start'],
            remarks=data['remarks']
        )
        # 断言--》界面中新增的网络通道名称是否与输入的名称一致，且‘保存网络通道成功’提示信息是否存在，两者都符合则用例通过，任意一个不符合则用例失败
        assert '成功' in enter_the_homepage.get_success_save_tip()