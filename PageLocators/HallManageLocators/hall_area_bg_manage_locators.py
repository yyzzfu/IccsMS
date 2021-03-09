from selenium.webdriver.common.by import By


class HallAreaBgManageLocators:

    # 选择按钮，轴定位
    select_button = (By.XPATH, '//*[@id="photoImagePreview"]/following-sibling::a[@onclick="photoImageFinderOpen();"]')
    # 取消按钮
    cancel_button = (By.XPATH, '//*[@id="photoImagePreview"]/following-sibling::a[@onclick="photoImageDelAll();"]')
    # 备注输入框
    remarks = (By.XPATH, "//*[@id='remarks']")
    # 保存按钮
    submit = (By.XPATH, "//*[@id='btnSubmit']")
    # 上传按钮
    upload_button = (By.XPATH, "//*[@id='cke_9_label']")
    # 已上传的第一张图片定位元素
    the_first_image = (By.XPATH, '//*[@class="files_thumbnails fake no_list"]/a[1]/div')
    # the_first_image = (By.XPATH, '//*[@class="files_thumbnails fake no_list"]//h5[text()='modify(1).jpg']')  ------>之后进行优化，根据上传的图片名称进行定位
    # uploa_iframe定位元素
    upload_iframe = (By.XPATH, '//iframe[@allowtransparency="true"]')
