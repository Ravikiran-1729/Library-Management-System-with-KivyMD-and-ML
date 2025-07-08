
from kivy.properties import ObjectProperty
from datetime import datetime, timedelta
from kivy.core.text import LabelBase
from kivy.metrics import dp
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.datatables import MDDataTable
import random
import pywhatkit
import csv

from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.label import MDLabel
from reportlab.lib.pdfencrypt import padding


import pandas as pd
from sklearn.neighbors import NearestNeighbors
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Read CSV file
df = pd.read_csv('data\\Books.csv', on_bad_lines='skip')

df.drop_duplicates(subset="Name", inplace=True)
df.fillna('', inplace=True)

# Create a lowercase version of the book titles for searching
df["Name_lower"] = df["Name"].str.lower()

vec = TfidfVectorizer()
tfid_matrix = vec.fit_transform(df["Name_lower"])

s_matrix = cosine_similarity(tfid_matrix)

knn = NearestNeighbors(n_neighbors=5, metric="cosine")
knn.fit(s_matrix)


def get_books():
    with open('data\\Books.csv', 'r', encoding='utf-8') as file:
        csv_reader = csv.reader(file, delimiter=',')
        next(csv_reader)
        return [tuple(row) for row in csv_reader]


class MainScreen(Screen):
    pass

class LoginScreen(Screen):
    login = ObjectProperty(None)

class SignUpScreen(Screen):
    signup: ObjectProperty = ObjectProperty(None)

class ForgetPassScreen(Screen):
    forget_Password = ObjectProperty(None)

class OtpScreen(Screen):
    otp = ObjectProperty(None)

class ResetPassScreen(Screen):
    reset_pass = ObjectProperty(None)

class HomeScreen(Screen):
    home = ObjectProperty(None)

class ProfileScreen(Screen):
    profile = ObjectProperty(None)

class ProfileEditScreen(Screen):
    profile_edit = ObjectProperty(None)

class SearchBookScreen(Screen):
    search_book = ObjectProperty(None)

class NotificationScreen(Screen):
    notifications = ObjectProperty(None)

class RecommendScreen(Screen):
    recommendation = ObjectProperty(None)

class BorrowBookScreen(Screen):
    borrow_book = ObjectProperty(None)

class ReturnBookScreen(Screen):
    return_book = ObjectProperty(None)

class RenewBookScreen(Screen):
    renew_book = ObjectProperty(None)

class HistoryScreen(Screen):
    history = ObjectProperty(None)

Window.size = (327, 680)

class LMS(MDApp):
    def __init__(self):
        super().__init__()
        self.signup_sem = None
        self.signup_branch = None
        self.user_name = None
        self.book_pos_name = None
        self.book_pos = None
        self.rec_label = None
        self.rec_grid = None
        self.recommend_screen = None
        self.book_input = None
        self.data_tables = None
        self.search_grid = None
        self.search_field = None
        self.renew_grid = None
        self.renewable_books = []
        self.renew = self.renewable_books
        self.history_grid = None
        self.books_history = []
        self.history = self.books_history
        self.image_label_grid = None
        self.books = []
        self.items = self.books
        self.book_name = None
        self.isbn = None
        self.a = None
        self.back_button = None
        self.user = None
        self.dialog = None
        self.profile_edit_screen = None
        self.edit_email = None
        self.edit_prn = None
        self.edit_name = None
        self.edit_number = None
        self.edit_branch = None
        self.profile_semester = None
        self.profile_branch = None
        self.profile_number = None
        self.profile_prn = None
        self.profile_email = None
        self.profile_name = None
        self.user_no = None
        self.user_email = None
        self.user_prn = None
        self.d2 = None
        self.d3 = None
        self.d4 = None
        self.user_pass = None
        self.d1 = None
        self.edit_semester = None
        self.otp_button = None
        self.new_pass = None
        self.new_pass1 = None
        self.mobile_no = None
        self.password = None
        self.username = None


    def build(self):
        Builder.load_file('kv\\LMS.kv')
        screen_manager = ScreenManager()
        screen_manager.add_widget(MainScreen(name="main"))
        screen_manager.add_widget(HomeScreen(name="home"))
        screen_manager.add_widget(LoginScreen(name="login"))
        screen_manager.add_widget(SignUpScreen(name="signup"))
        screen_manager.add_widget(ForgetPassScreen(name="forgot_pass"))
        screen_manager.add_widget(OtpScreen(name="otp"))
        screen_manager.add_widget(ResetPassScreen(name="reset_pass"))
        screen_manager.add_widget(ProfileScreen(name="profile"))
        screen_manager.add_widget(ProfileEditScreen(name="profile_edit"))
        screen_manager.add_widget(NotificationScreen(name="notification"))
        screen_manager.add_widget(SearchBookScreen(name="searchBook"))
        screen_manager.add_widget(RecommendScreen(name="recommend"))
        screen_manager.add_widget(BorrowBookScreen(name="borrow_book"))
        screen_manager.add_widget(ReturnBookScreen(name="return_book"))
        screen_manager.add_widget(RenewBookScreen(name="renew_book"))
        screen_manager.add_widget(HistoryScreen(name="history"))

        return screen_manager

#############################################ALL INPUT TEXT############################################################
    def on_start(self):
        login_screen = self.root.get_screen("login")
        self.username = login_screen.ids.username
        self.password = login_screen.ids.password

        home_screen = self.root.get_screen("home")
        self.user = home_screen.ids.user
        self.book_pos_name = home_screen.ids.book_pos_name
        self.book_pos = home_screen.ids.book_pos

        forgot_pass_screen = self.root.get_screen("forgot_pass")
        self.mobile_no = forgot_pass_screen.ids.forgotPass_no

        reset_pass_screen = self.root.get_screen("reset_pass")
        self.new_pass = reset_pass_screen.ids.new_pass
        self.new_pass1 = reset_pass_screen.ids.new_pass1

        otp_screen = self.root.get_screen("otp")
        self.otp_button = otp_screen.ids.otp_button
        self.back_button = otp_screen.ids.back_button
        self.d1 = otp_screen.ids.d1
        self.d2 = otp_screen.ids.d2
        self.d3 = otp_screen.ids.d3
        self.d4 = otp_screen.ids.d4

        signup_screen = self.root.get_screen("signup")
        self.user_name = signup_screen.ids.signup_name
        self.user_prn = signup_screen.ids.signup_prn
        self.user_email = signup_screen.ids.signup_email
        self.user_no = signup_screen.ids.signup_no
        self.user_pass = signup_screen.ids.signup_pass
        self.signup_branch = signup_screen.ids.signup_branch
        self.signup_sem = signup_screen.ids.signup_sem

        profile_screen = self.root.get_screen("profile")
        self.profile_name = profile_screen.ids.profile_name
        self.profile_email = profile_screen.ids.profile_email
        self.profile_prn = profile_screen.ids.profile_prn
        self.profile_number = profile_screen.ids.profile_number
        self.profile_branch = profile_screen.ids.profile_branch
        self.profile_semester = profile_screen.ids.profile_semester

        self.profile_edit_screen = self.root.get_screen("profile_edit")
        self.edit_name = self.profile_edit_screen.ids.edit_name
        self.edit_email = self.profile_edit_screen.ids.edit_email
        self.edit_prn = self.profile_edit_screen.ids.edit_prn
        self.edit_number = self.profile_edit_screen.ids.edit_no
        self.edit_branch = self.profile_edit_screen.ids.edit_branch
        self.edit_semester = self.profile_edit_screen.ids.edit_sem

        borrow_screen = self.root.get_screen("borrow_book")
        self.isbn = borrow_screen.ids.isbn

        return_book_screen = self.root.get_screen("return_book")
        self.image_label_grid = return_book_screen.ids.image_label_grid

        renew_book_screen = self.root.get_screen("renew_book")
        self.renew_grid = renew_book_screen.ids.renew_grid

        history_screen = self.root.get_screen("history")
        self.history_grid = history_screen.ids.history_grid

        search_book_screen = self.root.get_screen("searchBook")
        self.search_field = search_book_screen.ids.search_field
        self.search_grid = search_book_screen.ids.search_grid

        self.recommend_screen = self.root.get_screen("recommend")
        self.book_input = self.recommend_screen.ids.book_input
        self.rec_grid = self.recommend_screen.ids.rec_grid
        self.rec_label = self.recommend_screen.ids.rec_label

    #############################################@Frequently used functions##################################################

    @staticmethod
    def change_cursor(is_enter):
        if is_enter:
            Window.set_system_cursor('hand')
        else:
            Window.set_system_cursor('arrow')
    @staticmethod
    def toggle_password_visibility(password_field, icon_button):
        if password_field.password:
            password_field.password = False
            icon_button.icon = "eye"
        else:
            password_field.password = True
            icon_button.icon = "eye-off"

    def clear_text(self):
        self.search_field.text = ""
        self.book_input.text = ""
        self.username.text = ""
        self.password.text = ""
        self.mobile_no.text = ""
        self.d1.text = ""
        self.d2.text = ""
        self.d3.text = ""
        self.d4.text = ""
        self.book_pos_name.text = ""
        self.book_pos.text = "Example.,Book Position is 1L42 , 1 represent row no., L represent left side of row, 4 represent rack/shelves no. ,2 represent shelves step no."
        self.mobile_no.text = ""
        self.isbn.text = ''

    def on_press_back_arrow(self):
        self.username.text = ""
        self.password.text = ""
        self.mobile_no.text = ""
        self.d1.text = ""
        self.d2.text = ""
        self.d3.text = ""
        self.d4.text = ""

    def focus_text_field(self, icon_button, focus, page):
        if focus:
            icon_button.icon_color = self.theme_cls.primary_color
        elif page == "password":
            icon_button.icon_color = 162 / 255, 169 / 255, 188 / 255, 1
        elif page == "sign_pass":
            icon_button.icon_color = 217 / 255, 217 / 255, 217 / 255, 1
        else:
            pass

    def otp_button_fun(self, obj):
        if obj == "True":
            self.otp_button.text = "Reset Password"
        elif obj == "1":
            self.otp_button.text = "Edit Credentials"
        elif obj == "2":
            self.otp_button.text = "Verify OTP"
        else:
            self.otp_button.text = "Sign Up"

    def otp_back_arrow_fun(self):
        if self.otp_button.text == "Sign Up":
            self.root.current = 'signup'
        elif self.otp_button.text == "Reset Password":
            self.root.current = 'reset_pass'
        elif self.otp_button.text == "Verify OTP":
            self.root.current = 'borrow_book'

############################################@DIALOG BOX most used functions##############################################
        # MDDialog box function 'dialog'
    def dialog1(self, text, title="Credential Check"):
        close_button = MDFlatButton(text="Close", on_release=self.close_dialog)
        self.dialog = MDDialog(title=title,
                               text=text,
                               size_hint=(0.84, 0.1),
                               buttons=[close_button])
        self.dialog.open()

    # MDDialog box dismiss function 'close_dialog'
    def close_dialog(self):
        self.dialog.dismiss()

###################################LoginPageWork-Start#################################################

    # login Verification function "verify"
    def verify(self, obj):
        status = False
        if self.username.text == "" or self.password.text == "":
            check = "Please enter your username & password."
            return self.dialog1(check)
        else:
            name = ""
            with open('data\\Users.csv', "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file, delimiter=",")
                for line in csv_reader:
                    try:
                        if not obj:
                            a = (line[1] == self.username.text or line[2] == self.username.text)
                        else:
                            a = (line[1] == self.edit_prn.text or line[2] == self.edit_email.text)
                        if a and line[4] == self.password.text:
                            status = True
                            name = line[0]
                            prn = line[1]
                            email = line[2]
                            number = line[3]
                            branch = line[5]
                            semester = line[6]
                            break
                    except IndexError:
                        pass
                    except Exception as e:
                        print(e)

            if status:
                if not obj:
                    check = "Login Successful" + "\nHello! " + name
                else:
                    check = "Profile Updated Successfully!"
                    self.secure_profile()
                self.root.current = "home"
                self.user.text = f"""[b]Hey! {name}[/b]"""
                self.profile_name.text = self.edit_name.text = name
                self.profile_email.text = self.edit_email.text = email
                self.profile_prn.text = self.edit_prn.text = prn
                self.profile_number.text = self.edit_number.text = number
                self.profile_semester.text = self.edit_semester.text = semester
                self.profile_branch.text = self.edit_branch.text = branch

            else:
                check = "Login Failed!. " + "Enter correct username and password."
        self.dialog1(check)

    click_count = 0
    def login_mode(self, username_text, button_text):
        self.click_count += 1
        if self.click_count % 2 == 0:
            username_text.hint_text = "Enter PRN"
            button_text.text = "VIT Email Login"
            username_text.icon_right = "dialpad"
            username_text.helper_text = "PRN of 8 digits starting with 1 2 ......only*"
            username_text.max_text_length = 8
        else:
            username_text.hint_text = "Enter Email"
            username_text.icon_right = "email-arrow-left"
            button_text.text = "VIT PRN Login"
            username_text.helper_text = "enter email ID of vit.edu only*"
            username_text.max_text_length = 50

###############################################SIGNUP Page Functions#####################################################

    # signup Verification function "check_signup"
    def check_signup(self, name, prn, email, num, password, branch, sem):
        if name == "" or prn == "" or email == "" or num == "" or password == "" or branch == "" or sem == "":
            check = "Enter all required fields"
            return self.dialog1(check)
        else:
            status = "None"
            with open('data\\Users.csv', "r") as file:
                csv_reader = csv.reader(file, delimiter=',')
                for line in csv_reader:
                    try:
                        if line[3] == num:
                            status = "num"
                            break
                        if line[1] == prn:
                            status = "prn"
                            break
                        if line[2] == email:
                            status = "email"
                            break

                        else:
                            status = False
                    except IndexError:
                        pass
            if status == "num":
                check = "Number already registered Please enter a new number"
                return self.dialog1(check)
            elif status == "prn":
                check = "PRN already registered Please enter a PRN"
                return self.dialog1(check)
            elif status == "email":
                check = "Email already registered Please enter a new email"
                return self.dialog1(check)
            else:
                self.root.current = "otp"
                self.send_otp(num)
                check = "One Time Password has been shared on your registered Whatsapp No. Successful!."
            self.dialog1(check)

##################################################FORGOT PassWord Page##################################################

    # FORGOT PASSWORD page mobile number verification function 'verify_no'
    def verify_no(self):
        status = False
        if self.mobile_no.text == "":
            check = "Please enter your Mobile Number."
            return self.dialog1(check)
        else:
            with open('data\\Users.csv', "r", encoding="utf-8") as file:
                csv_reader = csv.reader(file, delimiter=",")
                for line in csv_reader:
                    try:
                        if line[3] == self.mobile_no.text:
                            status = True
                            break
                        else:
                            status = False
                    except IndexError:
                        pass
                    except Exception as e:
                        print(e)

        if status:
            check = "One Time Password has been shared on your registered Whatsapp No. Successful!."
            self.root.current = "otp"
            self.send_otp(self.mobile_no.text)
            return self.dialog1(check)
        else:
            check = "Enter Registered Mobile Number."
        self.dialog1(check)

    def reset_password(self):
        if self.new_pass.text == "" or self.new_pass1.text == "":
            check = "Please enter your new password"
            return self.dialog1(check)

        elif not self.new_pass.text == self.new_pass1.text:
            check = "Password Does Not Match. \nPlease Re-check your password."
            return self.dialog1(check)

        else:
            with open('data\\Users.csv', "r", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file, delimiter=",")
                rows = [row for row in csv_reader]

            for row in rows:
                if row['Student_Whatsapp_no'] == self.mobile_no.text:
                    row['Student_pass'] = self.new_pass.text
                    break

            try:
                with open('data\\Users.csv', "w", newline='', encoding="utf-8") as file:
                    headers = ["Student_Name", "Student_PRN", "Student_Email", "Student_Whatsapp_no", "Student_pass",
                               "Branch", "Semester"]
                    csv_writer = csv.DictWriter(file, fieldnames=headers)
                    csv_writer.writeheader()
                    csv_writer.writerows(rows)
                check = "Password Updated Successfully!"
                self.root.current = "login"
            except Exception as e:
                print(e)
                check = "Something went wrong please try again."
        self.dialog1(check)

###############################################PROFILE & EDIT Profile Page##############################################

    def edit_profile(self):
        if self.edit_name.text == "" or self.edit_prn.text == "" or self.edit_email.text == "" or self.edit_number.text == "":
            check = "Enter all required fields"
            return self.dialog1(check)
        else:
            with open('data\\Users.csv', "r", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file, delimiter=",")
                rows = [row for row in csv_reader]

            for row in rows:
                if row['Student_Whatsapp_no'] == self.profile_number.text:
                    row['Student_Name'] = self.edit_name.text
                    row['Student_PRN'] = self.edit_prn.text
                    row['Student_Email'] = self.edit_email.text
                    row['Student_Whatsapp_no'] = self.edit_number.text
                    row['Student_pass'] = self.password.text
                    row['Branch'] = self.edit_branch.text
                    row['Semester'] = self.edit_semester.text
                    break

            with open('data\\Users.csv', newline="", mode="w", encoding="utf-8") as file:
                header = ["Student_Name", "Student_PRN", "Student_Email", "Student_Whatsapp_no", "Student_pass",
                          "Branch", "Semester"]
                csv_writer = csv.DictWriter(file, fieldnames=header)
                csv_writer.writeheader()
                csv_writer.writerows(rows)
            self.verify(True)
            self.root.current = "home"

    def secure_profile(self):
        self.profile_edit_screen.ids.edit_email.readonly = True
        self.profile_edit_screen.ids.edit_prn.readonly = True
        self.profile_edit_screen.ids.edit_no.readonly = True
        self.profile_edit_screen.ids.edit_private_credential_butn.disabled = False


#############################################OTP SEND & VERIFY PAGE#####################################################

    def send_otp(self, number):
        self.a = random.randint(1000, 9999)
        if len(str(number)) == 10:
            number1 = "+91" + str(number)
            message = f"""Your verification code is {self.a}. It expires in 10 minutes. Don’t share this code with anyone."""
            pywhatkit.sendwhatmsg_instantly(number1, message, wait_time=15, tab_close=True, close_time=3)
        elif len(str(number)) != 10:
            check = "Please enter a 10 digit number."
            return self.dialog1(check)
        else:
            pass

    def verify_otp(self, d1, d2, d3, d4, otp_button):
        entered_otp = str(d1) + str(d2) + str(d3) + str(d4)
        if entered_otp == str(self.a):
            if otp_button == "Reset Password":
                self.root.current = "reset_pass"
                check = "Reset your password "
                return self.dialog1(check)

            elif otp_button == "Edit Credentials":
                self.root.current = "profile_edit"
                check = "Edit your credentials "
                self.profile_edit_screen.ids.edit_email.readonly = False
                self.profile_edit_screen.ids.edit_prn.readonly = False
                self.profile_edit_screen.ids.edit_no.readonly = False
                self.profile_edit_screen.ids.edit_private_credential_butn.disabled = True
                return self.dialog1(check)

            elif otp_button == "Verify OTP":
                self.root.current = "home"
                self.add_book()

            else:
                data = [self.user_name.text, self.user_prn.text, self.user_email.text, self.user_no.text,
                        self.user_pass.text, self.signup_branch.text, self.signup_sem.text]

                with open('data\\Users.csv', encoding="utf-8") as file:
                    csv_writer = csv.writer(file, delimiter=",")
                    csv_writer.writerow(data)

                self.root.current = "home"
                check = "SignUP Successful" + "\nHello ! " + self.user_name.text
                self.user.text = "H e y  !" + self.user_name.text
                self.verify(True)
                return self.dialog1(check)

        elif entered_otp != str(self.a):
            check = "Please enter a correct verification code."
            self.d1.text = ""
            self.d2.text = ""
            self.d3.text = ""
            self.d4.text = ""
            return self.dialog1(check)

        else:
            check = "Sorry! Try again later."
            self.root.current = "login"
            self.d1.text = ""
            self.d2.text = ""
            self.d3.text = ""
            self.d4.text = ""
            return self.dialog1(check)

    #######################################################Borrow BOok######################################################

    def get_book(self, isbn):
        self.isbn.text = isbn
        if not self.isbn.text:
            check = "Please enter a valid ISBN."
            return self.dialog1(check)
        elif not len(self.isbn.text) == 13:
            check = "Please enter a valid ISBN."
            return self.dialog1(check)
        else:
            with open('data\\Books.csv', mode="r", encoding="utf-8") as file:
                csv_reader = csv.DictReader(file, delimiter=",")
                rows = [row for row in csv_reader]
            for row in rows:
                if row["ISBN"] == self.isbn.text:
                    if row['Availability'] == "0":
                        check = "Your book is unavailable. "
                        return self.dialog1(check)
                    else:
                        self.otp_button_fun('2')
                        self.root.current = "otp"
                        self.send_otp(self.profile_number.text, )

    def add_book(self):
        with open('data\\Books.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            rows = [row for row in csv_reader]

        for row in rows:
            if row['ISBN'] == self.isbn.text:
                try:
                    self.book_name = row['Name']
                    a = row['Availability']
                    row['Availability'] = str(int(a) - 1)
                except KeyError:
                    pass

        with open('data\\Books.csv', newline="", mode="w", encoding="utf-8") as file:
            headers = ["Name", "Author", "Publication Year", "Publisher", "ISBN",
                       "Availability"]
            csv_writer = csv.DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(rows)

        self.date = datetime.now()
        self.Due_date = self.date + timedelta(days=10)

        details = [self.profile_prn.text, self.profile_number.text, self.book_name, self.isbn.text, self.date,
                   self.Due_date, ]
        transaction_details = details + ["Not Returned"]
        borrow_details = details + ["Not Renewed"]

        files = ['data\\borrowed_books.csv', 'data\\all_book_transactions.csv']
        for file1 in files:
            with open(file1, "a", encoding="utf-8", newline='') as file:
                csv_writer = csv.writer(file, delimiter=",")
                if file1 == 'data\\borrowed_books.csv':
                    csv_writer.writerow(borrow_details)
                elif file1 == 'data\\all_book_transactions.csv':
                    csv_writer.writerow(transaction_details)

        check = "OTP Verified! \nBook Borrowed Successfully!"
        return self.dialog1(check)

    def fetch_borrowed_book(self):
        with open('data\\borrowed_books.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            rows = [row for row in csv_reader]
        self.books.clear()
        for row in rows:
            if row['User'] == self.profile_prn.text:
                book = {'source': 'assets\\sample_book_display.jpg', 'btn_text': 'Return Book', 'Book_name': row['Book_Name'],
                        'time': row['Due_Date'], 'Renew_status': row['Renew_status']}
                self.books += [book]
                print(self.books)
        self.items = self.books

    def fetch_renewable_books(self):
        with open('data\\borrowed_books.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            rows = [row for row in csv_reader]
        self.renewable_books.clear()
        for row in rows:
            a = datetime.strptime(row['Due_Date'], "%Y-%m-%d %H:%M:%S.%f")
            a = a.strftime("%d-%m-%Y")
            if row['User'] == self.profile_prn.text and row[
                'Renew_status'] == "Not Renewed" and a == datetime.now().strftime("%d-%m-%Y"):
                renew_book = {'source': 'assets\\sample_book_display.jpg', 'btn_text': 'Renew Book', 'Book_name': row['Book_Name'],
                              'time': row['Due_Date'], 'Renew_status': row['Renew_status']}
                self.renewable_books += [renew_book]
                print(self.renewable_books)
            self.renew = self.renewable_books

    def return_book(self, obj):
        if obj == 'Return':
            self.fetch_borrowed_book()
            self.image_label_grid.clear_widgets()
            book_list = self.items
        elif obj == 'Renew':
            self.fetch_renewable_books()
            self.renew_grid.clear_widgets()
            book_list = self.renew

        for item in book_list:
            box = MDBoxLayout(orientation='vertical', size_hint_y=None, height="125dp")
            anchor = AnchorLayout(anchor_x="center", anchor_y="center")
            grid = GridLayout(cols=2, spacing=dp(20), size_hint_x=None, size_hint_y=None, size=[dp(320), dp(200)],
                              padding=dp(0))

            img = Image(source=item['source'],
                        size_hint_x=None,
                        size_hint_y=None,
                        width=dp(100),
                        height=dp(125),
                        allow_stretch=True)
            label = MDLabel(
                text=item['Book_name'],
                font_name="BPoppins",
                size_hint_x=None,
                size_hint_y=None,
                bold=True,
                size=[dp(215), dp(70)],
                padding=dp(0),
                on_touch_down=lambda instance, touch: self.change_cursor(True),
                on_touch_up=lambda instance, touch: self.change_cursor(False),
            )
            date11 = item['time']
            date22 = "Due Date is "
            for i in range(10):
                date22 += date11[i]

            label1 = MDLabel(
                text=date22,
                font_name="BPoppins",
                size_hint_x=None,
                size_hint_y=None,
                size=[dp(215), dp(40)],
                padding=dp(0),
                on_touch_down=lambda instance, touch: self.change_cursor(True),
                on_touch_up=lambda instance, touch: self.change_cursor(False),
            )

            if item['btn_text'] == "Return Book":
                btn = Button(
                    text=item['btn_text'],
                    font_name="BPoppins",
                    size_hint=(None, None),
                    size=(dp(200), dp(30)),
                    background_color=(0, 0, 1, 1),
                    on_touch_down=lambda instance, touch: self.change_cursor(True),
                    on_touch_up=lambda instance, touch: self.change_cursor(False),
                    on_release=lambda instance, src=item['source'], txt=item['btn_text'], name=item['Book_name'],
                                      time=item['time']: self.remove_book(src, txt, name, time),
                )
            elif item['btn_text'] == "Renew Book":
                btn = Button(
                    text=item['btn_text'],
                    font_name="BPoppins",
                    size_hint=(None, None),
                    size=(dp(200), dp(30)),
                    background_color=(0, 0, 1, 1),
                    on_touch_down=lambda instance, touch: self.change_cursor(True),
                    on_touch_up=lambda instance, touch: self.change_cursor(False),
                    on_release=lambda instance, src=item['source'], txt=item['btn_text'], name=item['Book_name'],
                                      time=item['time']: self.renew_book(src, txt, name, time),
                )

            vertical_box = BoxLayout(orientation='vertical', size_hint_y=None, height=label.height + btn.height)
            vertical_box.add_widget(label)
            vertical_box.add_widget(label1)
            vertical_box.add_widget(btn)

            grid.add_widget(img)
            grid.add_widget(vertical_box)
            anchor.add_widget(grid)
            box.add_widget(anchor)
            if btn.text == "Return Book":
                self.image_label_grid.add_widget(box)
            elif btn.text == "Renew Book":
                self.renew_grid.add_widget(box)

    def remove_book(self, source, text, name, time):
        with open('data\\borrowed_books.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.reader(file, delimiter=",")
            header = next(csv_reader)
            rows = list(csv_reader)

        new_rows = [row for row in rows if row[0] != self.profile_prn.text or row[2] != name or row[5] != time]

        with open('data\\borrowed_books.csv', mode="w", newline="", encoding="utf-8") as file:
            csv_writer = csv.writer(file, delimiter=",")
            csv_writer.writerow(header)
            csv_writer.writerows(new_rows)

        with open('data\\all_book_transactions.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            rows = [row for row in csv_reader]

        return_date = datetime.now()
        return_date = return_date.strftime("%d/%m/%Y")

        for row in rows:
            if row['User'] == self.profile_prn.text and row['Book_Name'] == name and row['Due_Date'] == time:
                row["Return_Date"] = return_date

        with open('data\\all_book_transactions.csv', mode="w", newline="", encoding="utf-8") as file:
            headers = ['User', 'User_No', 'Book_Name', 'ISBN', 'Date', 'Due_Date', 'Return_Date', ]
            csv_writer = csv.DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(rows)

        with open('data\\Books.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            rows = [row for row in csv_reader]

        for row in rows:
            if row['Name'] == name:
                try:
                    a = row['Availability']
                    row['Availability'] = str(int(a) + 1)
                except KeyError:
                    pass

        with open('data\\Books.csv', newline="", mode="w", encoding="utf-8") as file:
            headers = ["Name", "Author", "Publication Year", "Publisher", "ISBN",
                       "Availability"]
            csv_writer = csv.DictWriter(file, fieldnames=headers)
            csv_writer.writeheader()
            csv_writer.writerows(rows)

        self.items = [item for item in self.items if
                      not (item['source'] == source and item['btn_text'] == text and item['Book_name'] == name)]

        check = "Book Returned Successfully!"
        self.dialog1(check)
        self.return_book("Return")

    def fetch_book_history(self):
        with open('data\\all_book_transactions.csv', mode="r", encoding="utf-8") as file:
            csv_reader = csv.DictReader(file, delimiter=",")
            rows = [row for row in csv_reader]
        self.books_history.clear()
        for row in rows:
            if row['User'] == self.profile_prn.text and row['Return_Date'] != 'Not Returned':
                book = {'source': 'assets\\sample_book_display.jpg', 'text': 'Rate Book', 'Book_name': row['Book_Name'],
                        'time': row['Date'], 'Return_Date': row['Return_Date']}
                self.books_history += [book]
        self.history = self.books_history

    def book_history(self):
        self.fetch_book_history()
        self.history_grid.clear_widgets()

        for item in self.history:
            box = MDBoxLayout(orientation='vertical', size_hint_y=None, height="125.001dp")
            anchor = AnchorLayout(anchor_x="center", anchor_y="center")
            grid = GridLayout(cols=2, spacing=dp(20), size_hint_x=None, size_hint_y=None, size=[dp(320), dp(200)],
                              padding=dp(0))

            img = Image(source=item['source'], size_hint_x=None, size_hint_y=None, width=dp(100), height=dp(125),
                        allow_stretch=True)
            label = MDLabel(
                text=item['Book_name'],
                font_name="BPoppins",
                size_hint_x=None,
                size_hint_y=None,
                bold=True,
                size=[dp(215), dp(60)],
                padding=dp(0),
                on_touch_down=lambda instance, touch: self.change_cursor(True),
                on_touch_up=lambda instance, touch: self.change_cursor(False),
            )

            B_date = datetime.strptime(item['time'], '%Y-%m-%d %H:%M:%S.%f')
            B_date = B_date.strftime("%d-%m-%Y")

            formated_B = ""
            for i in range(10):
                formated_B += B_date[i]

            R_date = datetime.strptime(item['Return_Date'], '%d/%m/%Y')
            R_date = R_date.strftime("%d-%m-%Y")
            formated_R = ""
            for i in range(10):
                formated_R += R_date[i]

            date22 = f"""Borrow Date: {formated_B}\nReturn Date: {formated_R}"""

            label1 = MDLabel(
                text=date22,
                font_name="BPoppins",
                size_hint_x=None,
                size_hint_y=None,
                size=[dp(215), dp(50)],
                padding=dp(0),
                on_touch_down=lambda instance, touch: self.change_cursor(True),
                on_touch_up=lambda instance, touch: self.change_cursor(False),
            )

            btn = Button(
                text=item['text'],
                font_name="BPoppins",
                size_hint=(None, None),
                size=(dp(200), dp(30)),
                background_color=(0, 0, 1, 1),
                on_touch_down=lambda instance, touch: self.change_cursor(True),
                on_touch_up=lambda instance, touch: self.change_cursor(False),
            )
            vertical_box = BoxLayout(orientation='vertical', size_hint_y=None, height=label.height + btn.height)
            vertical_box.add_widget(label)
            vertical_box.add_widget(label1)
            vertical_box.add_widget(btn)

            grid.add_widget(img)
            grid.add_widget(vertical_box)
            anchor.add_widget(grid)
            box.add_widget(anchor)
            self.history_grid.add_widget(box)

    def data_load(self):
        self.search_field.bind(text=self.search_books)
        self.search_grid.clear_widgets()
        self.data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.4},
            size_hint=(0.95, 0.5),
            use_pagination=True,
            padding=dp(0),
            rows_num=7,
            pagination_menu_pos='auto',
            background_color_selected_cell=(0.8, 0.9, 1, 1),
            column_data=[
                ("Book Name", dp(80)),
                ("Author", dp(50)),
                ("Publication Year", dp(30)),
                ("Publisher", dp(40)),
                ("ISBN", dp(30)),
                ("Availability", dp(30)),
            ],
            row_data=get_books()
        )
        self.search_grid.add_widget(self.data_tables)

    def search_books(self, instance, value):
        all_data = get_books()
        filtered_data = [row for row in all_data if (
                    value.lower() in row[0].lower() or value.lower() in row[1].lower() or value.lower() in row[4])]
        self.data_tables.row_data = filtered_data

    def get_recommendations(self):
        book_title = self.book_input.text
        recommendations = self.rec_book(book_title)
        if isinstance(recommendations, str):
            self.rec_label.text = recommendations
            self.rec_grid.clear_widgets()
        else:
            self.display_rec_table(recommendations)

    @staticmethod
    def rec_book(book_title):
        book_title_lower = book_title.lower()
        if book_title_lower not in df["Name_lower"].values:
            return f"{book_title} not in database"
        index = df[df['Name_lower'] == book_title_lower].index[0]

        distance, indices = knn.kneighbors(s_matrix[index].reshape(1, -1))
        rec_title = df.iloc[indices.flatten()]["Name"].tolist()
        aval = df.iloc[indices.flatten()]["Availability"].tolist()
        isbn = df.iloc[indices.flatten()]["ISBN"].tolist()

        recommendation = list(zip(rec_title, isbn, aval))

        return recommendation

    def display_rec_table(self, recommendations):
        self.rec_grid.clear_widgets()
        data_tables = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.2},
            size_hint=(0.95, 0.2),
            use_pagination=True,
            padding=dp(0),
            rows_num=6,
            pagination_menu_pos='auto',
            background_color_selected_cell=(0.8, 0.9, 1, 1),
            column_data=[
                ("Book Name", dp(80)),
                ("ISBN", dp(30)),
                ("Availability", dp(30)),
            ],
            row_data=[(title, isbn, availability) for title, isbn, availability in recommendations]
        )
        self.rec_grid.add_widget(data_tables)

    def where_is_book(self):
        with open('data\\book_positions.csv', 'r') as csvfile:
            data = csv.reader(csvfile, delimiter=',')
            rows = list(data)
            a = self.book_pos_name.text.lower()
            for row in rows:
                if row[0].lower() == a:
                    pos = str(row[1])
                    self.book_pos.text = f"{a.upper()} Book is kept at {row[1]} location. Please Go and Borrow it!!\n({row[1]} means {pos[0]} th row, Left/Right side(L/R), {pos[2]} th shelf, {pos[3]} th shelf step )"
                    break
                else:
                    self.book_pos.text = "Please check the Spell!"


LabelBase.register(name="MPoppins", fn_regular="fonts\\Poppins\\Poppins-Medium.ttf")
LabelBase.register(name="BPoppins", fn_regular="fonts\\Poppins\\Poppins-SemiBold.ttf")
LabelBase.register(name="RRubik",   fn_regular="fonts\\Rubik_Vinyl\\RubikVinyl-Regular.ttf")
LabelBase.register(name="RCro",     fn_regular="fonts\\Croissant_One\\CroissantOne-Regular.ttf")
LabelBase.register(name="RPac",     fn_regular="fonts\\Pacifico\\Pacifico-Regular.ttf")

if __name__ == '__main__':
    LMS().run()
