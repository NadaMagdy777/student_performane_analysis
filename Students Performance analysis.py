import pandas as pd
import matplotlib.pyplot as plt

def filter_summary(gender,race,ploe, df):

    filtered_rides = len(df)
    print('Filters (gender, race, parental level of education):        ', gender,', ', race,", ",ploe)
    print('Rides in filtered set:       ',filtered_rides)
    print("-"*40)

def get_gender():
    gender_dict={"1":"female","2":"male"}
    print("\nwhich gender\n")
    display_dict(gender_dict)
    gender=input("your choice: ")
    while(gender not in gender_dict.keys()):
        print('\nplease enter correct gender type\n')
        display_dict(gender_dict)
        gender=input("your choice: ")
    print("-"*40)
    
    return gender_dict[gender]
    
    
def get_race_ethnicity():
    race_ethnicity_dict={"1":"group A","2":"group B","3":"group C","4":"group D","5":"group E"}
    print("\nwhich race/ethnicity  ?\n")
    display_dict(race_ethnicity_dict)
    race=input("your choice: ")
    while(race not in race_ethnicity_dict.keys()):
        print('\nplease enter correct race_ethnicity type\n')
        display_dict(race_ethnicity_dict)
        race=input("your choice: ")
    print("-"*40)
    return race_ethnicity_dict[race]
     


# ploe -> parental level of education
def get_ploe():
    ploe_dict={"1":'some college',"2":'associate degree' ,"3":'high school ' , "4":'some high school',"5":'bachelor\'s degree', "6":'master\'s degree'}
    print("\nwhich parental level of education   ?\n")
    display_dict(ploe_dict)
    ploe=input("your choice: ")
    while(ploe not in ploe_dict.keys()):
        print('\nplease enter correct parental level of education\n ')
        display_dict(ploe_dict)
        ploe=input("your choice: ")
    print("-"*40)
    return ploe_dict[ploe]




#filter data 
def filter_data():
    gender=None
    ploe=None
    race=None
    filter_by={'1':'gender' ,'2':'race/ethnicity','3':'parental level of education','4':'all','5':"none"}
    print('\nwhould you like to filter data\n ') 
    display_dict(filter_by)
    filter_input=input("your choice: ").strip().lower()
    
    while(filter_input not in filter_by.keys()) :
        print('please enter correct chooces')
        display_dict(filter_by)
        filter_input=input().strip().lower()
    
    else:
        if(filter_input=='1' or filter_input=='4'):
           print("-"*40) 
           gender= get_gender()
          
    
        if(filter_input=='2' or filter_input=='4'):
            print("-"*40) 
            race=get_race_ethnicity()
           
        if(filter_input=='3' or filter_input=='4'):
            print("-"*40) 
            ploe=get_ploe()
         
    return gender,race,ploe
            

#send dictionary and print it    
def display_dict(dictionary):
    for key in dictionary:
        print("\tEnter {0} For Filter By {1}".format(key,dictionary[key]))
    

#return data after filter
def load_data(gender,race,ploe):
    data=pd.read_csv("StudentsPerformance.csv")     
    if( gender!=None ):
        data=data[data["gender"]==gender]
    if(race != None):
        data=data[data["race/ethnicity"]==race]
    if(ploe != None):
        data=data[data["parental level of education"]==ploe]
    
    return data

def gender_question(df):
    
    """Displays statistics on the most popular gender ."""
    print('\nCalculating The Most Popular gender type ...\n')
    common_gender=df["gender"].value_counts()
    print ('common gender in data is \t ( {0} ) '.format(common_gender.index[0]))
    plt.pie(common_gender[0:len(common_gender)],labels=common_gender.index,shadow=True,explode=[0.05,0.05],autopct='%1.1f%%')
    plt.title("common gender")
    plt.axis("equal")
    plt.show()
    print("-"*40)

def race_ques(df):
     """Displays statistics on the most and less popular group in 'race/ethnicity'."""
     print("\nCalculating the most and less popular group in 'race/ethnicity\n")
     common_race_group=df["race/ethnicity"].value_counts()
     print("common group in 'race/ethnicity is\t ( {0} )".format(common_race_group.index[0]))
     print("less group in 'race/ethnicity is\t ( {0} )".format(common_race_group.index[len( common_race_group)-1]))
     print("-"*40)
     x=common_race_group.index[0:len(common_race_group)]
     y=common_race_group[0:len(common_race_group)]
     plt.bar(x,y)
     plt.title("common group in race/ethnicity")
     for xx,yy in zip(x,y):
         plt.text(xx,yy,yy)
     
     plt.show()

#ploe -> parental level of education
def ploe_ques(df):
     """Displays statistics on the most and less popular level in parental level of education"""
     print("\nCalculating the most and less popular level in parental level of education\n")
     common_level=df["parental level of education"].value_counts()
     print("common level in parental level of education is\n\t ( {0} )".format(common_level.index[0]))
     print("less level in parental level of educationis\n\t ( {0} )".format(common_level.index[len( common_level)-1]))
     plt.pie(common_level[0:len(common_level)],labels=common_level.index,shadow=True,explode=[0.05,0.05,0.05,0.05,0.05,0.05],autopct='%1.1f%%')
     plt.title("common level")
     plt.axis("equal")
     plt.show()
     print("-"*40)
     

def lunch_ques(df):
     """Displays statistics on the most popular lunch type """
     print("\nCalculating the most popular lunch type\n")
     common_type=df["lunch"].value_counts()
     print("common type in lunch is\n\t ( {0} )".format(common_type.index[0]))
     plt.pie(common_type[0:len(common_type)],labels=common_type.index,shadow=True,explode=[0.05,0.05],autopct='%1.1f%%')
     plt.title("common type")
     plt.axis("equal")
     print("-"*40)

def Tcp_ques(df):
     """Displays statistics on the most  popular type in test preparation course"""
     print("\nCalculating the most popular test preparation course type\n")
     common_type=df["test preparation course"].value_counts()
     print("common type in test preparation course is\t ( {0} )\n".format(common_type.index[0]))
     print("number of students that {0}  test preparation course is\t ( {1} )\n".format(common_type.index[0],common_type[0]))
     print("number of students that {0}  test preparation course is\t ( {1} )\n".format(common_type.index[len(common_type)-1],common_type[len(common_type)-1]))
     plt.pie(common_type[0:len(common_type)],labels=common_type.index,shadow=True,explode=[0.05,0.05],autopct='%1.1f%%')
     plt.title("test preparation course")
     plt.axis("equal")
     print("-"*40)
 
def material_grads(material_name,df):
     """Displays statistics on the most  popular grades in material"""
     print("\nCalculating the most popular grades in {0}\n".format(material_name))
     common_score=df[material_name].value_counts()
     max_score=max(df[material_name])
     min_score=min(df[material_name])
     print("common score in student {0} is\t ( {1} )".format(material_name,common_score.index[0]))
     print("max score in student {0} is\t     ( {1} )".format(material_name,max_score))
     print("min score in student {0} is\t     ( {1} )".format(material_name,min_score))
     print("number of students get max score is\t     ( {0} )".format(common_score[max_score]))
     print("number of students get min score is\t     ( {0} )".format(common_score[min_score]))
     x=common_score.index[0:5]
     y=common_score[0:5]
     plt.bar(x,y,color="b",width=0.9)
     plt.title("common {0}".format(material_name))
     for xx,yy in zip(x,y):
         plt.text(xx,yy,yy)
     plt.show()
     print("-"*40)
    
def math_ques(df):
     """Displays statistics on the most  popular grades in math_score"""
     material_grads("math score",df)

def reading_ques(df):
     """Displays statistics on the most  popular scores in reading_score"""
     material_grads("reading score",df)

def writing_ques(df):
     """Displays statistics on the most  popular scores in reading_score"""
     material_grads("writing score",df)

def show_raw(df):
    
    """display 5 raw"""
    request=input("Would you like to see some raw data from the current dataset?(y or n):  ").lower().strip()
    row_length=0
    while(request!='n' and row_length<=len(df)):
        if(request=='y'):
            print(" Displaying rows {0} to {1}:".format(row_length,row_length+5))
            print(df[row_length:row_length+5])
            row_length+=5
            request=input("Would you like to see the next 5 rows?(y or n):  "  )
        else:
           request=input("please enter (y or n)")
           
def main():
  while True:
   gender,race,ploe=filter_data()
   df= load_data(gender,race,ploe)
   filter_summary(gender,race,ploe, df)
   gender_question(df)
   race_ques(df)
   ploe_ques(df)
   lunch_ques(df)
   Tcp_ques(df)
   math_ques(df)
   reading_ques(df)
   writing_ques(df)
   show_raw(df)
   restart = input('\nWould you like to restart? Enter yes or no.\n')
   if restart.lower() != 'yes':
            break
main()
    
