import time

from Common import dir_path
from Common.do_excel import DoExcel
import pytest
import allure


@pytest.mark.skip(reason="普利人脸服务连接目前不可用")
@allure.epic('项目名称：中控平台V2.1')
@allure.feature('人脸识别')
@allure.story('人脸信息管理')
@pytest.mark.usefixtures('enter_the_homepage')
@pytest.mark.usefixtures('refresh')
class TestFaceRecognition:

    datas = DoExcel('face_info_add').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('人脸信息管理--访客新增功能')
    def test_add_face_info(self, data, enter_the_homepage):
        enter_the_homepage.goto_face_info_manage().add_face_info(
            add_type=data['add_type'],
            employee=data['employee'],
            name=data['name'],
            gender=data['gender'],
            telephone_number=data['telephone_number'],
            id_card_number=data['id_card_number'],
            company=data['company'],
            dirpath=data['dirpath'],
            smartwatch=data['smartwatch']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('face_info_modify').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('人脸信息管理--访客修改功能')
    def test_modify_face_info(self, data, enter_the_homepage):
        enter_the_homepage.goto_face_info_manage().modify_face_info(
            modify_face_info=data['modify_face_info'],
            add_type=data['add_type'],
            employee=data['employee'],
            name=data['name'],
            gender=data['gender'],
            telephone_number=data['telephone_number'],
            id_card_number=data['id_card_number'],
            company=data['company'],
            dirpath=data['dirpath'],
            smartwatch=data['smartwatch']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('set_customer_level').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('人脸信息管理--访客等级管理')
    def test_set_customer_level(self, data, enter_the_homepage):
        enter_the_homepage.goto_face_info_manage().set_customer_level(
            customer=data['customer'],
            level=data['level']
        )
        assert '成功' in enter_the_homepage.get_success_save_tip()

    datas = DoExcel('face_info_delete').get_data(dir_path.archives_data_excel_path)

    @pytest.mark.parametrize('data', datas)
    @allure.title('人脸信息管理--删除功能')
    def test_delete_face_info(self, data, enter_the_homepage):
        enter_the_homepage.goto_face_info_manage().delete_face_info(delete_face_info=data['delete_face_info'])
        time.sleep(0.5)
        enter_the_homepage.switch_iframe_to_new_tab()
        assert '成功' in enter_the_homepage.get_success_save_tip()



