import formattor
import converter

data = [
    ["JPMorganChase\n4.0\n10000+ employees\n·\nJakarta\nJPMorgan Chase is one of the world's oldest, largest and best-known financial institutions. With a history that traces our roots to 1799 in New York City, we carry forth the innovative spirit of our heritage firms in our global operations in over 60 countries. We serve millions of customers and many of the world’s most prominent corporate, institutional, and government clients-managing assets and investments, offering business advice and strategies, and providing innovative banking solutions and services. © 2023 JPMorgan Chase & Co. All rights reserved. JPMorgan Chase is an Equal Opportunity Employer, including Disability/Veterans.\n5.4K\njobs\n33.6K\nreviews\n78.3K\nsalaries"],
    ['Bank Indonesia\n4.5\n5001 to 10000 employees\n·\nJakarta\n0\njobs\n259\nreviews\n4\nsalaries']
    ]

(id, information) = formattor.company_formatting(data, company_type="demo", company_ids=0, city="jakarta")

print([information])
converter.convert([information], {}, "just trying")
