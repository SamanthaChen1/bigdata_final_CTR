
# coding: utf-8

# In[1]:

import xlrd
wb=xlrd.open_workbook('smalltrain.xlsm')
wb.sheet_names()
sh=wb.sheet_by_index(0)
sh=wb.sheet_by_name(u'smalltrain')

# show the number of column
sh.ncols
# show the number of rows
sh.nrows


#print first_column
id1=sh.col_values(0)

click=sh.col_values(1)
hour=sh.col_values(2)
C1=sh.col_values(3)
banner_pos=sh.col_values(4)
site_id=sh.col_values(5)
site_domain=sh.col_values(6)
site_category=sh.col_values(7)
app_id=sh.col_values(8)
app_domain=sh.col_values(9)
app_category=sh.col_values(10)
device_id=sh.col_values(11)
device_ip=sh.col_values(12)
device_model=sh.col_values(13)
device_type=sh.col_values(14)
device_conn_type=sh.col_values(15)
C14=sh.col_values(16)
C15=sh.col_values(17)
C16=sh.col_values(18)
C17=sh.col_values(19)
C18=sh.col_values(20)
C19=sh.col_values(21)
C20=sh.col_values(22)
C21=sh.col_values(23)




#座標讀取某cell
cell_A1=sh.cell(0,1).value
print
assert isinstance(cell_A1, object)
cell_A1

#可用ASSIGN變數的方式,控制colx rowx數字
sh.cell(colx=0,rowx=2).value


# In[2]:

sh.cell(0,3).value


# In[3]:

import numpy as np


# In[4]:

nid1=np.unique(id1)
nclick=np.unique(click)
nhour=np.unique(hour)
nC1=np.unique(C1)
nbanner_pos=np.unique(banner_pos)
nsite_id=np.unique(site_id)
nsite_domain=np.unique(site_domain)
nsite_category=np.unique(site_category)
napp_id=np.unique(app_id)
napp_domain=np.unique(app_domain)
napp_category=np.unique(app_category)
ndevice_id=np.unique(device_id)
ndevice_ip=np.unique(device_ip)
ndevice_model=np.unique(device_model)
ndevice_type=np.unique(device_type)
ndevice_conn_type=np.unique(device_conn_type)
nC14=np.unique(C14)
nC15=np.unique(C15)
nC16=np.unique(C16)
nC17=np.unique(C17)
nC18=np.unique(C18)
nC19=np.unique(C19)
nC20=np.unique(C20)
nC21=np.unique(C21)

for i in range(100000):
    id1[i]=str(id1[i])
    i=i+1
for i in range(100000):
    click[i]=str(click[i])
    i=i+1
    
for i in range(100000):
    hour[i]=str(hour[i])
    i=i+1


# In[5]:

for i in range(100000):
    id1[i]=str(id1[i])
    i=i+1


# In[6]:

for i in range(100000):
    click[i]=str(click[i])
    i=i+1

        


# In[7]:

for i in range(100000):
    hour[i]=str(hour[i])
    i=i+1

            


# In[8]:

for i in range(100000):
    C1[i]=str(C1[i])
    i=i+1


# In[9]:

for i in range(100000):
    banner_pos[i]=str(banner_pos[i])
    i=i+1

    


# In[10]:

for i in range(100000):
    site_id[i]=str(site_id[i])
    i=i+1


# In[11]:

for i in range(100000):
    site_domain[i]=str(site_domain[i])
    i=i+1


# In[12]:

for i in range(100000):
    site_category[i]=str(site_category[i])
    i=i+1

    


# In[13]:

for i in range(100000):
    app_id[i]=str(app_id[i])
    i=i+1


# In[14]:

for i in range(100000):
    app_domain[i]=str(app_domain[i])
    i=i+1


# In[15]:

for i in range(100000):
    app_category[i]=str(app_category[i])
    i=i+1


# In[16]:

for i in range(100000):
    device_ip[i]=str(device_ip[i])
    i=i+1


# In[16]:




# In[17]:

for i in range(100000):
    device_id[i]=str(device_id[i])
    i=i+1


# In[18]:

for i in range(100000):
    device_model[i]=str(device_model[i])
    i=i+1


# In[19]:

for i in range(100000):
    device_type[i]=str(device_type[i])
    i=i+1


# In[20]:

for i in range(100000):
    device_conn_type[i]=str(device_conn_type[i])
    i=i+1


# In[21]:

for i in range(100000):
    C14[i]=str(C14[i])
    i=i+1


# In[22]:

for i in range(100000):
    C15[i]=str(C15[i])
    i=i+1


# In[23]:

for i in range(100000):
    C16[i]=str(C16[i])
    i=i+1


# In[24]:

for i in range(100000):
    C17[i]=str(C17[i])
    i=i+1


# In[25]:

for i in range(100000):
    C18[i]=str(C18[i])
    i=i+1


# In[26]:

for i in range(100000):
    C19[i]=str(C19[i])
    i=i+1


# In[27]:

for i in range(100000):
    C20[i]=str(C20[i])
    i=i+1


# In[28]:

for i in range(100000):
    C21[i]=str(C21[i])
    i=i+1


# In[177]:

R=np.mat(np.zeros([4,np.size(nC1)]))
for j in range(np.size(nC1)):
    x1=0
    x2=0
    for i in range(100000):
        if C1[i]==nC1[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_C1=0
for j in range(np.size(nC1)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_C1=entropy_C1+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_C1


    
    
    


# In[180]:

R=np.mat(np.zeros([4,np.size(nhour)]))
for j in range(np.size(nhour)):
    x1=0
    x2=0
    for i in range(100000):
        if hour[i]==nhour[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_hour=0
for j in range(np.size(nhour)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_hour=entropy_hour+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_hour


# In[ ]:

R=np.mat(np.zeros([4,np.size(nid1)]))
for j in range(np.size(nid1)):
    x1=0
    x2=0
    for i in range(100000):
        if id1[i]==nid1[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_id1=0
for j in range(np.size(id1)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_id1=entropy_id1+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_id1


# In[ ]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[128]:

R=np.mat(np.zeros([4,np.size(nsite_domain)]))
for j in range(np.size(nsite_domain)):
    x1=0
    x2=0
    for i in range(100000):
        if site_domain[i]==nsite_domain[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_site_domain=0
for j in range(np.size(nsite_domain)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_site_domain=entropy_site_domain+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_site_domain


# In[ ]:

R=np.mat(np.zeros([4,np.size(nsite_category)]))
for j in range(np.size(nsite_category)):
    x1=0
    x2=0
    for i in range(100000):
        if site_category[i]==nsite_category[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_site_category=0
for j in range(np.size(nsite_category)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_site_category=entropy_site_category+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_site_category


# In[137]:

R=np.mat(np.zeros([4,np.size(napp_domain)]))
for j in range(np.size(napp_domain)):
    x1=0
    x2=0
    for i in range(100000):
        if app_domain[i]==napp_domain[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_app_domain=0
for j in range(np.size(napp_domain)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_app_domain=entropy_app_domain+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_app_domain


# In[94]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[145]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[144]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[146]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[148]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[149]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos


# In[ ]:

R=np.mat(np.zeros([4,np.size(nbanner_pos)]))
for j in range(np.size(nbanner_pos)):
    x1=0
    x2=0
    for i in range(100000):
        if banner_pos[i]==nbanner_pos[j] :
            if click[i]=='1.0':
                x1=x1 +1
            if click[i]=='0.0':
                x2=x2 +1
            R[0,j]=x1
            R[1,j]=x2
            R[2,j]=x1+x2
            if x1+x2 !=0:
                R[3,j]=float(x1)/(x1+x2)
            else:
                R[3,j]=2
entropy_banner_pos=0
for j in range(np.size(nbanner_pos)) :
    if R[3,j]<=1 and R[3,j]>0:
        entropy_banner_pos=entropy_banner_pos+R[2,j]*np.log2(R[3,j])*(-1.0/99999)
print entropy_banner_pos

