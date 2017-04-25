##
 # @file   : NISTFund.py
 # @brief  : Fundamental Constants and official units conversions directly scraped from NIST (National Institute of Standards and Technology) website.  
 # Build the most current and accurate copy, directly from the NIST website, of a table of fundamental constants and unit conversions 
 # and have the values ready to use in Python.  
 # @author : Ernest Yeung	ernestyalumni@gmail.com
 # @date   : 20170423
 # 
 # If you find this code useful, feel free to donate directly and easily at this direct PayPal link: 
 # 
 # https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ernestsaveschristmas%2bpaypal%40gmail%2ecom&lc=US&item_name=ernestyalumni&currency_code=USD&bn=PP%2dDonationsBF%3abtn_donateCC_LG%2egif%3aNonHosted 
 # 
 # which won't go through a 3rd. party such as indiegogo, kickstarter, patreon.  
 # Otherwise, I receive emails and messages on how all my (free) material on 
 # physics, math, and engineering have helped students with their studies, 
 # and I know what it's like to not have money as a student, but love physics 
 # (or math, sciences, etc.), so I am committed to keeping all my material 
 # open-source and free, whether or not 
 # sufficiently crowdfunded, under the open-source MIT license: 
 # 	feel free to copy, edit, paste, make your own versions, share, use as you wish.  
 #  Just don't be an asshole and not give credit where credit is due.  
 # Peace out, never give up! -EY
 ## 
 
## Screen scraping i.e. web scraping with Beautiful Soup (BS) and requests  

import os

import urllib2
import re
import decimal
from decimal import Decimal

import pandas as pd

import requests
from bs4 import BeautifulSoup as BS

############################################################
## NIST - National Institute of Standards and Technology
############################################################

class scraped_BS(object):
    """
    scraped_BS
    scraped_BS is a class so we can have, as an object, all that results from scraping 
    with requests and BeautifulSoup (BS)
    
    Example of Usage:
    python -i scrape_BS.py
    >>> mainNISTcuu = scraped_BS(NISTCUU_URL)
    >>> NISTconvBS  = scraped_BS(NISTCONValpha)
    """
    def __init__(self,url):
        self.url  = url
        self.req  = requests.get(url)
        self.soup = BS(self.req.content) 
        self.req.close()

#################################################################
## NIST Reference on Constants, Units, and Uncertainty mainpage
# only imports needed so far are
##  urllib2, re, Decimal
#################################################################

FPCascii    = "http://physics.nist.gov/cuu/Constants/Table/allascii.txt" # Fundamental Physical Constants

#####
# On looking at mainNISTcuu.soup.find_all("a") and your favorite Web Inspector of the 
# NIST cuu webpage, NISTCUU_URL, one realizes that to get to Frequently Used Constants 
# or All values, one does a query.  Let's grab all values in ascii.  
# Do this with FPCasciitbl = scraped_BS(FPCascii) if you want to use requests
# Do this with urllib2 as follows, using urllib
#####

def retrieve_file(url=FPCascii,filename="allascii.txt"):
    if not os.path.exists('./rawdata/'):
		os.makedirs('./rawdata/')
    with open('./rawdata/'+filename,'wb') as targetfile:
        u = urllib2.urlopen(url) 
        targetfile.write(u.read())
        targetfile.close()
    return u

####################
# At this point, running retrieve_file() should put allascii.txt into the rawdata subdirectory
# You can open up allascii.txt and see you have all the Fundamental Physical Constants (!!!)
# Time to parse this table:
####################

def line_reading(filename='./rawdata/allascii.txt'):
	""" line_reading - needed for scraping_allascii Python function, below
	"""
	openedfile = open(filename,'rb')
	lines = openedfile.read().splitlines()
	lines = [line for line in lines if line != '']
	return lines

def scraping_allascii(filename='./rawdata/allascii.txt'):
    lines  = line_reading(filename)
    title  = lines[0].strip()
    src    = lines[1].strip()
    header = lines[2].split()

    # cf. http://stackoverflow.com/questions/12866631/python-split-a-string-with-at-least-2-whitespaces for re
    rawtbl = []
    for line in lines[4:]:
        rawtbl.append( re.split(r'\s{2,}', line) )
    tbl = []
    for rawline in rawtbl:
        line = []
        line.append(rawline[0])
        try:
            line.append(Decimal(rawline[1].replace(" ","")))
        except decimal.InvalidOperation:
            value = rawline[1].replace(" ","")
            value = ''.join( re.split(r'[.]{2,}',value))
            line.append( Decimal(value) )
        try:
            line.append(Decimal(rawline[2].replace(" ","")))
        except decimal.InvalidOperation:
            line.append(None)
        line.append(rawline[3])
        tbl.append(line)

    return lines, title, src, header, rawtbl, tbl

###########################################################################
# Now you should be able to put this into your favorite database of choice
###########################################################################

###################################
#### Preprocessing for Pandas
###   From a list
###################################
def init_FundConst(subdir='./rawdata/'):
	if os.path.isfile( subdir + 'allascii.txt'):
		lines,title,src,header,rawtbl,tbl=scraping_allascii()
		FundConst = pd.DataFrame(tbl,columns=header)
		return FundConst
	else:
		retrieve_file()
		lines,title,src,header,rawtbl,tbl=scraping_allascii()
		FundConst = pd.DataFrame(tbl,columns=header)
		return FundConst


###############################################################################################
# NIST Official conversions
# from http://physics.nist.gov/cuu/Reference/unitconversions.html
# Appendix Bof NIST Special Publication 811
# are the official values of conversion factors
###############################################################################################
##################################################
### NIST Guide to SI
## B.8 Factors for Units Listed Alphabetically
#### BeautifulSoup is needed 

NISTCONValphabetical = "https://www.nist.gov/physical-measurement-laboratory/nist-guide-si-appendix-b8"

def make_alphabeticalconv_lst(url=NISTCONValphabetical ):
    """ make_alphabeticalconv_lst - makes alphabetical conversion list
		
    make_alphabeticalconv_lst is needed for make_pd_alphabeticalconv_lst
    """
    convBS = scraped_BS(url)
    convBS.convtbls = convBS.soup.find_all("table")
    convdata = []
    convdata2 = []

    headers = convBS.convtbls[0].find_all('tr')[1].find_all('th')
    headers = [ele.text.replace(' ','') for ele in headers]

    for tbl in convBS.convtbls:
        for row in tbl.find_all('tr'):
            if row.find_all('td') != []:
                if row.text != '':
                    rowsplit = row.text.replace("\n",'',1).split('\n')
                    try:
                        rowsplit = [pt.replace(u'\xa0',u' ').strip() for pt in rowsplit]
                    except UnicodeDecodeError as err:
                        print rowsplit
                        Break
                        raise err
                    convdata.append( rowsplit )
                    if len(row.find_all('td')) == (len(headers)+1):
                        convdata2.append( row.find_all('td'))
    convdata3 = []
    for row in convdata2:
        rowout = []
        rowout.append( row[0].text.strip())
        rowout.append( row[1].text.strip())
        value = (row[2].text+row[3].text).strip().replace(u'\xa0',' ').replace(u'\n',' ').replace(' ','')
        
        rowout.append(Decimal( value ))
        convdata3.append(rowout)
    convdata2 = convdata3
                        
    return headers, convdata, convdata2

def make_pd_alphabeticalconv_lst(subdir='./rawdata/',filename="DF_alphabeticalconv"):
    """
    make_pd_alphabeticalconv_lst
    
    DESCRIPTION
    run make_pd_alphabeticalconv_1st first to put the panda DataFrame saved locally
    """
    headers,convdata,convdata2 = make_alphabeticalconv_lst()
    DF_conv = pd.DataFrame(convdata2,columns=headers)
    DF_conv.to_pickle(subdir +filename) 
    return DF_conv

## Dealing with Appendix B.9: Factor for units listed by kind of quantity or field of science

NISTCONVURL = "https://www.nist.gov/pml/nist-guide-si-appendix-b9-factors-units-listed-kind-quantity-or-field-science"


def make_conv_lst(url=NISTCONVURL):
	""" make_conv_lst 
	"""
	convBS = scraped_BS(url)
	convBS.convtbls = convBS.soup.find_all("table")
	convdata = []
	convdata2 = []
    
	headers = convBS.convtbls[1].find_all('tr')[1].find_all('th')
	headers = [ele.text.replace(' ','') for ele in headers]

	headers.append("kind")

	for tbl in convBS.convtbls[1:]:
		field_of_science = ""
		for row in convBS.convtbls[1].find_all('tr'):
			if row.find_all('td') != []:
				if row.text != '':
					rowsplit = row.text.split('\n')
					if u'' in rowsplit:
						rowsplit.remove(u'')
					if len(rowsplit) is 1:
						field_of_science = rowsplit[0]
					elif field_of_science is not "":
						rowsplit.append(field_of_science)
						convdata.append(rowsplit)
						if len(row.find_all('td')) is len(headers):
							convdata2.append( rowsplit ) 
	
	convdata3 = []
	for row in convdata2:
		rowout = []
		rowout.append( row[0]  )
		rowout.append( row[1]  )

		value = (row[2] + row[3]).strip().replace(u'\xa0',' ').replace(u'\n',' ').replace(' ','')
		
		rowout.append(Decimal(value))
		rowout.append( row[4] )
		convdata3.append(rowout)

	print("This is what happens when I test the length of convdata and convdata2: ")
	print( len(convdata) == len(convdata2) )
	print( len(convdata) )
	print( len(convdata2) )
	return headers, convdata2, convdata3

def make_pd_conv_lst(subdir='./rawdata/',filename="DF_conv"):
    """
    make_pd_alphabeticalconv_lst
    
    DESCRIPTION
    run make_pd_alphabeticalconv_1st first to put the panda DataFrame saved locally
    """
    headers,convdata,convdata2 = make_conv_lst()
    DF_conv = pd.DataFrame(convdata2,columns=headers)
    DF_conv.to_pickle( subdir +filename) 
    return DF_conv

