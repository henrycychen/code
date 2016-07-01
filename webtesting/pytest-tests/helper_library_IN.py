import requests
import json

#Use package faker factory to generate random information
from faker import Factory
faker = Factory.create()

class Generate_information(object):

    def create_name(self):
        self.create_name = faker.name()
        fake_name = str(self.create_name)
        return fake_name

    def create_email(self):
        self.create_email = faker.email()
        fake_email = str(self.create_email)
        return fake_email

    def create_first_name(self):
        self.create_first_name = faker.first_name()
        fake_first_name = str(self.create_first_name)
        return fake_first_name

    def create_last_name(self):
        self.create_last_name = faker.last_name()
        fake_last_name = str(self.create_last_name)
        return fake_last_name

    def create_item(self):
        self.create_item = faker.ssn()
        fake_item = self.create_item
        return fake_item

    #Creates a fake name and splits the name into an email so the name and email match accordingly
    def split_name_to_email(self,name=''):
        self.split_name_to_email = name
        split_name = (str(self.split_name_to_email)).split(' ',1)
        return (split_name[0]+split_name[1]+'@testmail.com').lower()

class Invoice_ninja(object):
    server_ip = '104.236.192.231'
    server_api = '/api/v1/'
    invoice_ninja_clients_url = 'http://' + server_ip + server_api + 'clients'
    invoice_ninja_invoices_url = 'http://' + server_ip + server_api + 'invoices'
    get_request_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    post_request_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}

    def get_client(self,get_client = 'hello'):
        self.get_client = requests.get(Invoice_ninja.invoice_ninja_clients_url,headers=Invoice_ninja.get_request_header)
        print self.get_client.status_code

    #Function to create 10 clients. Should be used for new servers.
    def create_10_clients(self):
        self.create_10_clients = ''
        for i in range(0,10):
            my_data = json.dumps({'name': Generate_information().create_name(), 'contact':{'email': Generate_information().split_name_to_email(Generate_information().create_name())}})
            r = requests.post(Invoice_ninja().invoice_ninja_clients_url,headers=Invoice_ninja().post_request_header,data=my_data)
