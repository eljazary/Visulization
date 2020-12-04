#!/usr/bin/env python
# coding: utf-8

# # (LoansDataset )
# ## by (Mohamed Gamal )
# 
# ## Preliminary Wrangling
# 
# > prosper is a website for mangment and awards loans for borrowers 

# In[1]:


# import all packages and set plots to be embedded inline
import numpy as np
import pandas as pd
import io 
import matplotlib.pyplot as plt
import seaborn as sb
get_ipython().run_line_magic('matplotlib', 'inline')
import altair as alt 


# > Load in your dataset and describe its properties through the questions below.
# Try and motivate your exploration goals through this section.

# In[183]:


#uploading data set 
loan = pd.read_csv('prosperLoanData.csv')
loan.head()


# In[184]:


loan.shape


# In[185]:


loan.columns


# In[186]:


loan.info()


# ### What is the structure of your dataset?
# 
# > this a dataset of loans details from (https://www.prosper.com/)
# 
# >and this data contain the following
# 'ListingKey', 'ListingNumber', 'ListingCreationDate', 'CreditGrade',
#        'Term', 'LoanStatus', 'ClosedDate', 'BorrowerAPR', 'BorrowerRate',
#        'LenderYield', 'EstimatedEffectiveYield', 'EstimatedLoss',
#        'EstimatedReturn', 'ProsperRating (numeric)', 'ProsperRating (Alpha)',
#        'ProsperScore', 'ListingCategory (numeric)', 'BorrowerState',
#        'Occupation', 'EmploymentStatus', 'EmploymentStatusDuration',
#        'IsBorrowerHomeowner', 'CurrentlyInGroup', 'GroupKey',
#        'DateCreditPulled', 'CreditScoreRangeLower', 'CreditScoreRangeUpper',
#        'FirstRecordedCreditLine', 'CurrentCreditLines', 'OpenCreditLines',
#        'TotalCreditLinespast7years', 'OpenRevolvingAccounts',
#        'OpenRevolvingMonthlyPayment', 'InquiriesLast6Months', 'TotalInquiries',
#        'CurrentDelinquencies', 'AmountDelinquent', 'DelinquenciesLast7Years',
#        'PublicRecordsLast10Years', 'PublicRecordsLast12Months',
#        'RevolvingCreditBalance', 'BankcardUtilization',
#        'AvailableBankcardCredit', 'TotalTrades',
#        'TradesNeverDelinquent (percentage)', 'TradesOpenedLast6Months',
#        'DebtToIncomeRatio', 'IncomeRange', 'IncomeVerifiable',
#        'StatedMonthlyIncome', 'LoanKey', 'TotalProsperLoans',
#        'TotalProsperPaymentsBilled', 'OnTimeProsperPayments',
#        'ProsperPaymentsLessThanOneMonthLate',
#        'ProsperPaymentsOneMonthPlusLate', 'ProsperPrincipalBorrowed',
#        'ProsperPrincipalOutstanding', 'ScorexChangeAtTimeOfListing',
#        'LoanCurrentDaysDelinquent', 'LoanFirstDefaultedCycleNumber',
#        'LoanMonthsSinceOrigination', 'LoanNumber', 'LoanOriginalAmount',
#        'LoanOriginationDate', 'LoanOriginationQuarter', 'MemberKey',
#        'MonthlyLoanPayment', 'LP_CustomerPayments',
#        'LP_CustomerPrincipalPayments', 'LP_InterestandFees', 'LP_ServiceFees',
#        'LP_CollectionFees', 'LP_GrossPrincipalLoss', 'LP_NetPrincipalLoss',
#        'LP_NonPrincipalRecoverypayments', 'PercentFunded', 'Recommendations',
#        'InvestmentFromFriendsCount', 'InvestmentFromFriendsAmount',
#        'Investors'],
# ### What is/are the main feature(s) of interest in your dataset?
# 
# > 'ListingKey','ListingNumber','CreditGrade','ClosedDate','EmploymentStatus',
#             'IsBorrowerHomeowner','BankcardUtilization','IncomeRange','IncomeVerifiable',
#             'LoanCurrentDaysDelinquent','MemberKey','Investors',
#           'BankcardUtilization','EstimatedLoss','AmountDelinquent','LoanOriginalAmount'
# 
# ### What features in the dataset do you think will help support your investigation into your feature(s) of interest?
# 
# >  fisrt , foucse in features which related to the borrower himself . 
# > second , relation between behavioure of the borrow a and how this reflect in increasing the investors or  not . 

# ### i'm Trying to check the criteria of person which get loans and the any parameter affact the increasing  the investmment to this loans 

# #### So i will select this specific data which i think it will help me to extract answers for my question 

# In[187]:


df= loan[['ListingKey','ListingNumber','CreditGrade','ClosedDate','EmploymentStatus',
            'IsBorrowerHomeowner','IncomeRange','IncomeVerifiable',
            'LoanCurrentDaysDelinquent','MemberKey','Investors',
          'BankcardUtilization','EstimatedLoss','EstimatedReturn', 
          'BorrowerAPR', 'LoanMonthsSinceOrigination', 
          'LoanOriginalAmount', 'MonthlyLoanPayment',
          'AmountDelinquent','Occupation',
          'Term','StatedMonthlyIncome',
          'ListingCategory (numeric)','ProsperRating (Alpha)','LoanStatus','AvailableBankcardCredit','Recommendations','ProsperScore','PercentFunded',
          'TradesOpenedLast6Months']]
df.head()


# In[188]:


df.info()


# In[ ]:





# ##### if  person owning home affect acceptance of bank to give loans ?

# In[189]:


df.IsBorrowerHomeowner.value_counts()


# In[190]:


df.IsBorrowerHomeowner.value_counts()


# In[ ]:





# ## Univariate Exploration
# 
# > In this section, investigate distributions of individual variables. If
# you see unusual points or outliers, take a deeper look to clean things up
# and prepare yourself to look at relationships between variables.

# In[191]:


plt.figure(figsize = [8, 10])
labels = 'Owning Home', 'Not Owning Home'
sizes = df.IsBorrowerHomeowner.value_counts()
explode = (0, 0.1)  # only "explode" the 2nd slice (i.e. 'Hogs')

fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
# Equal aspect ratio ensures that pie is drawn as a circle.
ax1.axis('equal') 
plt.show()


# ##### answer : borrows  who have loans around 50% of them didn't own home so owning home not affect the granting loans to person .

#  
# 

# In[192]:


df.IncomeRange.value_counts()


# In[193]:


from matplotlib import rcParams
# Specify the figure size in inches, for both X, and Y axes
rcParams['figure.figsize'] = 14,4


# In[194]:


# Considering the same chart from the Example 1 above, print the text (proportion) BELOW the bars
plt.figure(figsize = [14.7 , 8.27])
type_counts = df["IncomeRange"].value_counts()
type_order = ['$0','$1-24,999','$25,000-49,999','$25,000-49,999','$50,000-74,999','$75,000-99,999','$100,000+','Not employed']
sb.countplot(data=df, x="IncomeRange", order=type_order , orient="h");
n_df = df["IncomeRange"].value_counts().sum()
# get the current tick locations and labels
locs, labels = plt.xticks(rotation=45) 

# loop through each pair of lodf.head cations and labels
for loc, label in zip(locs, labels):

    # get the text property for the label to get the correct count
    count = type_counts[label.get_text()]
    pct_string = '{:0.1f}'.format(count)

    # print the annotation just below the top of the bar
    plt.text(loc, count+2, pct_string, ha = 'center', color = 'black')
plt.tight_layout();


# ####  we found most of the borrower have  income range from ( 25K : 50K) dollar 

# > Make sure that, after every plot or related series of plots, that you
# include a Markdown cell with comments about what you observed, and what
# you plan on investigating next.

# #### credit grade count  to see  which credit Grades is trend 

# In[195]:


df_credit_grade =  df.CreditGrade.value_counts()
df_credit_grade


# In[196]:


df['BankcardUtilization'].dropna(inplace = True )


# In[197]:


df['AvailableBankcardCredit'].dropna(inplace = True )


# In[198]:


df['AvailableBankcardCredit'].shape


# In[199]:


sb.displot(df , x="AvailableBankcardCredit" , bins = 'auto' )
plt.tight_layout();
plt.title('availabe bank credit frequency Distribution');


# ##### use a scale to make the disribuation is clear . 

# In[200]:


f, ax = plt.subplots(figsize=(7, 7))
ax.set(xscale="log", yscale="log")
sb.distplot(df['AvailableBankcardCredit']  , vertical= False , norm_hist=False,
            axlabel='Distribution',label=" Borrower Annual Percent Rate ")
plt.tight_layout();
plt.title('availabe bank credit frequency Distribution with log scale ');


# 

# In[ ]:





# In[201]:


type_counts = df["EmploymentStatus"].value_counts()
type_counts


# In[202]:


# Considering the same chart from the Example 1 above, print the text (proportion) BELOW the bars
type_counts = df["EmploymentStatus"].value_counts()
type_order = type_counts.index
sb.countplot(data=df, x="EmploymentStatus", order=type_order);
n_df = df["EmploymentStatus"].value_counts().sum()
# get the current tick locations and labels
locs, labels = plt.xticks(rotation=45) 

# loop through each pair of lodf.head cations and labels
for loc, label in zip(locs, labels):

    # get the text property for the label to get the correct count
    count = type_counts[label.get_text()]
    pct_string = '{:0.1f}'.format(count)

    # print the annotation just below the top of the bar
    plt.text(loc, count+2, pct_string, ha = 'center', color = 'black')
plt.tight_layout();


# In[203]:


type_counts = df['Occupation'].value_counts()
type_order = type_counts.index
plt.figure(figsize=[12,20]);
sb.countplot(data = df,y= 'Occupation' , order=type_order);
plt.title('Occupation frequency Distribution');
plt.ylabel('Count')
plt.xlabel('Occupation')
plt.xscale ('log')
plt.tight_layout();


# 
# ###### above plot to show trend of occupuation  and acorrding to graph above we found trend for people without recoded name , also second names with tricky name is Professional  , but the third is programmer  and less is student techincal school and i think is normal 
# ### in general we have maginfier which tells us which people occupation is tend to borrow .

# In[204]:


sb.distplot(df['BorrowerAPR']  , color='Green', vertical= False , norm_hist=False,
            axlabel='Distribution', label=" Borrower Annual Percent Rate ")


# ####  represensting The Borrower's Annual Percentage Rate (APR) for the loan distubation to explore the trend

# ### Discuss the distribution(s) of your variable(s) of interest. Were there any unusual points? Did you need to perform any transformations?
# > drawing a conculasion about the borower (ownhome or not , his occupation , income range , annual rate for loans )
# > borrows  who have loans around 50% of them didn't own home so owning home not affect the granting loans to person .
# >  most of the borrower have income range from ( 25K : 50K) dollar
# >  most of the borrowe is empolyed . 
# 
# ### Of the features you investigated, were there any unusual distributions? Did you perform any operations on the data to tidy, adjust, or change the form of the data? If so, why did you do this?
# 
# > scale is used to show the distribution of bank utilization !
# > also occupation 

# ## Bivariate Exploration
# 
# > In this section, investigate relationships between pairs of variables in your
# data.
# assuring that all  variables that you cover here have been introduced in some
# fashion in the previous section (univariate exploration).

# #### in this Section , some relation between  two factor to the study the effect of some varible to each other  are  represented .

# ##### a relation between 2 varible which will study relation between  lonaer criteria and investment to show if this  studied criteria  affect the investment .

# In[205]:


#dividing the in two data set depending on owning home or not .
df_home_True = df.query('IsBorrowerHomeowner ==  True ')
df_home_False = df.query('IsBorrowerHomeowner ==  False ')
df_home_False.info()


# In[206]:


#grouping the dataframe accroding to income range and owning home and get size .
ct_counts = df.groupby(['IncomeRange', 'IsBorrowerHomeowner']).size()
ct_counts = ct_counts.reset_index(name='count')


# In[207]:


#making a pivot table IsBorrowerHomeowner is column and row IncomeRange 
ct_counts = ct_counts.pivot(index = 'IncomeRange', columns = 'IsBorrowerHomeowner', values = 'count')


# In[208]:


fig, ax = plt.subplots(figsize= [ 14.70, 8.27])
sb.heatmap(ct_counts , annot = True, fmt = 'd' , ax = ax )


# In[209]:


sb.set_theme(style="darkgrid")
fig, ax = plt.subplots(figsize= [ 14.70, 8.27])
sb.countplot(data = df, x = 'IsBorrowerHomeowner', hue= 'IncomeRange' , ax = ax )


# #### different method is used  to observe the relation between owning home and income range  and liky found that the range of 100k dollar is person who owning home is more . 
# 

# In[210]:


df['StatedMonthlyIncome'].head()


# In[211]:


#regression plot to show the line which represent the correlation .
fig, ax = plt.subplots(figsize= [ 14.70, 8.27])
sb.regplot(data = df,y = 'StatedMonthlyIncome', x = 'BorrowerAPR', color = 'blue'  , ax = ax );
plt.xlabel('BorrowerAPR')
plt.ylabel('StatedMonthlyIncome')
plt.yscale('symlog')
plt.tight_layout();


# In[212]:


#also extract this relation numerically 
df['BorrowerAPR'].corr(df['StatedMonthlyIncome'])


# ##### Test relation between two quantattive values 

# ###  correlation factor is very small of colleration and graph 

# In[213]:


df["LoanStatus"].value_counts()


# #### I will drop completed  , final pyment in progresss and cancelled status 

# In[214]:


#remove loanStatus which will not make sense .
df.drop(df[df['LoanStatus'] == 'Completed' ].index, inplace=True)
df.drop(df[df['LoanStatus'] == 'FinalPaymentInProgress'].index, inplace=True)
df.drop(df[df['LoanStatus'] == 'Cancelled' ].index, inplace=True)


# In[215]:


df['LoanStatus']


# In[216]:


#using countplot to show the repeated of each status 
ax.set(yscale="log")
sb.set_theme(style="darkgrid")
a4_dims = (11.7, 8.27)
fig, ax = plt.subplots(figsize= [ 14.70, 8.27])
sb.countplot(data = df, y = 'LoanStatus' , ax=ax )


# ##### represent distribution of loan status 

# In[217]:


plt.figure(figsize=[ 14.70, 8.27])
a=np.random.random(100)*0.5 #a uniform distribution
b=np.random.normal(100)*0.5 #a normal distribution
c=np.random.random(100)*0.5 #a uniform distribution
d=np.random.random(100)*0.5 #a uniform distribution
e=np.random.random(100)*0.5 #a uniform distribution
f=np.random.random(100)*0.5 #a uniform distribution
#bins 
bins=np.histogram(np.hstack((a,b,c,d,e,f)), bins=40)[1] #get the bin edges
Rating = ['C',  'D', 'E','HR','A','B']
Classes = pd.api.types.CategoricalDtype(ordered=True, categories = Rating);
df["ProsperRating (Alpha)"] = df["ProsperRating (Alpha)"].astype(Classes);
#Plot the Seaborn's FacetGrid
g = sb.FacetGrid(data = df , col = "ProsperRating (Alpha)" , col_wrap=3, sharey=False , height = 8.27/4,  aspect = (14.70/3)/(8.27/4));
g.map(plt.hist, "EstimatedReturn" );
plt.tight_layout();


# #### representing sample prospor rating and estimated return 

# In[218]:


g = sb.FacetGrid(data = df, hue = 'ProsperRating (Alpha)', hue_order = ['HR','E','D','C','B','A','AA'], size = 5, aspect = 1.5 , palette="husl")
g.map(sb.regplot, "EstimatedReturn","StatedMonthlyIncome", fit_reg = False);
plt.legend(loc=1, fontsize = 9)


# ##### this a relation between  Estimated return and Stated monthly income  with respect to prosper raring 

# #### this a relation between Borrow annaul per revnue  and Stated monthly income with respect to prosper raring

# In[219]:


sb.boxplot(data = df , x='ProsperScore', y = 'EstimatedReturn')


# #### five number analysis between  prospor score and Estimated Return 

# 

# In[220]:


df.dropna(subset = ['ProsperScore', 'Investors'], inplace=True)


# In[221]:


df['Investors'].head(20)


# In[222]:


df.dropna(subset =  ['ProsperScore', 'Investors'], inplace = True )
df['Investors'].head(20)
plt.figure(figsize = [14.7, 8.27])

# PLOT ON LEFT
plt.subplot(1, 2, 1)
sb.stripplot(data = df, y = 'Investors', x = 'ProsperScore' , jitter = 0.35 , color =  'teal') 
plt.xlabel('ProsperScore')
plt.ylabel('Investors');

# PLOT ON RIGHT
plt.subplot(1, 2, 2)
sb.stripplot(data = df, y = 'Investors', x = 'Recommendations' , jitter = 0.35 , color =  'teal')
plt.xlabel('Recommendations')
plt.ylabel('Investors')
plt.suptitle('Distribustion of prosper Score and Recommendation')          
plt.tight_layout();


# ##### this relation to assure the affect of recoomandation and prospor score on recommandation 

# 

# #### in income range from 50,000 to 74.999  ,   and from range  have the heighst income range 

# ### Talk about some of the relationships you observed in this part of the investigation. How did the feature(s) of interest vary with other features in the dataset?
# 
# > fisrt i discussed the realtion between income of borrower and income . 
# > second showed the correlation BorrowerAnnual per rate   Stated Monthly Income'
# > representing sample prospor rating and estimated return. 
# > this a relation between Estimated return and Stated monthly income with respect to prosper raring.
# > this a relation between Borrow annaul per revnue and Stated monthly income with respect to prosper raring
# this relation to assure the affect of recoomandation and prospor score on recommandation
# ### Did you observe any interesting relationships between the other features (not the main feature(s) of interest)?
# 
# > negative  weak correlation correlation BorrowerAnnual per rate   Stated Monthly Income.
# > postive relation between prospor score and investors  also unlikly negative realtion between recommendation and investors 

# ## Multivariate Exploration
# 
# > Create plots of three or more variables to investigate your data even
# further. Make sure that your investigations are justified, and follow from
# your work in the previous sections.

# In[223]:


#relation between prosperscore , recommendation with respect ProsperRating 
g = sb.FacetGrid(data = df, hue = 'ProsperRating (Alpha)', hue_order = ['HR','E','D','C','B','A','AA'], size = 5, aspect = 1.5 , palette="husl")
g.map(sb.regplot,"ProsperScore" , "Recommendations", fit_reg = False);
plt.legend(loc=1, fontsize = 9)


# 

# In[224]:


df['LoanOriginalAmount']


# In[225]:


g = sb.FacetGrid(data = df, hue = 'ProsperRating (Alpha)', hue_order = ['HR','E','D','C','B','A','AA'], size = 5, aspect = 1.5 , palette="husl")
g.map(sb.regplot, "BorrowerAPR","EstimatedReturn", fit_reg = False);
plt.legend(loc=1, fontsize = 9)
plt.xscale('symlog')


# In[226]:


df["BorrowerAPR"].corr(df["EstimatedReturn"])


# ##### this a relation between Borrow annaul per revnue and Stated monthly income with respect to prosper raring

# In[227]:


plt.figure(figsize = [14.7, 8.27])
sb.set_theme(style="ticks")

# Load the penguins dataset
penguins = sb.load_dataset("penguins")

# Show the joint distribution using kernel density estimation
g = sb.lmplot(
    data=df,
    y = 'MonthlyLoanPayment', x = 'LoanOriginalAmount', hue= 'Term',
     height=5,
)
plt.tight_layout();


# #### show realtion between term of loans period by month and loan original amount with respect to monthly loan payment 

# In[228]:


df_numeric = ['EstimatedReturn', 'BorrowerAPR', 'Term', 'Investors','MonthlyLoanPayment']
df_categoric = ['IncomeRange', 'CreditScore', 'IsBorrowerHomeowner']

# correlation plot
plt.figure(figsize = [14, 8])
sb.heatmap(df[df_numeric].corr(), annot = True, fmt = '.3f', cmap = 'viridis_r', center = 0 , label = 'correlation between some numeric values ')
plt.show()
g.set_axis_labels(x_var="Percentage Depth", y_var="Number of Defects")


# ##### heat map for some numeric values which represents correlation between this numeric values 

# ### Talk about some of the relationships you observed in this part of the investigation. Were there features that strengthened each other in terms of looking at your feature(s) of interest?
# 
# > relation between prospor score and recommendation with referance to prospor rating alpha
#   major of with A score
# >this a relation between Borrow annaul per revnue and Stated monthly income with respect to prosper raring
# > show realtion between term of loans period by month and loan original amount with respect to monthly loan payment 
# ### Were there any interesting or surprising interactions between features?
# > correlation between BorrowerAPR  EstimatedReturn is 0.8 strong postive relation 

# > At the end of your report, make sure that you export the notebook as an
# html file from the `File > Download as... > HTML` menu. Make sure you keep
# track of where the exported file goes, so you can put it in the same folder
# as this notebook for project submission. Also, make sure you remove all of
# the quote-formatted guide notes like this one before you finish your report!

# In[230]:


get_ipython().system('jupyter nbconvert Visualizationudacityproject.ipynb --to slides --post serve --template output_toggle')


# In[ ]:




