import sys, locale, os
import urllib.request
from bs4 import BeautifulSoup
import codecs

#input file with all Yelp links
f = open('All Links.txt', 'r')
f.readline()
for line in f:
        print (line, '\n')
        
        url = line
        ourUrl = urllib.request.urlopen(url)
        soup = BeautifulSoup(ourUrl)

        #Address for the store
        address_string = soup.address
        addEn = str(address_string).index('</address>')
        print("address_string: ",str(address_string)[18:addEn], '\n')

        #Review Count for the store
        reviewCnt_string = str(soup.findAll('meta', attrs={'name':'description'}))
        reviewCntEn = str(reviewCnt_string).index('Review')
        print("reviewCnt_string: ",str(reviewCnt_string)[16:reviewCntEn], '\n')

        #User Location
        userLoc_string = str(soup.findAll('li', attrs={'class':'user-location'}))
        userLocEn = str(userLoc_string).index('</b>')
        len_userLoc_string = len(userLoc_string)
        #print("userLoc_string: ",str(userLoc_string)[31:userLocEn], '\n')

        #User Rating
        userRat_string = str(soup.findAll('meta', attrs={'itemprop':'ratingValue'}))
        userRatEn = str(userRat_string).index('</meta>')
        len_userRat_string = len(userRat_string)
        #print("userRat_string: ",str(userRat_string), '\n')


        #Comment
        new_string = str(soup.findAll('p', attrs={'itemprop':'description'})) 
        len_new_string = len(new_string)
        a = new_string.index('</p>')

        with open ('yelp_data.txt','a') as csvfile: #Open file to write        
            i = 0
            csvfile.write('\n')
            csvfile.write('\n')
            csvfile.write("Store URL: "+ str(url)+ '\n')
            csvfile.write("Store Address: "+ str(address_string)[18:addEn] + '\n')
            csvfile.write("Review #: " + str(reviewCnt_string)[16:reviewCntEn] + '\n')
            
            while a > 0: #While not end of file
                    try:
                        a = new_string.index('</p>')
                        userLocEn = str(userLoc_string).index('</b>')
                        userRatEn = str(userRat_string).index('</meta>')
                        #print("index of </p> is:" + str(a))
                        
                    except ValueError:
                        break
                
                    review = new_string[0:a]
                    len_review = len(review)
                    
                    userLoc = userLoc_string[0:userLocEn]
                    len_userLoc = len(userLoc)
                    
                    userRat = userRat_string[0:userRatEn]
                    len_userRat = len(userRat)
                    
                    if '<br>' in review:
                        review.replace('<br>', '')
                        

                    review=review.encode('utf-8')
                    
                    print(userLoc, '\n')
                    print(userRat, '\n')
                    print(review, '\n')
                        
                    csvfile.write(userLoc + '\n')
                    csvfile.write(userRat + '\n')
                    csvfile.write(str(review) + '\n')
                    
                    # new contenxt starts from the end of one review to the end
                    new_string = new_string[-(len_new_string - len_review - 6):]
                    len_new_string = len(new_string)
                    
                    # new contenxt starts from the end of one userLoc to the end
                    userLoc_string = userLoc_string[-(len_userLoc_string - len_userLoc - 40):]
                    len_userLoc_string = len(userLoc_string)

                    # new contenxt starts from the end of one userRat to the end
                    userRat_string = userRat_string[-(len_userRat_string - len_userRat - 24):]
                    len_userRat_string = len(userRat_string)
                    
                    i = i + 1
                    if i > 39: #Get 40 reviews on this page 
                            break
            
        
