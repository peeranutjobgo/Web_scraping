import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# from selenium.common.exceptions import NoSuchElementException
from webdriver_manager.chrome import ChromeDriverManager
# import openpyxl 
import time

# ฟังก์ชันเพื่อแปลงเลขไทยเป็นเลขอาราบิก
def thai_to_arabic_numbers(thai_num):
    thai_arabic_dict = {
        '๐': '0',
        '๑': '1',
        '๒': '2',
        '๓': '3',
        '๔': '4',
        '๕': '5',
        '๖': '6',
        '๗': '7',
        '๘': '8',
        '๙': '9'
    }
    return ''.join(thai_arabic_dict.get(ch, ch) for ch in thai_num)

def extract_total_pages(page_text):
    try:
        # สมมติว่ารูปแบบข้อความเป็น "หน้า x จาก y"
        current_page, total_pages = page_text.split('จาก')
        # แปลงเป็นเลขอาราบิกหากเป็นเลขไทย
        total_pages_arabic = thai_to_arabic_numbers(total_pages.strip())
        return int(total_pages_arabic)
    except (ValueError, IndexError) as e:
        print(f"Error parsing total pages from text: {e}")
        return None

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
url = "https://dictionary.orst.go.th/lookup_domain.php"
driver.get(url)

# wait = WebDriverWait(driver, 60)
# word_data = pd.DataFrame(columns=["หมวดอักษร", "คำ", "ความหมาย"])

# # word_count =  pd.DataFrame(columns=["หมวดอักษร", "หน้าทั้งหมด", "หน้าสุดท้ายที่ต้องการดึง"])
# # thai_alphabet = ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ', 'ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
# alphabet_buttons_1 =  ['ก', 'ข', 'ฃ', 'ค', 'ฅ', 'ฆ', 'ง', 'จ', 'ฉ', 'ช', 'ซ', 'ฌ', 'ญ', 'ฎ', 'ฏ', 'ฐ', 'ฑ', 'ฒ', 'ณ', 'ด', 'ต', 'ถ']
# print(alphabet_buttons_1)

# for alphabet in alphabet_buttons_1:
#     last_page = last_page_intext = 0
#     button_xpath = f"//button[@onclick=\"getwordlist('{alphabet}')\"]"
#     wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()
#     print(f"Processing alphabet: {alphabet}")
#     # ------------------------------------------------------------------------------------------------ 
#     # รับจำนวนหน้าทั้งหมดสำหรับหมวดอักษรนี้
#     pages_xpath = "//span[@id='spnPage']"
#     pages_text = wait.until(EC.presence_of_element_located((By.XPATH, pages_xpath))).text
#     # print(pages_text)
#     last_page_intext = extract_total_pages(pages_text)
#     print(f"หน้าสุดท้ายในหมวดอักษรนี้ : {last_page_intext}")
#     # ------------------------------------------------------------------------------------------------ 
#     # ถ้าจำนวนหน้าน้อยกว่า 10 ให้ตั้งค่าให้ตามจำนวนหน้าที่มีจริง
#     last_page = min(last_page_intext, 10)
#     print(last_page)
#     print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
#     # new_row_word_count = pd.DataFrame({"หมวดอักษร": [alphabet], "หน้าทั้งหมด": [last_page_intext], "หน้าสุดท้ายที่ต้องการดึง": [last_page]})
#     # word_count = pd.concat([word_count, new_row_word_count], ignore_index=True)
#     time.sleep(5)
#     # ------------------------------------------------------------------------------------------------ 
    
#     last_page += 1
#     for page in range(1, last_page):  # วน loop จนถึงหน้าที่ 10
#         # if page == last_page : break
#         print(f"Processing page: {page}")
#         print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
#         word_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(@class,'list-group-item') and contains(@onclick,'lookupWord')]")))
        
#         for index in range(len(word_elements)):
#             word_elements = wait.until(EC.presence_of_all_elements_located(
#             (By.XPATH, "//button[contains(@class,'list-group-item') and contains(@onclick,'lookupWord')]")))
#             if index < len(word_elements):
#                 # word_button = word_elements[index]
#         # for index in range(len(word_elements)):
#         #     word_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class,'list-group-item') and contains(@onclick,'lookupWord')]")))
#                 word_button = word_elements[index]
#                 word = word_button.text
#                 print(f"this word : {word}")
#                 word_button.click()
#                 time.sleep(5)
#                 print("------------------------------------------------------------------------------------")
#                 meaning_xpath = '//*[@id="r_lookup"]/div/div[2]'
#                 meaning = wait.until(EC.presence_of_element_located((By.XPATH, meaning_xpath))).text
#                 print(f"this word meaning : {meaning}")
#                 print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
#                 new_row = pd.DataFrame({"หมวดอักษร": [alphabet], "คำ": [word], "ความหมาย": [meaning]})
#                 word_data = pd.concat([word_data, new_row], ignore_index=True)
#                 time.sleep(5)
#                 # time.sleep()

#         # บันทึกข้อมูลลงไฟล์
#         word_data.to_csv("word_data.csv", index=False, encoding='utf-8-sig')
#         word_data.to_json("word_data.json", orient='records', force_ascii=False)
        
#         print(f"Processing page: {page} in {last_page - 1}")
#         # if page == last_page + 1 : break
        
#         if page < last_page:
#             next_page_button = wait.until(EC.element_to_be_clickable((By.ID, "nextpage")))
#             next_page_button.click()
#             time.sleep(5)


wait = WebDriverWait(driver, 30)
word_data = pd.DataFrame(columns=["หมวดอักษร", "คำ", "ความหมาย"])

# print(f"Processing is susussfull in set one,go to set two") 
# print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
# alphabet_buttons_2 = ['ท', 'ธ', 'น', 'บ', 'ป', 'ผ', 'ฝ', 'พ', 'ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
alphabet_buttons_2 = ['ฟ', 'ภ', 'ม', 'ย', 'ร', 'ฤ', 'ล', 'ฦ', 'ว', 'ศ', 'ษ', 'ส', 'ห', 'ฬ', 'อ', 'ฮ']
print(alphabet_buttons_2)

for alphabet in alphabet_buttons_2:
    last_page = last_page_intext = 0
    button_xpath = f"//button[@onclick=\"getwordlist('{alphabet}')\"]"
    wait.until(EC.element_to_be_clickable((By.XPATH, button_xpath))).click()
    print(f"Processing alphabet: {alphabet}")
    # ------------------------------------------------------------------------------------------------ 
    # รับจำนวนหน้าทั้งหมดสำหรับหมวดอักษรนี้
    pages_xpath = "//span[@id='spnPage']"
    pages_text = wait.until(EC.presence_of_element_located((By.XPATH, pages_xpath))).text
    # print(pages_text)
    last_page_intext = extract_total_pages(pages_text)
    print(f"หน้าสุดท้ายในหมวดอักษรนี้ : {last_page_intext}")
    # ------------------------------------------------------------------------------------------------ 
    # ถ้าจำนวนหน้าน้อยกว่า 10 ให้ตั้งค่าให้ตามจำนวนหน้าที่มีจริง
    last_page = min(last_page_intext, 10)
    print(last_page)
    print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
    # new_row_word_count = pd.DataFrame({"หมวดอักษร": [alphabet], "หน้าทั้งหมด": [last_page_intext], "หน้าสุดท้ายที่ต้องการดึง": [last_page]})
    # word_count = pd.concat([word_count, new_row_word_count], ignore_index=True)
    time.sleep(5)
    # ------------------------------------------------------------------------------------------------ 
    
    last_page += 1
    for page in range(1, last_page):  # วน loop จนถึงหน้าที่ 10
        # if page == last_page : break
        print(f"Processing page: {page}")
        print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
        word_elements = wait.until(EC.visibility_of_all_elements_located((By.XPATH, "//button[contains(@class,'list-group-item') and contains(@onclick,'lookupWord')]")))
        
        for index in range(len(word_elements)):
            word_elements = wait.until(EC.presence_of_all_elements_located(
            (By.XPATH, "//button[contains(@class,'list-group-item') and contains(@onclick,'lookupWord')]")))
            if index < len(word_elements):
                # word_button = word_elements[index]
        # for index in range(len(word_elements)):
        #     word_elements = wait.until(EC.presence_of_all_elements_located((By.XPATH, "//button[contains(@class,'list-group-item') and contains(@onclick,'lookupWord')]")))
                word_button = word_elements[index]
                word = word_button.text
                print(f"this word : {word}")
                word_button.click()
                time.sleep(3)
                print("------------------------------------------------------------------------------------")
                meaning_xpath = '//*[@id="r_lookup"]/div/div[2]'
                meaning = wait.until(EC.presence_of_element_located((By.XPATH, meaning_xpath))).text
                print(f"this word meaning : {meaning}")
                print("---------------------------------------------------------------------------------------------------------------------------------------------------------")
                new_row = pd.DataFrame({"หมวดอักษร": [alphabet], "คำ": [word], "ความหมาย": [meaning]})
                word_data = pd.concat([word_data, new_row], ignore_index=True)
                time.sleep(5)
                # time.sleep()

        # บันทึกข้อมูลลงไฟล์
        word_data.to_csv("word_data_2.csv", index=False, encoding='utf-8-sig')
        word_data.to_json("word_data_2.json", orient='records', force_ascii=False)
        
        print(f"Processing page: {page} in {last_page - 1}")
        # if page == last_page + 1 : break
        
        if page < last_page:
            next_page_button = wait.until(EC.element_to_be_clickable((By.ID, "nextpage")))
            next_page_button.click()
            time.sleep(2)


driver.quit()

# # บันทึกข้อมูลลงไฟล์
# word_data.to_csv("word_data_test.csv", index=False, encoding='utf-8-sig')
# word_data.to_json("word_data_test.json", orient='records', force_ascii=False)
# word_count.to_csv("word_count.csv", index=False, encoding='utf-8-sig')
# excel_path = "C:\Users\LeCe380\Documents\Web scraping\v.2"  # ที่ตั้งไฟล์ที่จะบันทึก
# word_data.to_excel(excel_path, index=False, engine='openpyxl')




