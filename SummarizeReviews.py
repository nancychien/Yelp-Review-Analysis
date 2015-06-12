import csv
import re

yelpComment = csv.reader(open('Bad Comments.csv'), delimiter='\t')

#Define Complaints String Array
S_Product =  ["Coffee", "drink", "drinks", "cup", "latte","tea","iced", "milk","food","wrong"]
#S_Product = ["sandwich","food"]
S_Service = ["people","service","staff","barista","baristas","rude","cashier","manager","friendly","attitude"]
S_Environment = ["bathroom", "small", "clean", "seating"]
S_WatingTime =  ["time","line","minutes","long","wait","slow","waiting","busy"]
S_Location = ["location", "place"]
#S_Service = ["time", "people","line","service","employees","staff","barista","minutes","long","slow","late","waiting","casheier"]

#Initial All Flags & Loop Number
rownum = 0
colnum = 0
ifService = "No"
ifProduct = "No"
ifEnvironment = "No"
ifWaitingTime = "No"
ifLocation = "No"

#Open file to write
with open ('Word_Freq.csv','a') as csvfile:
    csvfile.write('Comment'+'\t'+'Service Complaint'+'\t'+'Product Complaint'+'\t'+'Environment Complaint'+'\t'+'Waiting Complaint'+'\t'+'Location Complaint'+'\n')
   
    for row in yelpComment:
        if rownum == 0:
            header = row
        else:
            colnum = 0        
            for col in row:
                values = re.split(r'\t+',col)
                print('The ',rownum, 'Comment: ', values[0])
                csvfile.write(values[0]+'\t')
                
                ####### Check if the comment has service complaint ####### 
                s = 0
                serviceLen=len(S_Service)
                for s in range(0,serviceLen):
                    #print ("Try to Find: ", S_Service[s])

                    #See if find service complaint substring in each comment
                    if values[0].upper().find(S_Service[s].upper())> -1:
                        print ('Found', S_Service[s].upper())
                        ifService = "Yes"
                        break;
                    else:
                        ifService = "No"
                        
                ####### Check if the comment has product complaint ####### 
                p = 0
                productLen=len(S_Product)
                for p in range(0,productLen):
                    #print ("Try to Find: ", S_Product[p])
                    
                    #See if find product complaint substring in each comment
                    if values[0].upper().find(S_Product[p].upper())> -1:
                        print ('Found', S_Product[p].upper())
                        ifProduct = "Yes"
                        break;
                    else:
                        ifProduct = "No"

                ####### Check if the comment has environment complaint ####### 
                e = 0
                environmentLen=len(S_Environment)
                for e in range(0,environmentLen):
                    #print ("Try to Find: ", S_Environment[e])
                    
                    #See if find environment complaint substring in each comment
                    if values[0].upper().find(S_Environment[e].upper())> -1:
                        print ('Found', S_Environment[e].upper())
                        ifEnvironment = "Yes"
                        break;
                    else:
                        ifEnvironment = "No"
                        
                ####### Check if the comment has waiting-time complaint ####### 
                w = 0
                waitingLen=len(S_WatingTime)
                for w in range(0,waitingLen):
                    #print ("Try to Find: ", S_WatingTime[w])
                    
                    #See if find waiting-time complaint substring in each comment
                    if values[0].upper().find(S_WatingTime[w].upper())> -1:
                        print ('Found', S_WatingTime[w].upper())
                        ifWaitingTime = "Yes"
                        break;
                    else:
                        ifWaitingTime = "No"

                ####### Check if the comment has location complaint ####### 
                l = 0
                locationLen=len(S_Location)
                for l in range(0,locationLen):
                    #print ("Try to Find: ", S_Location[l])
                    
                    #See if find location complaint substring in each comment
                    if values[0].upper().find(S_Location[l].upper())> -1:
                        print ('Found', S_Location[l].upper())
                        ifLocation = "Yes"
                        break;
                    else:
                        ifLocation = "No"
               
                colnum = colnum + 1
        #Output
        if rownum > 0:
            print('The ',rownum, 'Comment: Service Complaint:', ifService)
            print('The ',rownum, 'Comment: Product Complaint:', ifProduct)
            print('The ',rownum, 'Comment: Environment Complaint:', ifEnvironment)
            print('The ',rownum, 'Comment: Waiting-Time Complaint:', ifWaitingTime)
            print('The ',rownum, 'Comment: Location Complaint:', ifLocation)
            
            csvfile.write(ifService+'\t'+ifProduct+'\t'+ifEnvironment+'\t'+ifWaitingTime+'\t'+ifLocation+'\n')
            
        rownum += 1
    
