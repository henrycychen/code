import json
import pytest
import requests

"""
#Get all client database.
def test_request_get():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients',headers=my_header)
    r.status_code
    r.text
    assert r.status_code == 200
    print 'test1'

#Create a new client
def test_post():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'name':'Hank_test123','contact':{'email':'test123123@gmail.com'}})
    r = requests.post('http://104.236.192.231/api/v1/clients',headers=my_header, data=my_data)
    r.status_code
    r.text
    assert r.status_code == 200
    print 'test2'

#Check if client is in the database
def test_post_client():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients',headers=my_header)
    r.status_code
    r.text
    assert 'test123123@gmail.com' in r.text
    print 'test3'

#Create an invoice to client id 2 and item: test_item1234.
def test_post_invoice():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'test_item1234'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test4'

#Check whether my post went to the correct client with the correct item by using request get
def test_check_post_invoice():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices',headers=my_header)
    r.status_code
    #changes the json text back to a python string
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 2 and check_assert['data'][0]['invoice_items'][0]['product_key'] == 'test_item1234'
    print 'test5'

#curl -X POST ninja.dev/api/v1/clients -H "Content-Type:application/json" -d '{"name":"Client","contact":{"email":"test@gmail.com"}}' -H "X-Ninja-Token: TOKEN" -H "X-Requested-With: XMLHttpRequest"
#Updating client information

def test_post_update_client():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'contact':{'id':3,'email':'whereisthis@1234'}})
    r = requests.post('http://104.236.192.231/api/v1/clients',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test6'

def test_check_update_client():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients',headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['contacts'][0]['email'] == 'whereisthis@1234' and check_assert['data'][0]['contacts'][0]['id'] == 3
    print 'test7'

#Create a new invoice testing if an existing item description will populate into client 2
def test_post_invoice_existing_item():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'New_item'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test8'

def test_check_post_invoice_existing_item():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices',headers=my_header)
    r.status_code
    #changes the json text back to a python string
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 2 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123'
    print 'test9'

#Create a new invoice testing if TWO existing item description will populate into client 2
def test_post_invoice_existing_itemssss():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test10'


def test_check_post_invoice_two_existing_item():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices',headers=my_header)
    r.status_code
    #changes the json text back to a python string
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 2 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123' and check_assert['data'][0]['invoice_items'][1]['notes'] == 'new item 321'
    print 'test11'


#Create a new invoice testing if TWO existing item description will populate into client 2
def test_post_invoice_existing_items():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    check_assert = json.loads(r.text)
    print 'test12'



def test_post_existing_email_add_invoices():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'email':'set_email888@gmail.com', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test13'


def test_check_existing_email_add_invoices():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 54 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123' and check_assert['data'][0]['invoice_items'][1]['notes'] == 'new item 321'
    print 'test14'


#Testing to see if posting works with a new email and additional info while also entering an invoice
def test_post_new_client_and_add_invoices():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'email':'newtest_email888@gmail.com','name':'Hank', 'private_notes':'testtest','first_name':'Hank','last_name':'Chen', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test15'



#tests to see if the new client was added with the other information
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['name'] == 'Hank' and check_assert['data'][0]['private_notes'] == 'testtest' and check_assert['data'][0]['contacts'][0]['first_name'] == 'Hank' and check_assert['data'][0]['contacts'][0]['last_name'] == 'Chen' and check_assert['data'][0]['contacts'][0]['email'] == 'newtest_email888@gmail.com'
    print 'test16'


#tests to see if the post added the invoice to the correct client and items
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 55 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123' and check_assert['data'][0]['invoice_items'][1]['notes'] == 'new item 321'
    print 'test17'

#creating a new client and emailing the invoice to the client
def test_post_new_client_and_add_invoices():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'email_invoice':'True', 'invoice_date':'2016-06-27','email':'henrycychen@gmail.com','name':'Henry', 'private_notes':'testtest','first_name':'Henry','last_name':'Chen', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test18'

#checks to see if the send_invoice field was updated to true
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['contacts'][0]['send_invoice'] == True
    print 'test19'

#check if invoice date was updated
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['invoice_date'] == '2016-06-27'
    print 'test20'

"""

#post request to send invoice # 13 to client
def test_post_email_invoice_to_client():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'id':13})
    r = requests.post('http://104.236.192.231/api/v1/email_invoice', headers=my_header, data=my_data)
    r.status_code
    print 'test21'



