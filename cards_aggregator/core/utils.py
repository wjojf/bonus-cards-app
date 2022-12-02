from dateutil.relativedelta import relativedelta
import datetime


def isValidDateTerm(date_expiring:str):
    return date_expiring in ('1y', '3y', '5y')
    

def extractYear(date_expiring:str):
    try:
        yearAmmount = int(date_expiring.replace('y', '').strip())
    except Exception:
        yearAmmount = 0
    
    return yearAmmount


def getDateFromShortString(date_expiring:str):

    now = datetime.datetime.now()

    if not isValidDateTerm(date_expiring):
        return now
    
    yearsDelta = extractYear(date_expiring)
    
    return now + relativedelta(years=yearsDelta)


