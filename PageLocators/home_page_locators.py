from selenium.webdriver.common.by import By


class HomePageLocator:

    # -----------------------------------------共用的定位元素--------------------------------------------------------
    # 退出按钮
    logout_ele = (By.XPATH, '//*[@id="userControl"]//a[@title="退出登录"]')
    # 在首页已默认打开的‘网络通道管理’的tab中的X定位
    tab_close = (By.XPATH, "//*[@id='jerichotab']//a[@title='关闭']")
    # 新增按钮
    add_button = (By.XPATH, '//*[@id="searchForm"]//*[text()="新增" and @class="btn btn-primary"] ')
    # iframe，使用xpath定位，因为元素中iframe的id和name都是变动的
    iframe = (By.XPATH, '//div[@id="jerichotab_contentholder"]//iframe')
    # 所有页面的保存按钮
    submit = (By.XPATH, '//*[@id="btnSubmit"]')
    # 保存成功提示信息
    # success_save_tip = (By.XPATH, '//*[@id="searchForm"]/following-sibling::div[@id="messageBox"]')
    success_save_tip = (By.XPATH, '//div[@id="messageBox"]')
    # 区域分布图保存成功提示信息
    hall_area_bg_success_save_tip = (By.XPATH, '//*[@id="inputForm"]/child::div[@id="messageBox"]')
    # 列表中第一个删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']/tbody/tr[1]//a[2]")
    # 列表中最后一个删除按钮
    last_delete_button = (By.XPATH, ".//*[@id='contentTable']/tbody/tr[last()]/td[last()]/a[last()]")
    # 弹出框中确定按钮
    alert_accept_button = (By.XPATH, '//*[@id="jbox-state-state0"]//button[text()="确定"]')
    # 列表中第一个名称定位元素
    list_first_name_text = (By.XPATH, '//*[@id="contentTable"]/child::tbody/tr[1]//td[1]//a[1]')
    # 列表中最后一个名称定位元素
    list_last_name_text = (By.XPATH, './/*[@id="contentTable"]/tbody/tr[last()]/td[1]/a')
    # 上传按钮
    upload_button = (By.XPATH, "//*[@id='cke_9_label']")
    # 已上传的第一张图片定位元素
    the_first_image = (By.XPATH, '//*[@class="files_thumbnails fake no_list"]/a[1]/div')
    # the_first_image = (By.XPATH, '//*[@class="files_thumbnails fake no_list"]//h5[text()='modify(1).jpg']')  ------>之后进行优化，根据上传的图片名称进行定位
    # uploa_iframe定位元素
    upload_iframe = (By.XPATH, '//iframe[@allowtransparency="true"]')

# ---------------------------------------设备管理----------------------------------------------------------------------------
    # 设备管理
    hall_equipment = (By.XPATH, '//ul[@id="menu"]//*[text()="设备管理" and @class="dropdown-toggle menuLevel1"]')
    # 网络通道管理
    hall_gateway = (By.XPATH, '//*[@id="menu"]//span[text()="网络通道管理"]')
    # 测控管理按钮
    hall_control = (By.XPATH, '//*[@id="menu"]//span[text()="测控管理"]')
    # 设备管理二级菜单
    hall_equipment_2 = (By.XPATH, '//ul[@id="menu"]//*[@menu-path=">>设备管理>>设备管理"]//*[text()="设备管理"]')
    # 场景设置
    hall_scene = (By.XPATH, '//*[@id="menu"]//span[text()="场景设置"]')

    # --------------------------------------营业厅管理-----------------------------------------------------------------------------
    # 营业厅管理
    hall_manage = (By.XPATH, '//*[@id="menu"]//*[text()="营业厅管理"]')
    # 区域管理
    hall_area_manage = (By.XPATH, '//*[@id="menu"]//*[text()="区域管理"]')
    # 区域分布图管理
    hall_area_bg_manage = (By.XPATH, '//*[@id="menu"]//*[text()="区域分布图管理"]')

# --------------------------------------------系统管理-----------------------------------------------------------------------
    # 系统管理
    system_manage = (By.XPATH, '//*[@id="menu"]//*[text()="系统管理"]')
    # 协议管理
    hall_protocol = (By.XPATH, '//*[@id="menu"]//*[@menu-path=">>系统管理>>协议管理>>协议管理"]//*[text()="协议管理"]')

# ------------------------------------------人脸识别-------------------------------------------------------------------------
    # 人脸识别一级菜单
    face_recognition = (By.XPATH, '//*[@id="menu"]//*[text()="人脸识别"]')
    # 人脸信息管理
    face_info_manage = (By.XPATH, '//*[@id="menu"]//*[text()="人脸信息管理"]')
    # 终端管理
    terminal_manage = (By.XPATH, '//*[@id="menu"]//*[text()="终端管理"]')

# -------------------------------------------媒体管理------------------------------------------------------------------------
    # 媒体管理
    media_manage = (By.XPATH, '//*[@id="menu"]//*[text()="媒体管理"]')
    # 媒体素材管理
    media_or_template_manage = (By.XPATH, '//*[@id="menu"]//*[text()="媒体素材管理"]')
    # 媒体下发计划
    media_or_welcome_play_send = (By.XPATH, '//*[@id="menu"]//*[text()="媒体下发计划"]')
    # 欢迎词管理
    welcome_manage = (By.XPATH, '//*[@id="menu"]//*[text()="欢迎词管理"]')

# -----------------------------------------------------------------------------------------------------------------------
    # 页面底部“下一页”按钮
    next_page_button = (By.XPATH, "//*[@class='pagination']//a[contains(text(),'下一页 ')]")