new_url = ""
with open('urls.txt', 'r') as url_data:
    urls = url_data.readlines()
    
# with open("url_corrected.txt", "w") as write_data:
#     for url in urls:
#         splitted_url = url.split(":")
#         first_part, second_part = splitted_url
#         first_part = first_part[:4]
#         second_part = "/"+second_part
#         new_url = first_part+":"+second_part
#         write_data.write(new_url)
        

with open("url_corrected.txt", "w") as write_data:
    for url in urls:
        url_remove_s = url.replace("s", "", 1)
        url_remove_s_add_slash = url_remove_s[:6]+"/"+url_remove_s[6:]
        write_data.write(url_remove_s_add_slash)
