from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.action_chains import ActionChains

options = webdriver.ChromeOptions()
# options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
options.add_experimental_option("prefs", {"profile.default_content_setting_values.notifications": 1})
options.add_argument('lnag=ko_KR')
# print('debug3')
driver = webdriver.Chrome('chromedriver', options=options)
actions = ActionChains(driver)

# 스크롤 내리기함수
def infinite_loop():

    last_page_height = driver.execute_script("return document.documentElement.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.documentElement.scrollHeight);")
        time.sleep(1.0)
        new_page_height = driver.execute_script("return document.documentElement.scrollHeight")
        if new_page_height == last_page_height:
            time.sleep(1.0)
            if new_page_height == driver.execute_script("return document.documentElement.scrollHeight"):
                break
        else:
            last_page_height = new_page_height


#-------------------------------------------------------------
# 원티드 로그인
# kakao login / 카카오로 로그인할 아이디와 비밀번호를 설정해주세요.
ID = ''
PW = ''
driver.get(
    'https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all')
time.sleep(1)
# driver.find_element('xpath', '//*[@id="__next"]/div[1]/div/nav/aside/ul/li[2]/button').click() # 윈도우 창 크기에 따라서 xpath 가 달라짐
driver.find_element('xpath', '//*[@id="__next"]/div[1]/div/nav/aside/ul/li[2]/button').click()
time.sleep(1)
driver.find_element('xpath', '//*[@id="MODAL_BODY"]/div[2]/div[2]/div[3]/div[1]/button').click()
time.sleep(1)
driver.find_element('name', 'email').send_keys(f'{ID}')
driver.find_element('name', 'password').send_keys(f'{PW}')
time.sleep(5)
driver.find_element('xpath', '//*[@id="login-form"]/fieldset/div[8]/button[1]').click()
time.sleep(2)
#-------------------------------------------------------------

df = pd.DataFrame()

category_list = []
page_url_list = []
picture_url_list = []
title_list = []
company_list = []
work_list = []
qualification_list = []
favor_list = []
welfare_list = []
skill_stack_list = []
place_list = []
money_list = []
number_list = []

for i in range(2, 6):
    df2 = pd.DataFrame()
    time.sleep(3)
    url = 'https://www.wanted.co.kr/wdlist/518?country=kr&job_sort=company.response_rate_order&years=-1&locations=all'
    driver.get(url)
    time.sleep(3)

    #세모클릭
    button1 = driver.find_element('xpath','//*[@id="__next"]/div[3]/article/div/div[2]/button/span[2]')
    driver.execute_script("arguments[0].click();", button1)

    time.sleep(1)

    # 직군선택
    driver.find_element('xpath',
                        '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[1]/div/button[{}]'.format(i)).click()
    # 직군명 크롤링
    category = driver.find_element('xpath', '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[1]/div/button[{}]'.format(i)).text
    time.sleep(0.3)

    # 선택완료 클릭
    button3 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/article/div/div[2]/section/div[2]/button')
    driver.execute_script("arguments[0].click();", button3)
    time.sleep(0.9)




    # 무한 스크롤 함수 호출 코드
    last_height = driver.execute_script('return document.body.scrollHeight')
    while True:
        # 끝까지 스크롤 다운
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        # 대기
        time.sleep(1.5)

        # 스크롤 다운 후 스크롤 높이 다시 가져옴
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height
    print('스크롤 완료')
    time.sleep(4)

    job_list = ['웹', '서버', '프론트엔드', '소프트웨어', '자바', '안드로이드', 'iOS', 'Nodejs', 'C++', '데이터엔지니어', 'DevOps', '파이썬', '시스템관리자', '머신러닝엔지니어',
                '데이터사이언티스트', '빅데이터엔지니어', 'QA', '기술지원', '개발매니저', '보안엔지니어', '프로덕트매니저', '블록체인엔지니어', 'PHP개발자', '임베디드개발자', '웹퍼블리셔',
                '크로스플랫폼', '하드웨어엔지니어', 'DBA', 'NET개발자', '영상음성엔지니어', 'CTO', '그래픽스엔지니어', 'VR엔지니어', 'BI', '엔지니어', 'ERP전문가', '루비온레일즈개발자',
                'CIO']
    # try:
    crawling_list = [1951,1956,1532,1504,1304,638,585,548,533,527,515,520,433,446,344,331,304,284,281,243,182,166,144,151,124,109,116,95,80,79,55,54,38,30,29,18,10]

    for j in range(1, crawling_list[i]+1):  # 2 , 12
        try:
            df = pd.DataFrame() #2
            # 공고문 클릭
            button5 = driver.find_element('css selector', '#__next > div.JobList_cn__t_THp > div > div > div.List_List_container__JnQMS > ul > li:nth-child({}) > div > a > header'.format(j))
            driver.execute_script("arguments[0].click();", button5)
            time.sleep(2)
            driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            # 공고문 url 크롤링
            page_url = driver.current_url
            print(page_url)

            # 회사명 클릭(연봉,직원수)
            button4 = driver.find_element('css selector', '#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div.JobContent_className___ca57 > section.JobHeader_className__HttDA > div:nth-child(2) > h6 > a')
            driver.execute_script("arguments[0].click();", button4)
            time.sleep(2)

            # 연봉, 직원수 화면까지

            driver.execute_script("window.scrollTo(0, 700);")

            time.sleep(5)

            # 연봉 크롤링
            try :
                money1 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[1]/div').get_attribute('style')
                money2 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[3]/div').get_attribute('style')
                money3 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[4]/div').get_attribute('style')
                money4 = driver.find_element('xpath', '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[1]/div/div[2]/div/div/div[5]/div').get_attribute('style')
                money = int( money1[7] + money2[7] + money3[7] + money4[7])
            except :
                money = '없음'
                pass
            print(money)

            # 직원 수 크롤링
            try:
                employee1 = driver.find_element('xpath',
                                                '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div').get_attribute(
                    'style')
                employee2 = driver.find_element('xpath',
                                                '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[2]/div').get_attribute(
                    'style')
                employee3 = driver.find_element('xpath',
                                                '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[3]/div').get_attribute(
                    'style')
                employee = int(employee1[7] + employee2[7] + employee3[7])
            except:
                try:
                    employee1 = driver.find_element('xpath',
                                                    '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[1]/div').get_attribute(
                        'style')
                    employee2 = driver.find_element('xpath',
                                                    '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div[2]/div').get_attribute(
                        'style')
                    employee = int(employee1[7] + employee2[7])
                except:
                    try:
                        employee1 = driver.find_element('xpath',
                                                        '//*[@id="__next"]/div[3]/div[2]/div[2]/div[3]/div/div[2]/div[1]/div/div/div/div').get_attribute(
                            'style')
                        employee = int(employee1[7])
                    except:
                        employee = '없음'
                        pass

            print(employee)
            driver.back()
            time.sleep(2)

            # 회사 이미지 크롤링
            try:
                picture_url = driver.find_element("css selector",
                                              '#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6 > div.JobDetail_relativeWrapper__F9DT5 > div > section.JobImage_JobImage__OFUyr > div > div:nth-child(1) > img').get_attribute(
                'src')
            except:
                picture_url = '없음'
            # 공고명 크롤링
            title = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/section[2]/h2').text
            print(title)
            # 회사명 크롤링
            company = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/section[2]/div[1]/h6/a').text
            print(company)

    #----------------------------------------------------------------------------------------------
            # 소제목 크롤링
            tag = ['주요업무', '자격요건', '우대사항', '혜택 및 복지', '기술스택 ・ 툴']
            tag_xpath = []
            for k in range(1, 6):
                try:
                    path = driver.find_element('xpath',
                                                 '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/h6[{}]'.format(
                                                     k)).text
                    tag_xpath.append(path)
                except:
                    pass
            print(tag_xpath)

    #-------------------------------------------------------------------------------------------------
            # 주소 크롤링





                # 회사 소개 text 위치
            try:
                Introduction = driver.find_element("xpath",
                                                   '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[1]/span').text
                print(Introduction)
            except:
                Introduction = '없음'
                pass
            # 주요 업무 text 위치
            try:
                work = driver.find_element("xpath",
                                           '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[2]/span').text
                print(work)
            except:
                work = '없음'
                pass
            # 자격 요건 text 위치
            time.sleep(0.2)
            try:
                qualification = driver.find_element("xpath",
                                                    '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[3]/span').text
                print(qualification)
            except:
                qualification = '없음'
                pass
            # 우대 사항 text 위치
            time.sleep(0.2)
            try:
                favor = driver.find_element("xpath",
                                            '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[4]/span').text
                print(favor)
            except:
                favor = '없음'
                pass
            # 혜택 및 복지 text 위치
            time.sleep(0.2)
            try:
                welfare = driver.find_element("xpath",
                                              '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[5]/span').text
                welfare_ = driver.find_element("xpath",
                                               '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/section[1]/p[5]/span')
                print(welfare)
            except:
                welfare = '없음'
                pass

            # 기술 스택 text 위치
            print('debug skill')
            try:
                try:
                    skill = driver.find_element('xpath',
                                                '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section[1]/p[6]/div').text
                    print(skill)

                except:
                    skill = '없음'
            except:
                skill = '없음'
                pass
            time.sleep(0.2)
            print('debug1')

            # 주소 크롤링
            time.sleep(1)
            try:
                button = driver.find_element("xpath", '//*[@id="__next"]/div[3]/div[1]/div[1]/div/div[2]/hr')
                desired_y = (button.size['height'] / 2) + button.location['y']
                current_y = (driver.execute_script('return window.innerHeight') / 2) + driver.execute_script(
                    'return window.pageYOffset')
                scroll_y_by = desired_y - current_y
                driver.execute_script("window.scrollBy(0, arguments[0]);", scroll_y_by)
                time.sleep(1)
                address = driver.find_element("xpath",
                                              '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section[2]/div[2]/span[2]').text
                print(address)
                time.sleep(1)
            except:
                address = '없음'
                pass
            time.sleep(0.2)
            print('debug1')





            category_list.append(category)
            page_url_list.append(page_url)
            picture_url_list.append(picture_url)
            title_list.append(title)
            company_list.append(company)
            work_list.append(work)
            qualification_list.append(qualification)
            favor_list.append(favor)
            welfare_list.append(welfare)
            skill_stack_list.append(skill)
            place_list.append(address)
            money_list.append(money)
            number_list.append(employee)
            time.sleep(0.2)
            driver.back()
            print('debug2')

            df = pd.DataFrame({'category': [category], 'page_url': [page_url], 'picture_url': [picture_url],
                               'title': [title], 'company': [company],
                               'work': [work], 'qualification': [qualification], 'favor': [favor],
                               'welfare': [welfare], 'skill_stack': [skill],
                               'place': [address], 'money': [money], 'employee': [employee]})
            print('debug3')
            df.to_csv('./rec_sys_model/wanted/crawling_{}_{}.csv'.format(i, j), index=False)
            print('save', i, j)
        except:
            print('error', job_list[i], j)
            driver.back()
            time.sleep(0.2)
            pass
    df2 = pd.DataFrame({'category': category_list, 'page_url': page_url_list, 'picture_url': picture_url_list,
                       'title': title_list, 'company': company_list,
                       'work': work_list, 'qualification': qualification_list, 'favor': favor_list,
                       'welfare': welfare_list, 'skill_stack': skill_stack_list,
                       'place': place_list, 'money': money_list, 'employee': number_list})
    df2.to_csv('./rec_sys_model/wanted/wanted_category/crawling_{}.csv'.format(job_list[i]), index=False)
    time.sleep(1)
    driver.back()

time.sleep(1)
