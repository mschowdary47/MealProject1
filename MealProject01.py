#!/usr/bin/env python
# coding: utf-8

# In[1]:


#connection to MongoDB Instance
import pymongo
client=pymongo.MongoClient()

client=pymongo.MongoClient('localhost',27017)

client.list_database_names()

local_db=client['local']

#collections
local_db.list_collection_names()

collection=local_db.startup_log


# In[2]:


document=[{"meal_id":1885,"category":"Beverages","cuisine":"Thai"},{"meal_id":1993,"category":"Beverages","cuisine":"Thai"},{"meal_id":2539,"category":"Beverages","cuisine":"Thai"},{"meal_id":1248,"category":"Beverages","cuisine":"Indian"},{"meal_id":2631,"category":"Beverages","cuisine":"Indian"},{"meal_id":1311,"category":"Extras","cuisine":"Thai"},{"meal_id":1062,"category":"Beverages","cuisine":"Italian"},{"meal_id":1778,"category":"Beverages","cuisine":"Italian"},{"meal_id":1803,"category":"Extras","cuisine":"Thai"},{"meal_id":1198,"category":"Extras","cuisine":"Thai"},{"meal_id":2707,"category":"Beverages","cuisine":"Italian"},{"meal_id":1847,"category":"Soup","cuisine":"Thai"},{"meal_id":1438,"category":"Soup","cuisine":"Thai"},{"meal_id":2494,"category":"Soup","cuisine":"Thai"},{"meal_id":2760,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2490,"category":"Salad","cuisine":"Italian"},{"meal_id":1109,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":2290,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1525,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":2704,"category":"Other Snacks","cuisine":"Thai"},{"meal_id":1878,"category":"Starters","cuisine":"Thai"},{"meal_id":2640,"category":"Starters","cuisine":"Thai"},{"meal_id":2577,"category":"Starters","cuisine":"Thai"},{"meal_id":1754,"category":"Sandwich","cuisine":"Italian"},{"meal_id":1971,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2306,"category":"Pasta","cuisine":"Italian"},{"meal_id":2139,"category":"Beverages","cuisine":"Indian"},{"meal_id":2826,"category":"Sandwich","cuisine":"Italian"},{"meal_id":2664,"category":"Salad","cuisine":"Italian"},{"meal_id":2569,"category":"Salad","cuisine":"Italian"},{"meal_id":1230,"category":"Beverages","cuisine":"Continental"},{"meal_id":1207,"category":"Beverages","cuisine":"Continental"},{"meal_id":2322,"category":"Beverages","cuisine":"Continental"},{"meal_id":2492,"category":"Desert","cuisine":"Indian"},{"meal_id":1216,"category":"Pasta","cuisine":"Italian"},{"meal_id":1727,"category":"Rice Bowl","cuisine":"Indian"},{"meal_id":1902,"category":"Biryani","cuisine":"Indian"},{"meal_id":1247,"category":"Biryani","cuisine":"Indian"},{"meal_id":2304,"category":"Desert","cuisine":"Indian"},{"meal_id":1543,"category":"Desert","cuisine":"Indian"},{"meal_id":1770,"category":"Biryani","cuisine":"Indian"},{"meal_id":2126,"category":"Pasta","cuisine":"Italian"},{"meal_id":1558,"category":"Pizza","cuisine":"Continental"},{"meal_id":2581,"category":"Pizza","cuisine":"Continental"},{"meal_id":1962,"category":"Pizza","cuisine":"Continental"},{"meal_id":1571,"category":"Fish","cuisine":"Continental"},{"meal_id":2956,"category":"Fish","cuisine":"Continental"},{"meal_id":2104,"category":"Fish","cuisine":"Continental"},{"meal_id":2444,"category":"Seafood","cuisine":"Continental"},{"meal_id":2867,"category":"Seafood","cuisine":"Continental"},{"meal_id":1445,"category":"Seafood","cuisine":"Continental"}]


# In[3]:


result=collection.insert_many(document)


# In[4]:


#insert ID'S
inserted_IDs=result.inserted_ids
for unique_id in inserted_IDs:
          print(unique_id)


# In[5]:


print(unique_id)


# In[7]:


#find
local_db.list_collection.find()


# In[8]:


#delete_one
local_db.list_collection.delete_one({"meal_id":1885,"category":"Beverages","cuisine":"Thai"})


# In[10]:


#delet_many

local_db.list_collection.delete_many({"meal_id":1993,"category":"Beverages","cuisine":"Thai"})


# In[17]:


#update
query = {"address":"Ap"}
Values = {"$set":{"address":"nlr"}}
local_db.list_collection.update_one(query,Values)


# In[39]:


#limit

#limit
for i in local_db.list_collection.find().limit(5):
    print(i)


# In[40]:


#Count
local_db.list_Collection.count_documents


# In[41]:


#sorting data
local_db.list_collection.find().sort("_id",0)


# In[42]:


#drop
local_db.list_collection.drop()


# In[ ]:




