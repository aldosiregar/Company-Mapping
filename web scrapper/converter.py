import pandas as pd

#ubah dictionary menjadi dataframe
def convert_to_dataframe(dictionary):
    df = pd.DataFrame.from_dict(dictionary, orient='index')
    df = df.transpose()
    return df

def convert_to_excel(dataframe, filename):
    dataframe.to_excel(filename)

#change_format : change data in dataframe into certain format
def convert(data=[], change_format={}, filename=""):
    for i in range(len(data)):
        data[i] = convert_to_dataframe(data[i])

    concated = pd.concat(data, ignore_index=True)
    changtype = change_format
    concated = concated.astype(changtype)

    convert_to_excel(concated, "./../data/" + filename + ".xlsx")