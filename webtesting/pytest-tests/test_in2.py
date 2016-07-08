"""
Testing the functionalities of each testable tab and API on Invoice
Ninja (Client, Tasks, Invoices, and Payments). Unfortunately, the Quotes
API is the same as the Invoices API (testing the web browser Quotes tab,
the data will end up under the invoices database). Also, per the API,
there isn't a POST Quotes API, only a GET, but it does not work.
"""

import pytest
import json
import requests
import random
from helper_library_IN import Invoice_ninja
from helper_library_IN import Generate_information

i = Invoice_ninja()
g = Generate_information()

#Email is the only required field to create a new account, let's test
# to see if that is true by not entering one. (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_email_validity():
    name = g.create_name()
    my_data = json.dumps({'name':name})
    r1 = i.post_client(my_data=my_data)
    assert r1.status_code == 500

#Test to see if an existing email can be used on another client (minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_existing_email():
    for tests in range(2):
        email = 'same_email@testmail.com'
        my_data = json.dumps({'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)

    r2 = i.get_client()
    check_email_1 = json.loads(r2.text)['data'][0]['contacts'][0]['email']
    check_email_2 = json.loads(r2.text)['data'][1]['contacts'][0]['email']
    assert check_email_1 == check_email_2

#Tests to see if the name field accepts strings (minimum requirement
# is email to create a new client).
@pytest.mark.client
def test_org_name_string():
    name = g.create_name()
    email = g.create_email(name)
    my_data = json.dumps({'name':name, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['name'] == name and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the name field accepts integers (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_org_name_integer():
    name = random.randint(0,100)
    email = g.create_email(g.create_name())
    my_data = json.dumps({'name':name, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['name'] == str(name) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the name field accepts special characters (minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_org_name_special_char():
    special_char = ['!','@','#','$','%','^','&','*','(',')',',']
    name = special_char[random.randint(0,11)]
    email = g.create_email(g.create_name())
    my_data = json.dumps({'name':name, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['name'] == str(name) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the id number field accepts strings (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_org_id_num_string():
    id_num = g.create_name()
    email = g.create_email(g.create_name())
    my_data = json.dumps({'id_number':id_num, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['id_number'] == str(id_num) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the id number field accepts integers (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_org_id_num_integers():
    id_num = random.randint(0,100)
    email = g.create_email(g.create_name())
    my_data = json.dumps({'id_number':id_num, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['id_number'] == str(id_num) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the id number field accepts special charachers (minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_org_id_num_special_char():
    special_char = ['!','@','#','$','%','^','&','*','(',')',',']
    id_num = special_char[random.randint(0,11)]
    email = g.create_email(g.create_name())
    my_data = json.dumps({'id_number':id_num, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['id_number'] == str(id_num) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the vat number field accepts strings (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_org_vat_num_string():
    vat_num = g.create_name()
    email = g.create_email(g.create_name())
    my_data = json.dumps({'vat_number':vat_num, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['vat_number'] == str(vat_num) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the vat number field accepts integers (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_org_vat_num_integers():
    vat_num = random.randint(0,100)
    email = g.create_email(g.create_name())
    my_data = json.dumps({'vat_number':vat_num, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['vat_number'] == str(vat_num) and \
           check_assert['contacts'][0]['email'] == email

#Tests to see if the vat number field accepts special characters (minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_org_vat_num_special_char():
    special_char = ['!','@','#','$','%','^','&','*','(',')',',']
    vat_num = special_char[random.randint(0,11)]
    email = g.create_email(g.create_name())
    my_data = json.dumps({'vat_number':vat_num, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['vat_number'] == str(vat_num) and \
           check_assert['contacts'][0]['email'] == email

#Test the website field if it will take a standard website addresses (minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_org_website():
    website = g.create_website(g.create_name())
    email = g.create_email(g.create_name())
    my_data = json.dumps({'website':website, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['website'] == website and \
           check_assert['contacts'][0]['email'] == email

#Test the website field if it will take a non-standard website addresses
# by creating a for loop and iterate through the different "addresses"(minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_org_website_nonstandard():
    website_list = ['wwwnoperioddotcom', 'www.onedotonlycom','$#@#%','12345',
                    12345,'00000']
    for websites in website_list:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'website':websites, 'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['website'] == str(websites) and \
               check_assert['contacts'][0]['email'] == email

#Test the phone field to see if it will take integers (minimum requirement
# needed is email to create a new client).
@pytest.mark.client
def test_org_phone():
    phone = g.create_phone()
    email = g.create_email(g.create_name())
    my_data = json.dumps({'work_phone':phone, 'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['work_phone'] == str(phone) and \
           check_assert['contacts'][0]['email'] == email

#Test the phone field to see if it will take a list of non-integers (minimum
# requirement needed is email to create a new client).
@pytest.mark.client
def test_org_phone_nonstandard():
    phone_list = ['!@#$%!@#','adfddfwwe','dfsd!@#fds','     123     123',
                  '123-456-7890']
    for phone_nums in phone_list:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'work_phone':phone_nums, 'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['work_phone'] == str(phone_nums) and \
               check_assert['contacts'][0]['email'] == email

#Test the street address field to see if it will take a standard street
# address format ex: 123 main street (minimum requirement needed is
# email to create a new client).
@pytest.mark.client
def test_address_street():
    address1 = g.create_street_address()
    email = g.create_email(g.create_name())
    my_data = json.dumps({'address1':address1,'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['address1'] == address1 and \
           check_assert['contacts'][0]['email'] == email

#Test the street address field to see if it will take a list of non
# standard addresses (minimum requirement needed is email to create a
# new client).
@pytest.mark.client
def test_address_street_nonstandard():
    address_list = ['$#@#$', 12324, '123@123', '  ']
    for addresses in address_list:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'address1':addresses,'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['address1'] == str(addresses) and \
               check_assert['contacts'][0]['email'] == email

#Test the second street address to see if it will take a standard
# street address format ex: apt 123 (minimum requirement needed is
# email to create a new client).
@pytest.mark.client
def test_address_apt_suite():
    address2 = g.create_apt_suite()
    email = g.create_email(g.create_name())
    my_data = json.dumps({'address2':address2,'contact':{'email':email}})
    r1 = i.post_client(my_data=my_data)
    r2 = i.get_client()
    check_assert = json.loads(r2.text)['data'][0]
    assert check_assert['address2'] == str(address2) and \
           check_assert['contacts'][0]['email'] == email


#Test the second street address to see if it will take a nonstandard
# street addresses formats (minimum requirement needed is email to
# create a new client).
@pytest.mark.client
def test_address_apt_suite_nonstandard():
    address2_list = ['!@#$', 123123, '123$!@123', '']
    for addresses in address2_list:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'address2':addresses,'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['address2'] == str(addresses) and \
               check_assert['contacts'][0]['email'] == email

#Test to see if the city field will take strings, special chars, and
# numbers (minimum requirement needed is email to create a new client).
@pytest.mark.client
def test_address_city():
    city_list = ['San Francisco', '!@#$!@', 123432, '123sanfrancisco']
    for cities in city_list:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'city':cities, 'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['city'] == str(cities) and \
               check_assert['contacts'][0]['email'] == email

#Test to see if the address will take different types of strings,
# integers, special chars (minimum requirement needed is email to
# create a new client).
@pytest.mark.client
def test_address_state_prov():
    state_list = ['CA', '12asdfadfsad', 12, '%$@#', 'C1', 'dfasfadsfdas']
    for items in state_list:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'state':items, 'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['state'] == str(items) and \
               check_assert['contacts'][0]['email'] == email

#Test to see if the postal code will take different types of strings,
# integers, special chars (minimum requirement needed is email to
# create a new client).
@pytest.mark.client
def test_address_postal_code():
    postal_codes = ['12344', 123214]
    for items in postal_codes:
        email = g.create_email(g.create_name())
        my_data = json.dumps({'state':items, 'contact':{'email':email}})
        r1 = i.post_client(my_data=my_data)
        r2 = i.get_client()
        check_assert = json.loads(r2.text)['data'][0]
        assert check_assert['state'] == str(items) and \
               check_assert['contacts'][0]['email'] == email

"""
@pytest.mark.client
def test_address_country():
    assert 1 == 2

@pytest.mark.client
def test_contacts_first_name():
    assert 1 == 2

@pytest.mark.client
def test_contacts_last_name():
    assert 1 == 2

@pytest.mark.client
def test_contacts_email():
    assert 1 == 2

@pytest.mark.client
def test_contacts_phone():
    assert 1 == 2

@pytest.mark.client
def test_additional_info_currency():
    assert 1 == 2

@pytest.mark.client
def test_additional_info_language():
    assert 1 == 2

@pytest.mark.client
def test_additional_info_payment_terms():
    assert 1 == 2

@pytest.mark.client
def test_additional_info_company_size():
    assert 1 == 2

@pytest.mark.client
def test_additional_info_industry():
    assert 1 == 2

@pytest.mark.client
def test_additional_info_private_notes():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_client():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_invoice_date():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_due_date():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_partial():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_po_num():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_discount():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_item():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_description():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_unit_cost():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_quantity():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_note_to_client():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_terms():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_footer():
    assert 1 == 2

@pytest.mark.invoices
def test_invoices_documents():
    assert 1 == 2

@pytest.mark.payments
def test_payments_client():
    assert 1 == 2

@pytest.mark.payments
def test_payments_invoice():
    assert 1 == 2

@pytest.mark.payments
def test_payments_amount():
    assert 1 == 2

@pytest.mark.payments
def test_payments_payment_type():
    assert 1 == 2

@pytest.mark.payments
def test_payments_payment_date():
    assert 1 == 2

@pytest.mark.payments
def test_payments_transaction_ref():
    assert 1 == 2

@pytest.mark.payments
def test_payments_email_payment_receipt_box():
    assert 1 == 2

@pytest.mark.tasks
def test_tasks_client():
    assert 1 == 2

@pytest.mark.tasks
def test_tasks_description():
    assert 1 == 2

"""


