# -*- coding: utf-8 -*-
# import sitedb
import xlrd
import urllib
import datetime
import dbclasses.dbobj
import dbclasses.dbworker
import sett

dbclasses.dbworker.cred = dbclasses.dbworker.loadmysqlcredential(sett)


def load_from_ars():
    rb = xlrd.open_workbook('PRICE_ARS.XLS', formatting_info=True)
    sheet = rb.sheet_by_index(0)
    sql = "delete from prices where synctag = 'from ars' and id <> ''"
    db = dbclasses.dbworker.getcon()
    cursor = db.cursor()
    cursor.execute(sql)
    db.commit()
    dt_now = datetime.datetime.now()
    dt_for_db = dt_now.strftime('%Y-%m-%d %H:%M:%S')
    org = dbclasses.dbobj.objects["organization"]()
    org.find(caption="ezsp")
    pos = 0
    for i in range(31, sheet.nrows - 30):
        currency = sheet.cell(i, 2).value
        if not (currency == ''):
            if type(currency) != float:
                currency = float(currency.replace(',', '.'))
            pr = sheet.cell(i, 3).value
            if pr != '':
                if type(pr) != float:
                    pr = float(pr.replace(',', '.'))
                if currency > pr:
                    pos += 1
                    newprice = dbclasses.dbobj.objects["prices"]()
                    newprice.caption = sheet.cell(i, 1).value
                    newprice.fantastic_url = urllib.parse.quote(sheet.cell(i, 1).value)
                    newprice.synctag = "from ars"
                    newprice.organization = org.id
                    newprice.vat = 18
                    newprice.insearch = True
                    newprice.price_in = pr
                    newprice.price = round((currency-pr)*0.75+pr, 2)
                    newprice.write()
                    addfld = dbclasses.dbobj.objects["properties"]()
                    addfld.priceref = newprice.id
                    addfld.caption = "код прайса Арсенал+"
                    addfld.value = sheet.cell(i, 0).value
                    addfld.write()
                    if (pos % 200) == 0:
                        print("Complate {p}".format(p=pos))
    print("Loading {p} complate, from {lines}".format(p=pos, lines=sheet.nrows))


load_from_ars()
