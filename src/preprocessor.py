
# coding: utf-8

# In[8]:

import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder


# In[9]:

def fill_missing_data():
    return "not implemented"

def preprocess_data(data, labels):
    review_info = {'revisionId':int}
    
    #content features (27 features)
    character_features = {'groupId':float, 'itemId':float, 'alphanumericRatio':float,'asciiRatio':float,'bracketRatio':float,'digitRatio':float
                    ,'latinRatio':float,'longestCharacterSequence':float,'lowerCaseRatio':float
                    ,'nonLatinRatio':float,'punctuationRatio':float,'upperCaseRatio':float,'whitespaceRatio':float}    
    word_features = {'languageWordRatio':float, 'containsLanguageWord':bool, 'lowerCaseWordRatio':float, 
                     'longestWord':float, 'containsURL':bool, 'badWordRatio':float, 'proportionOfQidAdded':float, 
                     'upperCaseWordRatio':float, 'proportionOfLinksAdded':float}
    sentence_features = {'commentCommentSimilarity':float, 'commentLabelSimilarity':float, 'commentTailLength':float
                         ,'commentSitelinkSimilarity':float}
    statement_features = {'propertyFrequency':float, 'itemValueFrequency':float, 'literalValueFrequency':float}
    
    #contextual features (20 features)
    user_features = {'isPrivilegedUser':bool, 'isRegisteredUser':bool, 'isBotUser':bool}

    #TODO need to fins mapping column names for the following user features
    #'cumUserUniqueItems':float, 'userFrequency':float
            
    user_cat_features = [ 'userCity', 'userContinent', 'userCountry', 'userCounty', 'userRegion', 'userTimeZone']
    item_features = {'logCumItemUniqueUsers':float, 'logItemFrequency':float}
    revision_features = {'isLatinLanguage':bool, 'commentLength':float}
    revision_cat_features = ['revisionTag', 'revisionLanguage', 'revisionAction', 'revisionSubaction',
                             'positionWithinSession']
        
    print("number of rows: %d"%data.shape[0])
    print("number of feaure columns: %d"%data.shape[1]) 
    
    cat_features = []
    cat_features.extend(user_cat_features)
    cat_features.extend(revision_cat_features)
    
    numerical_features = {}
    numerical_features.update(review_info)
    numerical_features.update(character_features)
    numerical_features.update(word_features)
    numerical_features.update(sentence_features)
    #numerical_features.update(statement_features) 
    numerical_features.update(user_features)
    #numerical_features.update(item_features)
    numerical_features.update(revision_features)

    selected_feature_list = []
    selected_feature_list.extend(numerical_features.keys())
    selected_feature_list.extend(cat_features)

    #numerical fields with '�' are replaced with -1 
    selected_data = data[selected_feature_list]
    
    #TODO replace missing values with a better approximation (ie: median)
    selected_data = selected_data.replace(['�', 'NA'], -1, inplace=False)

    for col in numerical_features.keys():
        selected_data[col] = selected_data[col].astype(numerical_features[col])

    #replacing nan with -1
    selected_data.loc[:,list(numerical_features.keys())] = selected_data.loc[:,list(numerical_features.keys())].fillna(-1,inplace=False) 
    
    for col in cat_features:
        #print(col)
        selected_data[col] = selected_data[col].astype(str)
        
    #converting categorical variables into numerica lists
    le = LabelEncoder()
    #TODO pickle these columns

    for col in cat_features:
        #print(col)
        selected_data[col] = le.fit_transform(selected_data[col])
        
    return selected_data


# In[11]:

features_file = "/home/kaushalya/Coding/wsdm_cup/vandalism/data/features100k.csv"
output_file = "/home/kaushalya/Coding/wsdm_cup/vandalism/data/features100k_preprocessed_new.csv"


# In[13]:

if __name__ == "__main__":
    #reading data
    data = pd.read_csv(features_file, encoding='utf-8',
                       header=0)
    labeled_data = pd.read_csv(labeled_data_file, encoding='utf-8', header=0)
    preprocessed_data = preprocess_data(data, labeled_data)
    
    preprocessed_data.to_csv(output_file)


# In[15]:

preprocessed_data.to_csv(output_file)


# In[ ]:



