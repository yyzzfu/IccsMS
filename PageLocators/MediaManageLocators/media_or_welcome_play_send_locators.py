from selenium.webdriver.common.by import By


class MediaOrWelcomePlaySendLocators:

    # 添加按钮--视频下发计划/欢迎词下发计划
    video_or_welcome_plan_add_button = (By.XPATH, "//*[@id='searchForm']//a[text()='replace']")
    # 任务名称
    plan_name = (By.XPATH, "//*[@id='name']")
    # 多媒体任务素材关系表--新增按钮
    add_button = (By.XPATH, "//label[text()='多媒体任务素材关系表：']/following-sibling::div//table//a")
    # 素材下拉框
    sucai_select = (By.XPATH, "//select[contains(@id,'mediaId')]")
    # 开始日期
    start_date = (By.XPATH, "//*[@name='hallMediaPlanId.startDate']")
    # 结束日期
    end_date = (By.XPATH, "//*[@name='hallMediaPlanId.endDate']")
    # 播放计划时段表--新增按钮
    time_add_button = (By.XPATH, "//label [text()='播放计划时段表：']/following-sibling::div//table//a")
    # 开始时间
    start_time = (By.XPATH, "//*[@id='hallMediaPlanId_hallMediaTimeSlotList']//input[contains(@id,'startTime')]")
    # 结束时间
    end_time = (By.XPATH, "//*[@id='hallMediaPlanId_hallMediaTimeSlotList']//input[contains(@id,'endTime')]")
    # 终端
    equipment = (By.XPATH, "//label[text()='replace']")
    # 修改按钮
    modify_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='修改']")
    # 删除按钮
    delete_button = (By.XPATH, "//*[@id='contentTable']//a[contains(text(),'replace')]/../..//a[text()='删除']")
