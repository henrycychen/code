import json
import pytest
import requests

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

#Create an invoice to client id 2 and add an item to the invoice.
def test_post_invoice():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'test_item1234'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test4'

#Check whether my invoice went to the correct client/
def test_check_post_invoice():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices',headers=my_header)
    r.status_code
    #changes the json text back to a python string
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 2 and check_assert['data'][0]['invoice_items'][0]['product_key'] == 'test_item1234'
    print 'test5'

#Try to update an exiting client email

def test_post_update_client():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'contact':{'id':3,'email':'whereisthis@1234'}})
    r = requests.post('http://104.236.192.231/api/v1/clients',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test6'

#Check to see if the existing client email was updated
def test_check_update_client():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients',headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['contacts'][0]['email'] == 'whereisthis@1234' and check_assert['data'][0]['contacts'][0]['id'] == 3
    print 'test7'

#Create a new invoice to an existing client and seeing if the exiting item will show up in the invoice
def test_post_invoice_existing_item():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'New_item'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test8'

#Check to see if the existing item showed up under the new invoice
def test_check_post_invoice_existing_item():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices',headers=my_header)
    r.status_code
    #changes the json text back to a python string
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 2 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123'
    print 'test9'

#Create a new invoice, but adding two items instead of one.
def test_post_invoice_existing_itemssss():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'client_id':'2', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test10'

#Check to see if both items were added to the invoice
def test_check_post_invoice_two_existing_item():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices',headers=my_header)
    r.status_code
    #changes the json text back to a python string
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 2 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123' and check_assert['data'][0]['invoice_items'][1]['notes'] == 'new item 321'
    print 'test11'

#Posting an invoice by using an existing email address instead of using client ID
def test_post_existing_email_add_invoices():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'email':'set_email888@gmail.com', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test12'

#Check to see if the invoice showed up under the existing email/client
def test_check_existing_email_add_invoices():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 54 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123' and check_assert['data'][0]['invoice_items'][1]['notes'] == 'new item 321'
    print 'test13'


#Testing to see if posting works with a new email and additional info while also entering an invoice
def test_post_new_client_and_add_invoices():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'email':'newtest_email888@gmail.com','name':'Hank', 'private_notes':'testtest','first_name':'Hank','last_name':'Chen', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test14'



#Check to see if the new client was added with the other information
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['name'] == 'Hank' and check_assert['data'][0]['private_notes'] == 'testtest' and check_assert['data'][0]['contacts'][0]['first_name'] == 'Hank' and check_assert['data'][0]['contacts'][0]['last_name'] == 'Chen' and check_assert['data'][0]['contacts'][0]['email'] == 'newtest_email888@gmail.com'
    print 'test15'


#Check to see if the post added the invoice to the correct client and items
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['client_id'] == 55 and check_assert['data'][0]['invoice_items'][0]['notes'] == 'new item 123' and check_assert['data'][0]['invoice_items'][1]['notes'] == 'new item 321'
    print 'test16'

#creating a new client and turning email invoice toggle to true
def test_post_new_client_and_add_invoices():
    my_header = {'content-type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'email_invoice':'True', 'invoice_date':'2016-06-27','email':'henrycychen@gmail.com','name':'Henry', 'private_notes':'testtest','first_name':'Henry','last_name':'Chen', 'invoice_items':[{'product_key': 'New_item'},{'product_key': 'New_item2'}]})
    r = requests.post('http://104.236.192.231/api/v1/invoices',headers=my_header, data=my_data)
    r.status_code
    r.text
    print 'test17'

#checks to see if the send_invoice field was updated to true
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/clients', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['contacts'][0]['send_invoice'] == True
    print 'test18'

#check if invoice date was updated
def test_check_assert_post_new_client_and_add_invoices_1():
    my_header = {'X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    r = requests.get('http://104.236.192.231/api/v1/invoices', headers=my_header)
    r.status_code
    check_assert = json.loads(r.text)
    assert check_assert['data'][0]['invoice_date'] == '2016-06-27'
    print 'test19'

#post request to send invoice # 13 to client - this test failed due to no email server setup
def test_post_email_invoice_to_client():
    my_header = {'Content-Type': 'application/json','X-Ninja-Token':'0277NOxWP8SBEjfqxLz9PaDATu7Y95oq', 'X-Requested-With':'XMLHttpRequest'}
    my_data = json.dumps({'id':'13'})
    r = requests.post('http://104.236.192.231/api/v1/email_invoice', headers=my_header, data=my_data)
    r.status_code
    print 'test20'



