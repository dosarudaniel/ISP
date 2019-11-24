from bs4 import BeautifulSoup
import requests

import time;

url = "https://prezenta.bec.ro/prezidentiale24112019/data/presence/json/presence_SR_now.json?_="


now = time.time()
struct_time = time.gmtime(now)

romanian_hour = struct_time.tm_hour + 2
romanian_min = struct_time.tm_min
romanian_sec = struct_time.tm_sec

response = requests.get(url+str(int(now)))

json_data = response.json()
counties = json_data["county"]

total_voturi_tara = 0
total_voturi_strainatate = 0
total_voturi_18_24 = 0
total_voturi_25_34 = 0
total_voturi_35_44 = 0
total_voturi_45_64 = 0
total_voturi_65_plus = 0

total_voturi_18_24_ab = 0
total_voturi_25_34_ab = 0
total_voturi_35_44_ab = 0
total_voturi_45_64_ab = 0
total_voturi_65_plus_ab = 0

for i in range(43):
    if i != 35:
        total_voturi_tara += counties[i]['LT']
        total_voturi_18_24 += counties[i]['age_ranges']['men_18_24']
        total_voturi_18_24 += counties[i]['age_ranges']['women_18_24']
        total_voturi_25_34 += counties[i]['age_ranges']['men_25_34']
        total_voturi_25_34 += counties[i]['age_ranges']['women_25_34']
        total_voturi_35_44 += counties[i]['age_ranges']['men_35_44']
        total_voturi_35_44 += counties[i]['age_ranges']['women_35_44']
        total_voturi_45_64 += counties[i]['age_ranges']['men_45_64']
        total_voturi_45_64 += counties[i]['age_ranges']['women_45_64']
        total_voturi_65_plus += counties[i]['age_ranges']['men_65+']
        total_voturi_65_plus += counties[i]['age_ranges']['men_65+']
    else:
        total_voturi_strainatate += counties[i]['LT']
        total_voturi_18_24_ab += counties[i]['age_ranges']['men_18_24']
        total_voturi_18_24_ab += counties[i]['age_ranges']['women_18_24']
        total_voturi_25_34_ab += counties[i]['age_ranges']['men_25_34']
        total_voturi_25_34_ab += counties[i]['age_ranges']['women_25_34']
        total_voturi_35_44_ab += counties[i]['age_ranges']['men_35_44']
        total_voturi_35_44_ab += counties[i]['age_ranges']['women_35_44']
        total_voturi_45_64_ab += counties[i]['age_ranges']['men_45_64']
        total_voturi_45_64_ab += counties[i]['age_ranges']['women_45_64']
        total_voturi_65_plus_ab += counties[i]['age_ranges']['men_65+']
        total_voturi_65_plus_ab += counties[i]['age_ranges']['women_65+']

prezenta_tara = total_voturi_tara/18217411 * 100
prezenta_total = (total_voturi_tara+total_voturi_strainatate)/18217411 * 100

print("Ora României         " + str(romanian_hour) + ":" + str(romanian_min) + ":" + str(romanian_sec))
print("Prezenţă România   ============= {0:.2f} %\n".format(round(prezenta_tara, 2)))
print("Total Voturi în Ro = " + "{:,}".format(total_voturi_tara))
print("Străinătate        = " + "  {:,}".format(total_voturi_strainatate))
print("Prezenţă Total     ============= {0:.2f} %".format(round(prezenta_total, 2)))

print("\nVoturi pe categorii de vârstă în România: ")
print("18-24 : " + "  {:,} -".format(total_voturi_18_24) + " prezenta: {0:.2f} %".format(round(total_voturi_18_24*100/1614567, 2)))
print("25-34 : " + "{:,} -".format(total_voturi_25_34)+ " prezenta: {0:.2f} %".format(round(total_voturi_25_34*100/3141395, 2)))
print("35-44 : " + "{:,} -".format(total_voturi_35_44) + " prezenta: {0:.2f} %".format(round(total_voturi_35_44*100/3576480, 2)))
print("45-64 : " + "{:,} -".format(total_voturi_45_64) + " prezenta: {0:.2f} %".format(round(total_voturi_45_64*100/6082477, 2)))
print("65+   : " + "{:,} -".format(total_voturi_65_plus) + " prezenta: {0:.2f} %".format(round(total_voturi_65_plus*100/3739491, 2)))

print("\nVoturi pe categorii de vârstă în afara ţării: ")
print("18-24 : " + " {:,} -".format(total_voturi_18_24_ab) + " prezenta: {0:.2f} %".format(round(total_voturi_18_24_ab*100/1614567, 2)))
print("25-34 : " + "{:,} -".format(total_voturi_25_34_ab)+ " prezenta: {0:.2f} %".format(round(total_voturi_25_34_ab*100/3141395, 2)))
print("35-44 : " + "{:,} -".format(total_voturi_35_44_ab) + " prezenta: {0:.2f} %".format(round(total_voturi_35_44_ab*100/3576480, 2)))
print("45-64 : " + "{:,} -".format(total_voturi_45_64_ab) + " prezenta: {0:.2f} %".format(round(total_voturi_45_64_ab*100/6082477, 2)))
print("65+   : " + " {:,} -".format(total_voturi_65_plus_ab) + " prezenta: {0:.2f} %".format(round(total_voturi_65_plus_ab*100/3739491, 2)))


print("\nVoturi pe categorii de vârstă în total: ")
print("18-24 : " + "  {:,} -".format(total_voturi_18_24 + total_voturi_18_24_ab) + " prezenta: {0:.2f} %".format(round((total_voturi_18_24 + total_voturi_18_24_ab)*100/1614567, 2)))
print("25-34 : " + "{:,} -".format(total_voturi_25_34 + total_voturi_25_34_ab)+ " prezenta: {0:.2f} %".format(round((total_voturi_25_34 + total_voturi_25_34_ab)*100/3141395, 2)))
print("35-44 : " + "{:,} -".format(total_voturi_35_44 + total_voturi_35_44_ab) + " prezenta: {0:.2f} %".format(round((total_voturi_35_44+ total_voturi_35_44_ab)*100/3576480, 2)))
print("45-64 : " + "{:,} -".format(total_voturi_45_64 + total_voturi_45_64_ab) + " prezenta: {0:.2f} %".format(round((total_voturi_45_64 + total_voturi_45_64_ab) * 100/6082477, 2)))
print("65+   : " + "{:,} -".format(total_voturi_65_plus + total_voturi_65_plus_ab) + " prezenta: {0:.2f} %".format(round((total_voturi_65_plus + total_voturi_65_plus_ab)*100/3739491, 2)))
