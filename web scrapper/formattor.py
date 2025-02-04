import converter

def splitter(text, split_parameter):
    return text.split(split_parameter)

#return current company ids
def company_formatting(page, company_type, company_ids, city):
    information = {
        "companyId" : [],
        "companyName" : [],
        "companyRating" : [],
        "companyEmployees" : [],
        "companyLocation" : [],
        "companyDescription" : [],
        "companyType" : []
        }
    
    keys_list = list(information.keys())
    
    #untuk setiap kumpulan company disetiap page
    for page_content in page:
        #untuk setiap content di page_content
        for content in page_content:

            #pisahkan setiap 
            data = splitter(content, "\n")
        
            #jika ada beberapa lokasinya di jakarta
            keys_index = 1
            information[keys_list[0]].append("company_" + str(company_ids))
            information[keys_list[4]].append(city)
            company_ids += 1
            if(len(data) > 11):
                for i in range(len(data[:-6])):
                    if(i == 4):
                        keys_index += 1
                        continue
                    elif(i == 3):
                        continue
                    information[keys_list[keys_index]].append(data[i])
                    keys_index += 1
                information[keys_list[len(keys_list) - 1]].append(company_type)
            else:
                for i in range(len(data[:-6])):
                    if(i == 4):
                        keys_index += 1
                        continue
                    elif(i == 3):
                        continue
                    elif(i == 5):
                        information[keys_list[5]].append(".")
                        keys_index += 1
                        continue
                    information[keys_list[keys_index]].append(data[i])
                    keys_index += 1
                information[keys_list[len(keys_list) - 1]].append(company_type)

    return (company_ids, information)


