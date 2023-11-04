from bs4 import BeautifulSoup
from email.header import decode_header
import imaplib
import filecmp
import shutil
import email
import time

import os




class MailBasicOrganizer:

    def __init__(self,email:str,):
        
        myaddresses = {'gmail1':'gmail password1',
                   'gmail2':'gmail password2',
                   'gmail3':'gmail password3'}

        self.EMAIL = email
        self.APP_PASSWORD = myaddresses[email]
        self.IMAP_SERVER = 'imap.gmail.com'

        self.filter_dict={'university': ['university','uni','admission','office','student'],
                          
                        'Stellenbewerbung' : ['career','assessment','internship',
                                            'vancanc','job',
                                            'applying','applied','apply',
                                            'invite','recruit',
                                            'application','workday']
            }


        self.copyallmails2()


        self.sort_mails()






    def sort_mails(self):

        self.filter_mail('university')
        self.filter_mail('Stellenbewerbung')
        time.sleep(2)

        self.inbox2starred()
        self.inbox2important()
        self.inbox2archive()







    
    def copyallmails2(self):

        base_directory = '/your desktop-directory'
        folder_name = 'newmails'
        os.chdir(base_directory)
        os.system(f'mkdir {folder_name}')

        os.chdir(os.path.join(base_directory, folder_name))




        mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
        mail.login(self.EMAIL, self.APP_PASSWORD)
        mail.select('"[Gmail]/All Mail"')
        result, data = mail.search(None, 'ALL')





        try:

            # Fetch each email and save its body to a separate file
            for num in data[0].split():
                result, data = mail.fetch(num, '(RFC822)')
                raw_email = data[0][1]

                msg = email.message_from_bytes(raw_email)

                sender = msg.get('From')
                subject = msg.get('Subject')

                # Sanitize the file name
                sender_sanitized = sender[:30].replace('/', '-').replace('\r', '').replace('\t', '').strip()
                subject_sanitized = subject[:30].replace('/', '-').replace('\r', '').replace('\t', '').strip()
                file_name = f"{sender_sanitized}_{subject_sanitized}.eml"

                # Save the email body to a file
                with open(file_name, 'wb') as file:
                    file.write(raw_email)



            mail.close()
            mail.logout()

        except Exception as e:
            print(f"An error ,., occurred: {e}")
        finally:
            if mail.state != 'LOGOUT':
                mail.close()
                mail.logout()





        new_directory = os.path.join('/your-directory/emails/', self.EMAIL)
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
            print(f"Directory '{new_directory}' created.")



        old_folder = os.path.join('/your-directory/emails/', self.EMAIL)
        new_folder = os.path.join(base_directory, folder_name)


        os.chdir('/your desktop-directory')


        dcmp = filecmp.dircmp(old_folder, new_folder)

        new_files = dcmp.right_only


        for file in new_files:
            src = os.path.join(new_folder, file)
            dst = os.path.join(old_folder, file)
            shutil.move(src, dst)



        folder_to_delete = os.path.join(base_directory, folder_name)

        try:
            shutil.rmtree(folder_to_delete)
        except OSError as e:
            print(f"Error: {folder_to_delete} - {e.strerror}")








        



    def copyallmails(self):
        base_directory = '/your desktop-directory'
        folder_name = 'newmails'
        os.chdir(base_directory)
        os.system(f'mkdir {folder_name}')

        os.chdir(os.path.join(base_directory, folder_name))



        try:

            mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
            mail.login(self.EMAIL, self.APP_PASSWORD)
            mail.select('"[Gmail]/All Mail"')

            status, data = mail.search(None, "ALL")
            mail_ids = data[0].split()

            for num in mail_ids:

                typ, data = mail.fetch(num, '(RFC822)')
                raw_email = data[0][1]
                email_message = email.message_from_bytes(raw_email)

                sender = email_message['From']
                subject = email_message['Subject']

                # Convert HTML to plain text for subject if needed
                if email_message.is_multipart():
                    for part in email_message.walk():
                        content_type = part.get_content_type()
                        if "text/html" in content_type:
                            #content = part.get_payload(decode=True).decode()
                            content = part.get_payload(decode=True).decode('utf-8', 'ignore')
                            soup = BeautifulSoup(content, "html.parser")
                            subject = soup.get_text()

                # Replace invalid characters in filenames and save the email
                file_name = f"{sender}_{subject[:30]}.eml".replace('_', " ")#.replace(':', '_').replace(' ', '_')
                with open(file_name, 'wb') as file:
                    file.write(raw_email)

    

            mail.close()
            mail.logout()

        except Exception as e:
            print(f"An error ,., occurred: {e}")
        finally:
            if mail.state != 'LOGOUT':
                mail.close()
                mail.logout()
                
                



        new_directory = os.path.join('/your-directory/emails/', self.EMAIL)
        if not os.path.exists(new_directory):
            os.makedirs(new_directory)
            print(f"Directory '{new_directory}' created.")



        old_folder = os.path.join('/your-directory/emails/', self.EMAIL)
        new_folder = os.path.join(base_directory, folder_name)


        os.chdir('/your desktop-directory')


        dcmp = filecmp.dircmp(old_folder, new_folder)

        new_files = dcmp.right_only


        for file in new_files:
            src = os.path.join(new_folder, file)
            dst = os.path.join(old_folder, file)
            shutil.move(src, dst)

            
            
        folder_to_delete = os.path.join(base_directory, folder_name)

        try:
            shutil.rmtree(folder_to_delete)
        except OSError as e:
            print(f"Error: {folder_to_delete} - {e.strerror}")





    def inbox2important(self):
        try:
            start_time = time.time()
            max_allowed_time = 60*3

            mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
            mail.login(self.EMAIL, self.APP_PASSWORD)
            mail.select("inbox")

            status, data = mail.search(None, "X-GM-RAW", "is:important")
            mail_ids = data[0].split()



            if len(mail_ids)!=0:
                
                while len(mail_ids)!=0:

                    status, data = mail.search(None, "X-GM-RAW", "is:important")
                    mail_ids = data[0].split()

                    for i,num in enumerate(mail_ids):
                        mail.copy(num, 'Important')


                        mail.store(num, '+FLAGS', '\\Deleted')
                        time.sleep(.5)
                        mail.expunge()
                        time.sleep(.5)

                        
                        
                    current_time = time.time()
                    elapsed_time = current_time - start_time


                    if elapsed_time > max_allowed_time:
                        mail.expunge()
                        break
                        
                        
                    time.sleep(1)

            mail.close()
            mail.logout()

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if mail.state != 'LOGOUT':
                mail.close()
                mail.logout()
      

    def inbox2starred(self):
        try:
            start_time = time.time()
            max_allowed_time = 60*3

            mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
            mail.login(self.EMAIL, self.APP_PASSWORD)
            mail.select("inbox")

            status, data = mail.search(None, "X-GM-RAW", "is:starred")
            mail_ids = data[0].split()



            if len(mail_ids)!=0:
                
                while len(mail_ids)!=0:

                    status, data = mail.search(None, "X-GM-RAW", "is:starred")
                    mail_ids = data[0].split()

                    for i,num in enumerate(mail_ids):
                        mail.copy(num, 'Starred')


                        mail.store(num, '+FLAGS', '\\Deleted')
                        time.sleep(.5)
                        mail.expunge()
                        time.sleep(.5)

                        
                    current_time = time.time()
                    elapsed_time = current_time - start_time

                    if elapsed_time > max_allowed_time:
                        mail.expunge()
                        break

                    time.sleep(1)

            mail.close()
            mail.logout()

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if mail.state != 'LOGOUT':
                mail.close()
                mail.logout()


    def inbox2archive(self):
        try:
            start_time = time.time()
            max_allowed_time = 60*3

            mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
            mail.login(self.EMAIL, self.APP_PASSWORD)
            mail.select("inbox")

            status, data = mail.search(None, "ALL")
            mail_ids = data[0].split()



            if len(mail_ids)!=0:
                
                while len(mail_ids)!=0:

                    status, data = mail.search(None, "ALL")
                    mail_ids = data[0].split()

                    for i,num in enumerate(mail_ids):
                        mail.copy(num, '"All Mail"')

                        mail.store(num, '+FLAGS', '\\Deleted')
                        time.sleep(.5)
                        mail.expunge()
                        time.sleep(.5)

                        
                    current_time = time.time()
                    elapsed_time = current_time - start_time

                    if elapsed_time > max_allowed_time:
                        mail.expunge()
                        break

                    time.sleep(1)

            mail.close()
            mail.logout()

        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if mail.state != 'LOGOUT':
                mail.close()
                mail.logout()


            

    def filter_mail(self,label):

        lista = self.filter_dict[label] + [word.capitalize() for word in self.filter_dict[label]]

        mail = imaplib.IMAP4_SSL(self.IMAP_SERVER)
        mail.login(self.EMAIL,self.APP_PASSWORD)
        mail.select("inbox")

        status, data = mail.search(None, "ALL")
        mail_ids = data[0].split()




        checkmate=True


        try:
            while checkmate:

                status, data = mail.search(None, "ALL")
                mail_ids = data[0].split()
                if len(mail_ids)==0:
                    break
                
                try:
                    for i,num in enumerate(mail_ids):

                        status, data = mail.fetch(num, "(RFC822)")
                        raw_email = data[0][1]



                        message = email.message_from_bytes(raw_email)


                        sender = message['From']


                        subject = message['Subject']

                        body = ""

                        if message.is_multipart():
                            for part in message.walk():
                                content_type = part.get_content_type()
                                content_disposition = str(part.get("Content-Disposition"))

                                if part.get_content_type() == "text/plain":
                                    body = part.get_payload(decode=True).decode('UTF-8')
                                    break
                        else:
                            body = message.get_payload(decode=True).decode('UTF-8')


                        text = body + sender + subject 



                        if any(word in text for word in lista):
                            #print(i,text)

                            mail.store(num, '+X-GM-LABELS', label)
                            mail.store(num, '+FLAGS', '\\Deleted')
                            time.sleep(.5)
                            mail.expunge()
                            checkmate=True


                        else:
                            #print('porcoddio')
                            checkmate=False

                except:
                    #print('porcamadonna')
                    pass

                
            mail.expunge()
            mail.close()
            mail.logout()        
                
        except Exception as e:
            print(f"An error occurred: {e}")
        finally:
            if mail.state != 'LOGOUT':
                mail.close()
                mail.logout()






if __name__=="__main__":
    m = MailBasicOrganizer('gmail1')
    m.sort_mails()

    m = MailBasicOrganizer('gmail2')
    m.sort_mails()

    print('done.')
