import requests
import json
import random

#Use package faker factory to generate random information
from faker import Factory
faker = Factory.create()

class Generate_information(object):

    def create_name(self):
        self.create_name = faker.name()
        return str(self.create_name)

    def create_email(self):
        self.create_email = faker.email()
        return str(self.create_email)

    def create_first_name(self):
        self.create_first_name = faker.first_name()
        return str(self.create_first_name)

    def create_last_name(self):
        self.create_last_name = faker.last_name()
        return str(self.create_last_name)

    def create_item(self):
        self.create_item = faker.ssn()
        return str(self.create_item)

    def create_id_num(self):
        self.create_id_num = random.randint(1000,9999)
        return str(self.create_id_num)

    def create_vat_num(self):
        self.create_vat_num = random.randint(10000,99999)
        return str(self.create_vat_num)

    def create_company(self):
        self.create_company = faker.providers()
        return self.create_company

    def create_website(self,website=''):
        self.create_website = website
        create_website = (str(self.create_website)).split(' ',1)
        return ('www.'+create_website[0]+create_website[1]+'.com').lower()

    def create_phone(self):
        self.create_phone = str(random.randint(1000000,9999999))
        return str(self.create_phone[0:3]+'-'+self.create_phone[3:6]+'-'+self.create_phone[0:4])

    #Creates a fake name and splits the name into an email so the name and email match accordingly
    def split_name_to_email(self,name=''):
        self.split_name_to_email = name
        split_name = (str(self.split_name_to_email)).split(' ',1)
        return (split_name[0]+split_name[1]+'@testmail.com').lower()

    def create_street_address(self):
        self.create_street_address = str(random.randint(1,1000))+' '+faker.first_name()+ ' Street'
        return str(self.create_street_address)

    def create_apt_suite(self):
        self.create_apt_suite = ''
        a_or_s = random.randint(0,1)
        if a_or_s == 0:
            a_or_s = 'Apt'
        else:
            a_or_s = 'Suite'
        self.create_apt_suite = a_or_s +' ' + str(random.randint(100,999))
        return str(self.create_apt_suite)

    def create_state_or_province(self):
        self.create_state_or_province = faker.first_name()
        return self.create_state_or_province[0:2].upper()

    def create_postal_code(self):
        self.create_postal_code = random.randint(10000,99999)
        return str(self.create_postal_code)

    def create_invoice_date(self):
        self.create_invoice_date = str(random.randint(2016,2017))+'-'+str(random.randint(10,12))+'-'+str(random.randint(10,31))
        return self.create_invoice_date

    def create_partial(self):
        self.create_partial = random.randint(0,5)
        return self.create_partial

    def create_cost(self):
        self.create_cost = random.randint(1000,10000)
        return self.create_cost



class Invoice_ninja(object):
    server_ip = '104.236.192.231'
    server_api = '/api/v1/'
    invoice_ninja_clients_url = 'http://' + server_ip + server_api + 'clients'
    invoice_ninja_invoices_url = 'http://' + server_ip + server_api + 'invoices'
    invoice_ninja_payments_url = 'http://' + server_ip + server_api + 'payments'
    invoice_ninja_tasks_url = 'http://' + server_ip + server_api + 'tasks'
    get_request_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    post_request_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}

    def get_client(self):
        self.get_client = requests.get(Invoice_ninja().invoice_ninja_clients_url,headers=Invoice_ninja().get_request_header)
        return self.get_client

    def get_invoice(self):
        self.get_invoice = requests.get(Invoice_ninja().invoice_ninja_invoices_url,headers=Invoice_ninja().get_request_header)
        return self.get_invoice

    def post_client(self):
        self.post_client = requests.post(Invoice_ninja().invoice_ninja_clients_url,headers=Invoice_ninja().post_request_header)
        return self.post_client

    def post_invoice(self):
        self.post_invoice = requests.post(Invoice_ninja().invoice_ninja_invoices_url(),headers=Invoice_ninja().post_request_header())
        return self.post_invoice

    #Function to create 10 clients. Should be used for new servers.
    def create_10_clients(self):
        self.create_10_clients = ''
        for i in range(0,10):
            new_client = Generate_information().create_name()
            my_data = json.dumps({'name':new_client, 'contact':{'email': Generate_information().split_name_to_email(new_client)}})
            r = requests.post(Invoice_ninja().invoice_ninja_clients_url,headers=Invoice_ninja().post_request_header,data=my_data)

    #Function to create one client.
    def create_new_client(self,name=''):
        self.create_new_client = Generate_information().create_name()
        name = self.create_new_client
        my_data = json.dumps({'name': name, 'contact':{'email': Generate_information().split_name_to_email(name)}})
        r = requests.post(Invoice_ninja().invoice_ninja_clients_url,headers=Invoice_ninja().post_request_header,data=my_data)