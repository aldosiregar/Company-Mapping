import scrapper
import formattor
import converter

#link dari setiap industri
links = [
    "https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1045&locType=M&locName=Jakarta&sector=10013&page=1&overall_rating_low=4",
    "https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1045&locType=M&locName=Jakarta&industry=200048&page=1&overall_rating_low=4",
    "https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1045&locType=M&locName=Jakarta&industry=200001&page=1&overall_rating_low=4",
    "https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1045&locType=M&locName=Jakarta&industry=200022&page=1&overall_rating_low=4",
    "https://www.glassdoor.com/Explore/browse-companies.htm?filterType=RATING_OVERALL&locId=1045&locType=M&locName=Jakarta&industry=200130&page=1&overall_rating_low=4",
]

#tipe industri yang ditekuni perusahaan
company_type = [
    "Information Technology",
    "Banking & Lending",
    "Accounting & Tax",
    "Advertising & Public Relasion",
    "Shipping & Trucking"
]

#xpath untuk setiap button next pada company profile
next_xpath = [
    "/html/body/div[1]/div[5]/div/div/div[3]/div[12]/nav/ol/li[9]/button",
    "/html/body/div[1]/div[5]/div/div/div[3]/div[12]/nav/ol/li[6]/button",
    "/html/body/div[1]/div[5]/div/div/div[3]/div[12]/nav/ol/li[5]/button",
    "/html/body/div[1]/div[5]/div/div/div[3]/div[12]/nav/ol/li[9]/button",
    None
]

#id company yang akan digunakan untuk membuat primary key
company_id = 0

#list dari bidang company
company_industries = []

#data yang nanti akan disimpan ke database
database = []

#untuk setiap link didalam list links
for i in range(len(links)):
    company_industries.append(scrapper.scrap_data(links[i], next_xpath[i]))

#untuk setiap index didalam company_type, sekaligus digunakan indexnya pada company_industries
for i in range(len(company_type)):
    #company id akan digunakan pada iterasi selanjutnya, sedangkan information berisi 
    #dict dari sekumpulan perusahaan dengan industri yang berbeda
    id, information = formattor.company_formatting(company_industries[i], company_type[i], company_id, "Jakarta")
    company_id = id
    #simpan sekumpulan list pada list database, nantinya akan digambungkan ke dataframe
    #baru disimpan ke database
    database.append(information)

converter.convert(database, {"companyRating" : float}, "companiesData")