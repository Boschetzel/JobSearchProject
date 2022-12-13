from selenium import webdriver
from selenium.webdriver.common.by import By
from PyQt5 import QtCore, QtGui, QtWidgets
import time
import os
import pandas as pd


class GetElements:
    def __init__(self):
        super().__init__()
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.job_title_lst = []
        self.company_list = []
        self.link_list = []
        self.date_list = []
        self.job_location = []
        self.driver.implicitly_wait(10)


class GuiSearchWindow(GetElements):
    def __init__(self):
        super().__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1128, 603)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.job_title_lbl = QtWidgets.QLabel(self.centralwidget)
        self.job_title_lbl.setGeometry(QtCore.QRect(80, 100, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.job_title_lbl.setFont(font)
        self.job_title_lbl.setObjectName("job_title_lbl")
        self.ui_job_title = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_job_title.setGeometry(QtCore.QRect(160, 100, 171, 22))
        self.ui_job_title.setObjectName("ui_job_title")

        self.entry_level_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.entry_level_chk_box.setGeometry(QtCore.QRect(160, 200, 81, 20))
        self.entry_level_chk_box.setObjectName("entry_level_chk_box")

        self.position_lbl = QtWidgets.QLabel(self.centralwidget)
        self.position_lbl.setGeometry(QtCore.QRect(80, 170, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.position_lbl.setFont(font)
        self.position_lbl.setObjectName("position_lbl")

        self.internship_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.internship_chk_box.setGeometry(QtCore.QRect(160, 170, 81, 20))
        self.internship_chk_box.setObjectName("internship_chk_box")

        self.associate_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.associate_chk_box.setGeometry(QtCore.QRect(160, 230, 81, 20))
        self.associate_chk_box.setObjectName("associate_chk_box")

        self.mid_sr_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.mid_sr_chk_box.setGeometry(QtCore.QRect(160, 260, 121, 20))
        self.mid_sr_chk_box.setObjectName("mid_sr_chk_box")

        self.director_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.director_chk_box.setGeometry(QtCore.QRect(160, 290, 81, 20))
        self.director_chk_box.setObjectName("director_chk_box")

        self.location_lbl = QtWidgets.QLabel(self.centralwidget)
        self.location_lbl.setGeometry(QtCore.QRect(310, 170, 55, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.location_lbl.setFont(font)
        self.location_lbl.setObjectName("location_lbl")

        self.on_site_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.on_site_chk_box.setGeometry(QtCore.QRect(390, 210, 81, 20))
        self.on_site_chk_box.setObjectName("on_site_chk_box")

        self.ui_location = QtWidgets.QLineEdit(self.centralwidget)
        self.ui_location.setGeometry(QtCore.QRect(390, 170, 113, 22))
        self.ui_location.setObjectName("ui_location")

        self.remote_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.remote_chk_box.setGeometry(QtCore.QRect(390, 240, 81, 20))
        self.remote_chk_box.setObjectName("remote_chk_box")

        self.hybrid_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.hybrid_chk_box.setGeometry(QtCore.QRect(390, 270, 81, 20))
        self.hybrid_chk_box.setObjectName("hybrid_chk_box")

        self.date_posted_lbl = QtWidgets.QLabel(self.centralwidget)
        self.date_posted_lbl.setGeometry(QtCore.QRect(530, 170, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.date_posted_lbl.setFont(font)
        self.date_posted_lbl.setObjectName("date_posted_lbl")

        self.any_time_chk_box = QtWidgets.QRadioButton(self.centralwidget)
        self.any_time_chk_box.setGeometry(QtCore.QRect(530, 200, 81, 20))
        self.any_time_chk_box.setObjectName("any_time_chk_box")

        self.past_week_chk_box = QtWidgets.QRadioButton(self.centralwidget)
        self.past_week_chk_box.setGeometry(QtCore.QRect(530, 230, 81, 20))
        self.past_week_chk_box.setObjectName("past_week_chk_box")

        self.past_24h_chk_boxx = QtWidgets.QRadioButton(self.centralwidget)
        self.past_24h_chk_boxx.setGeometry(QtCore.QRect(530, 260, 81, 20))
        self.past_24h_chk_boxx.setObjectName("past_24h_chk_boxx")

        self.past_month_chk_box = QtWidgets.QRadioButton(self.centralwidget)
        self.past_month_chk_box.setGeometry(QtCore.QRect(530, 290, 91, 20))
        self.past_month_chk_box.setObjectName("past_month_chk_box")

        self.job_type_lbl = QtWidgets.QLabel(self.centralwidget)
        self.job_type_lbl.setGeometry(QtCore.QRect(660, 170, 71, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.job_type_lbl.setFont(font)
        self.job_type_lbl.setObjectName("job_type_lbl")

        self.full_time_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.full_time_chk_box.setGeometry(QtCore.QRect(740, 170, 91, 20))
        self.full_time_chk_box.setObjectName("full_time_chk_box")

        self.contract_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.contract_chk_box.setGeometry(QtCore.QRect(740, 200, 91, 20))
        self.contract_chk_box.setObjectName("contract_chk_box")

        self.internship_chk_box_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.internship_chk_box_2.setGeometry(QtCore.QRect(740, 230, 91, 20))
        self.internship_chk_box_2.setObjectName("internship_chk_box_2")

        self.search_box_btn = QtWidgets.QPushButton(self.centralwidget)
        self.search_box_btn.setGeometry(QtCore.QRect(160, 420, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.search_box_btn.setFont(font)
        self.search_box_btn.setObjectName("search_box_btn")

        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(370, 10, 491, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")

        self.other_chk_box = QtWidgets.QCheckBox(self.centralwidget)
        self.other_chk_box.setGeometry(QtCore.QRect(740, 260, 91, 20))
        self.other_chk_box.setObjectName("other_chk_box")

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1128, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.search_box_btn.clicked.connect(self.start_search)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.job_title_lbl.setText(_translate("MainWindow", "Job Title"))
        self.entry_level_chk_box.setText(_translate("MainWindow", "Entry level"))
        self.position_lbl.setText(_translate("MainWindow", "Position"))
        self.internship_chk_box.setText(_translate("MainWindow", "Internship"))
        self.associate_chk_box.setText(_translate("MainWindow", "Associate"))
        self.mid_sr_chk_box.setText(_translate("MainWindow", "Mid-Senior level"))
        self.director_chk_box.setText(_translate("MainWindow", "Director"))
        self.location_lbl.setText(_translate("MainWindow", "Location"))
        self.on_site_chk_box.setText(_translate("MainWindow", "On-Site"))
        self.remote_chk_box.setText(_translate("MainWindow", "Remote"))
        self.hybrid_chk_box.setText(_translate("MainWindow", "Hybrid"))
        self.date_posted_lbl.setText(_translate("MainWindow", "Date posted"))
        self.any_time_chk_box.setText(_translate("MainWindow", "Any time"))
        self.past_week_chk_box.setText(_translate("MainWindow", "Past week"))
        self.past_24h_chk_boxx.setText(_translate("MainWindow", "Past 24 h"))
        self.past_month_chk_box.setText(_translate("MainWindow", "Past month"))
        self.job_type_lbl.setText(_translate("MainWindow", "Job type"))
        self.full_time_chk_box.setText(_translate("MainWindow", "Full time"))
        self.contract_chk_box.setText(_translate("MainWindow", "Contract"))
        self.internship_chk_box_2.setText(_translate("MainWindow", "Internship"))
        self.search_box_btn.setText(_translate("MainWindow", "Search"))
        self.label_6.setText(_translate("MainWindow", "Job search application for LinkedIn "))
        self.other_chk_box.setText(_translate("MainWindow", "Other"))

    def start_search(self):
        job_title = self.ui_job_title.text()
        location = self.ui_location.text()

        # Job Title and Location url
        self.driver.get(f"https://www.linkedin.com/jobs/search?keywords={job_title}&location={location}"
                        f"&geoId=&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0")

        print("Reached here")
        self.select_date_jobs_posted()
        print("1")
        self.select_job_type()
        print("2")
        self.select_experience_level()
        print("3")
        self.select_job_location()
        print("4")
        self.get_total_search_results()
        print("5")
        self.auto_scroll_page()
        print("6")
        self.get_results()

        print("7")
        self.make_dataframe()
        print("8")
        self.save_csv_file()
        print("9")
        self.driver.close()
        print("Done")
        MainWindow.close()

    def click_done_btn_date_posted(self):
        self.driver.find_element(By.XPATH,
                                 "//button[@class='filter__submit-button' and @data-tracking-control-name="
                                 "'public_jobs_f_TPR']").click()

    """Method to select the timeframe when the job was posted. 
       User have 4 choices [Last 24 h, Past Week, Past Month, Any Time] """

    def select_date_jobs_posted(self):
        # Select the "Any Time" btn and click it
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Any Time')]").click()
        time.sleep(2)

        # Select the elements from the "Date-Posted" checkbox
        self.driver.find_elements(By.CLASS_NAME, "filter-values-container__filter-value")
        time.sleep(2)

        # Select "Any Time" RadioBtn
        if self.any_time_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_TPR-3").click()
            time.sleep(2)

            # Click the "Done" btn
            self.click_done_btn_date_posted()

            # Select "Past-Week" RadioBtn
        if self.past_week_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_TPR-1").click()
            time.sleep(2)

            # Click the "Done" btn
            self.click_done_btn_date_posted()

        # Select "Past-24h" RadioBtn
        if self.past_24h_chk_boxx.isChecked():
            self.driver.find_element(By.ID, "f_TPR-0").click()
            time.sleep(2)

            # Click the "Done" btn
            self.click_done_btn_date_posted()

        # Select "Past-Month" RadioBtn
        if self.past_month_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_TPR-2").click()
            time.sleep(2)

            # Click the "Done" btn
            self.click_done_btn_date_posted()

    def click_done_btn_job_type(self):
        self.driver.find_element(By.XPATH, "//button[@class='filter__submit-button' and @data-tracking-control-name="
                                           "'public_jobs_f_JT']").click()

    """Method to select the job type.
       User have the following options: [Full-Time, Contract, Internship, Other]"""

    def select_job_type(self):
        # Select "Job-Type" btn and click it
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Job Type')]").click()
        time.sleep(2)

        # Select the elements from the "Job-Type" checkbox
        self.driver.find_elements(By.CLASS_NAME, "filter-values-container__filter-value")
        time.sleep(2)

        # Select "Full-Time" checkbox
        if self.full_time_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_JT-0").click()
            time.sleep(2)
        else:
            pass

        # Select "Contract" checkbox
        if self.contract_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_JT-1").click()
            time.sleep(2)
        else:
            pass

        # Select "Internship" checkbox
        if self.internship_chk_box_2.isChecked():
            self.driver.find_element(By.ID, "f_JT-3").click()
            time.sleep(2)
        else:
            pass

        # Select "Other" checkbox
        if self.other_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_JT-4").click()
            time.sleep(2)
        else:
            pass

        # Click the "Done" btn
        self.click_done_btn_job_type()

    def click_done_btn_experience_level(self):
        # Click "Done" button
        self.driver.find_element(By.XPATH, "//button[@class='filter__submit-button' and @data-tracking-control-name="
                                           "'public_jobs_f_E']").click()

    """Method to select the experience level.
       User have 4 choices : [Internship, Entry-Level, Associate, Mid-Senior, Director]"""

    def select_experience_level(self):
        # Select "Experience Level" btn and click it
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Experience Level')]").click()
        time.sleep(2)

        # Select the elements from the "Experience Level" checkbox
        self.driver.find_elements(By.CLASS_NAME, "filter-values-container__filter-value")
        time.sleep(2)

        # Select "Internship" checkbox
        if self.internship_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_E-0").click()
            time.sleep(2)
        else:
            pass

        # Select  "Entry-Level" checkbox
        if self.entry_level_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_E-1").click()
            time.sleep(2)
        else:
            pass

        # Select  "Associate" checkbox
        if self.associate_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_E-2").click()
            time.sleep(2)
        else:
            pass

        # Select  "Mid-Senior Level" checkbox
        if self.mid_sr_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_E-3").click()
            time.sleep(2)
        else:
            pass

        # Select  "Director" checkbox
        if self.director_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_E-3").click()
            time.sleep(2)
        else:
            pass

        self.click_done_btn_experience_level()

    def click_done_btn_job_location(self):
        # Click "Done" button
        self.driver.find_element(By.XPATH, "//button[@class='filter__submit-button' and @data-tracking-control-name="
                                           "'public_jobs_f_WT']").click()
        time.sleep(2)

    def select_job_location(self):
        # Select "On-Site/Remote" btn and click it
        self.driver.find_element(By.XPATH, "//button[contains(text(),'On-site/Remote')]").click()
        time.sleep(2)

        # Select the elements from the "On-Site/Remote" checkbox
        self.driver.find_elements(By.CLASS_NAME, "filter-values-container__filter-value")
        time.sleep(2)

        # Select  "Remote"  checkbox
        if self.remote_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_WT-0").click()
            time.sleep(2)
        else:
            pass

        # Select  "On-site" checkbox
        if self.on_site_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_WT-1").click()
            time.sleep(2)
        else:
            pass

        # Select  "Hybrid" checkbox
        if self.hybrid_chk_box.isChecked():
            self.driver.find_element(By.ID, "f_WT-3").click()
            time.sleep(2)
        else:
            pass

        self.click_done_btn_job_location()

    def get_total_search_results(self):
        jobs_num = self.driver.find_element(By.CSS_SELECTOR, "h1>span").get_attribute("innerText")
        if len(jobs_num.split(',')) > 1:
            jobs_num = int(jobs_num.split(',')[0]) * 1000
        else:
            jobs_num = int(jobs_num)

        jobs_num = int(jobs_num)
        return jobs_num

    def auto_scroll_page(self):
        # Auto scroll and click "See more jobs" btn
        jobs_num = self.get_total_search_results()
        i = 2
        while i <= int(jobs_num / 2) + 1:
            # We keep scrolling down to the end of the view.
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            i = i + 1
            try:
                # We try to click on the see  more results buttons in case it is already displayed.
                btn_scroll = self.driver.find_element(By.XPATH, "//button[contains(text(),'See more jobs')]")
                self.driver.execute_script("arguments[0].click();", btn_scroll)
                time.sleep(0.1)
            except IndexError:
                # If there is no button, there will be an error, so we keep scrolling down.
                time.sleep(0.1)
                pass

    def get_results(self):

        # Get all the job listed
        job_lists = self.driver.find_element(By.CLASS_NAME, "jobs-search__results-list")

        # Make a list with all the jobs results
        jobs = job_lists.find_elements(By.TAG_NAME, "li")  # return a list

        # Get job title
        for job in jobs:
            job_title = job.find_element(By.CSS_SELECTOR, "h3").get_attribute("innerText")
            self.job_title_lst.append(job_title)

        # Get company
            company_name = job.find_element(By.CSS_SELECTOR, "h4").get_attribute("innerText")
            self.company_list.append(company_name)

        # Get location
            location = job.find_element(By.CSS_SELECTOR, "div>div>span").get_attribute("innerText")
            self.job_location.append(location)

        # Get date
            date = job.find_element(By.CSS_SELECTOR, "div>div>time").get_attribute("datetime")
            self.date_list.append(date)

        # Get job_link
            job_link = job.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
            self.link_list.append(job_link)

    def make_dataframe(self):
        # Make DataFrames for each list : Date Posted,Job Title, Company and Link

        df_date_list = pd.DataFrame(self.date_list, columns=["Posted"])
        df_job = pd.DataFrame(self.job_title_lst, columns=["Job Title"])
        df_comp = pd.DataFrame(self.company_list, columns=["Company"])
        df_links = pd.DataFrame(self.link_list, columns=["LINK"])
        df_location = pd.DataFrame(self.job_location, columns=["Location"])

        # Make a single DataFrame with the following columns :Date Posted,Job Title, Company and Link
        temp_1 = df_date_list.join(df_job)
        temp_2 = temp_1.join(df_comp)
        df_final = temp_2.join(df_links)
        df_final2 = df_final.join(df_location)

        # TODO - make link clickable in DF
        return df_final2

    def save_csv_file(self):
        # Save the results as *.csv file with the name of the job title as filename
        # Directory
        output_dir = "output_file"

        # Filename
        filename = self.ui_job_title.text()
        # Path

        path = os.getcwd() + "\\" + output_dir + "\\" + filename + ".csv"

        # Save to *.csv
        df = self.make_dataframe().to_csv(path)
        return df


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = GuiSearchWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
