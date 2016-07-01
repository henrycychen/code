import json
import pytest
import requests
from helper_library_IN import *

"""
QA_invoice_ninja.py has the following Classes:
Generate_information
Invoice_ninja()

Class Generate_information() - uses the faker package to generate fake data for testing.
Class Invoice_ninja() - has information regarding server, api, header information
"""

#Creating some global variables to avoid repetition for future asserts and tests).
i = Invoice_ninja() #Variable for Class Invoice Ninja

g = Generate_information() #Variable for Class Generate Information
#name = g.create_name() #Create client name into

fake_item1 = g.create_item()

#create test_client which is the most recent client ID created
r1 = requests.get(i.invoice_ninja_clients_url,headers=i.get_request_header)
test_client = (json.loads(r1.text))['data'][0]['id']


#Get all the clients from the database and check to see if the status code is good (response 200).
@pytest.mark.client
def test_get_client():
    r = requests.get(i.invoice_ninja_clients_url,headers=i.get_request_header)
    assert r.status_code == 200

#Create a new client name and email using the faker generator while also splitting the name.
@pytest.mark.client
def test_post_new_client():
    my_data = json.dumps({'name': name, 'contact':{'email': g.split_name_to_email(name)}})
    r = requests.post(i.invoice_ninja_clients_url,headers=i.post_request_header,data=my_data)

#Checks to see if the new client is in the database.
@pytest.mark.client
def test_check_assert_post_new_client():
    r = requests.get(i.invoice_ninja_clients_url,headers=i.get_request_header)
    assert name in r.text


#Get all the invoices from the database and check to see if status code is good (response 200).
@pytest.mark.invoices
def test_get_invoices():
    r = requests.get(i.invoice_ninja_invoices_url,headers=i.get_request_header)
    assert r.status_code == 200

#Enter an invoice under an existing client by using the latest client ID (test_client)
@pytest.mark.invoices
def test_post_invoices():
    my_data = json.dumps({'client_id':test_client, 'invoice_items':[{'product_key': fake_item1},{'product_key': fake_item1}]})
    r = requests.post(i.invoice_ninja_invoices_url,headers=i.post_request_header,data=my_data)

#checking to see if both items appeared on the invoice under the most recent client_id
@pytest.mark.invoices
def test_check_assert_post_invoices():
    r = requests.get(i.invoice_ninja_invoices_url,headers=i.get_request_header)
    check_asserts = (json.loads(r.text))
    assert check_asserts['data'][0]['client_id'] == test_client and (fake_item1 in r.text) and (fake_item1 in r.text)

#creating 10 new clients if a new server is created
i.get_client()
#i.create_10_clients()