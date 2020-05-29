#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd 


# In[2]:


dt = pd.read_csv("wines.csv")


# In[3]:


dt.head()


# In[4]:


y = dt['Class']

y_cat = pd.get_dummies(y)


# In[5]:


X = dt.drop('Class' , axis=1)


# In[6]:


from keras.models import Sequential


# In[7]:


model  =  Sequential()


# In[8]:


from keras.layers import Dense


# In[9]:


model.add(Dense(units=5 , input_shape=(13,), 
                activation='relu'))


# In[10]:


model.add(Dense(units=10 , 
                activation='relu', 
                kernel_initializer='he_normal' ))


# In[11]:


model.add(Dense(units=7, 
                activation='relu', 
                kernel_initializer='he_normal' ))


# In[12]:


model.add(Dense(units=3, activation='softmax'))


# In[13]:


from keras.optimizers import adam

model.compile(optimizer=adam(learning_rate=0.01),  
              loss='categorical_crossentropy',
             metrics=['accuracy']
             )


# In[14]:


a = model.fit(X,y_cat, epochs=200)


# In[15]:


a = model.fit(X,y_cat, epochs=200)


# In[16]:


acc = a.history["accuracy"]


# In[17]:


acc_= acc[199]


# In[18]:


ad=acc_.reshape(1,1)


# In[19]:


import numpy
numpy_loss_history = ad
numpy.savetxt("acc.txt", numpy_loss_history , fmt='%1.4f')

